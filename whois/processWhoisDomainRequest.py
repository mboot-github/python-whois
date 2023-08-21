import sys

from typing import (
    cast,
    Optional,
    List,
    Dict,
    # Tuple,
    Any,
)

from .exceptions import WhoisPrivateRegistry
from .exceptions import UnknownTld

from ._0_init_tld import filterTldToSupportedPattern
from ._0_init_tld import TLD_RE

from .doWhoisCommand import doWhoisAndReturnString
from .doParse import do_parse
from .domain import Domain
from .parameterContext import ParameterContext
from .lastWhois import updateLastWhois


class ProcessWhoisDomainRequest:
    def __init__(
        self,
        domain: str,
        pc: ParameterContext,
    ) -> None:
        self.domain = domain
        self.pc = pc
        self.tldString: Optional[str] = None

    def setThisTldEntry(self, thisTld: Dict[str, str]) -> None:
        self.thisTld = thisTld

    def _fromDomainStringToTld(
        self,
    ) -> Optional[List[str]]:
        def _internationalizedDomainNameToPunyCode(d: List[str]) -> List[str]:
            return [k.encode("idna").decode() or k for k in d]

        self.domain = self.domain.lower().strip().rstrip(".")  # Remove the trailing dot to support FQDN.

        dList: List[str] = self.domain.split(".")
        if self.pc.verbose:
            print(dList, file=sys.stderr)

        if dList[0] == "www":
            dList = dList[1:]

        if len(dList) == 1:
            self.tldString = None
            return None
        else:
            self.tldString = filterTldToSupportedPattern(
                self.domain,
                dList,
                self.pc.verbose,
            )  # may raise UnknownTld

            if self.pc.verbose:
                print(f"filterTldToSupportedPattern returns tld: {self.tldString}", file=sys.stderr)

            if self.pc.internationalized:
                dList = _internationalizedDomainNameToPunyCode(dList)

            return dList

    def makeMessageForUnsupportedTld(
        self,
    ) -> Optional[str]:
        if self.pc.return_raw_text_for_unsupported_tld:
            return None

        a = f"The TLD {self.tldString} is currently not supported by this package."
        b = "Use validTlds() to see what toplevel domains are supported."
        msg = f"{a} {b}"
        return msg

    def _doUnsupportedTldAnyway(
        self,
        dList: List[str],
    ) -> Optional[Domain]:
        # we will not hunt for possible valid first level domains as we have no actual feedback
        self.pc.include_raw_whois_text = True
        whoisStr = doWhoisAndReturnString(
            dList=dList,
            pc=self.pc,
        )

        # we will only return minimal data
        data: Dict[str, Any] = {
            "tld": self.tldString,
            "domain_name": [],
        }
        data["domain_name"] = [".".join(dList)]  # note the fields are default all array, except tld
        self.pc.return_raw_text_for_unsupported_tld = True

        return Domain(
            data=data,
            pc=self.pc,
            whoisStr=whoisStr,
        )

    def _verifyPrivateRegistry(
        self,
    ) -> bool:
        # may raise WhoisPrivateRegistry
        # signal we know the tld but it has no whos or does not respond with any information
        if self.thisTld.get("_privateRegistry"):
            if self.pc.simplistic is False:
                msg = "WhoisPrivateRegistry"
                raise WhoisPrivateRegistry(msg)
            return True
        return False

    def _doServerHintsForThisTld(
        self,
    ) -> None:
        # note _server hints currently are not passes down when using "extend", that may have been my error during the initial implementation
        # allow server hints using "_server" from the tld_regexpr.py file
        thisTldServer = self.thisTld.get("_server")
        if self.pc.server is None and thisTldServer:
            self.pc.server = thisTldServer

    def _doSlowdownHintForThisTld(
        self,
    ) -> int:
        self.pc.slow_down = self.pc.slow_down or 0

        slowDown = self.thisTld.get("_slowdown")
        if slowDown:
            if self.pc.slow_down == 0 and int(slowDown) > 0:
                self.pc.slow_down = int(slowDown)

        if self.pc.verbose and int(self.pc.slow_down):
            print(f"using _slowdown hint {self.pc.slow_down} for tld: {self.tldString}", file=sys.stderr)

        return int(self.pc.slow_down)

    def doOneLookup(
        self,
        dList: List[str],
    ) -> Optional[Domain]:

        try:
            whoisStr = doWhoisAndReturnString(
                dList=dList,
                pc=self.pc,
            )
        except Exception as e:
            if self.pc.simplistic:
                return Domain(
                    data={},
                    pc=self.pc,
                    whoisStr=None,
                    exeptionStr=f"{e}",
                )

            raise e

        updateLastWhois(
            dList=dList,
            whoisStr=whoisStr,
            pc=self.pc,
        )

        if self.pc.verbose:
            # is not cleaned
            print(whoisStr, file=sys.stderr)

        data, whoisStr = do_parse(
            whoisStr=whoisStr,
            tldString=str(self.tldString),
            dList=dList,
            pc=self.pc,
        )

        if self.pc.verbose:
            # should be cleaned now
            print(whoisStr, file=sys.stderr)

        if isinstance(data, Domain):
            return data

        # do we have a result and does it have a domain name
        if data and data["domain_name"][0]:
            return Domain(
                data=data,
                pc=self.pc,
                whoisStr=whoisStr,
            )
        return None

    def processRequest(self) -> Optional[Domain]:
        # =================================================
        try:
            dList = self._fromDomainStringToTld()  # may raise UnknownTld
            if self.tldString is None:
                return None
        except Exception as e:
            if self.pc.simplistic:
                return Domain(
                    data={},
                    pc=self.pc,
                    whoisStr=None,
                    exeptionStr="UnknownTld",
                )
            else:
                raise (e)

        # =================================================
        dList = cast(List[str], dList)
        if self.tldString not in TLD_RE.keys():
            msg = self.makeMessageForUnsupportedTld()
            if msg is None:
                return self._doUnsupportedTldAnyway(
                    dList=dList,
                )

            if self.pc.simplistic:
                return Domain(
                    data={},
                    pc=self.pc,
                    whoisStr=None,
                    exeptionStr="UnknownTld",
                )

            raise UnknownTld(msg)

        # =================================================
        self.setThisTldEntry(cast(Dict[str, Any], TLD_RE.get(self.tldString)))

        if self._verifyPrivateRegistry():  # may raise WhoisPrivateRegistry
            msg = "This tld has either no whois server or responds only with minimal information"
            return Domain(
                data={},
                pc=self.pc,
                whoisStr=None,
                exeptionStr=msg,
            )

        # =================================================
        self._doServerHintsForThisTld()
        self._doSlowdownHintForThisTld()

        # if the tld is a multi level we should not move further down than the tld itself
        # we currently allow progressive lookups until we find something:
        # so xxx.yyy.zzz will try both xxx.yyy.zzz and yyy.zzz
        # but if the tld is yyy.zzz we should only try xxx.yyy.zzz

        tldLevel = self.tldString.split(".")
        while True:  # loop until we decide we are done
            result = self.doOneLookup(
                dList=dList,
            )
            if result:
                return result

            if len(dList) > (len(tldLevel) + 1):
                dList = dList[1:]  # strip one element from the front and try again
                if self.pc.verbose:
                    print(f"try again with {dList}, {len(dList)}, {len(tldLevel) + 1}", file=sys.stderr)
                continue

            # no result or no domain but we can not reduce any further so we have None
            return None

        return None
