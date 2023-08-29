#! /usr/bin/env python3

from typing import (
    Any,
    Dict,
    Optional,
    # Tuple,
    List,
    Union,
    # cast,
)

import re
import sys

from .exceptions import (
    FailedParsingWhoisOutput,
    WhoisQuotaExceeded,
)

from ._0_init_tld import TLD_RE
from .domain import Domain

from .strings.noneStrings import NoneStrings
from .strings.quotaStrings import QuotaStrings
from .context.parameterContext import ParameterContext
from .context.dataContext import DataContext


class WhoisParser:
    def __init__(
        self,
        tldString: str,
        pc: ParameterContext,
        dc: DataContext,
    ) -> None:
        self.tldString = tldString
        self.pc = pc
        self.dc = dc
        self.dc.whoisStr = str(self.dc.whoisStr)
        #
        self.resultDict: Dict[str, Any] = {
            "tld": tldString,
            "DNSSEC": self._doDnsSec(),
        }
        self.cleanupWhoisResponse()

    def _doExtractPattensIanaFromWhoisString(
        self,
    ) -> None:
        # now handle the actual format if this whois response
        iana = {
            "domain_name": r"domain:\s?([^\n]+)",
            "registrar": r"organisation:\s?([^\n]+)",
            "creation_date": r"created:\s?([^\n]+)",
        }

        for k, v in iana.items():
            zz = re.findall(v, str(self.dc.whoisStr))
            if zz:
                if self.pc.verbose:
                    print(f"parsing iana data only for tld: {self.tldString}, {zz}", file=sys.stderr)
                self.resultDict[k] = zz

    def _doExtractPattensFromWhoisString(
        self,
    ) -> None:
        # here we apply the regex patterns
        # use TLD_RE["com"] as default if a regex is missing
        for k, v in TLD_RE.get(self.tldString, TLD_RE["com"]).items():
            if k.startswith("_"):
                # skip meta element like: _server or _privateRegistry
                continue

            # Historical: here we use 'empty string' as default, not None
            if v is None:
                self.resultDict[k] = [""]
            else:
                self.resultDict[k] = v.findall(self.dc.whoisStr) or [""]

    def _doSourceIana(
        self,
    ) -> Optional[Dict[str, Any]]:
        self.dc.whoisStr = str(self.dc.whoisStr)

        # here we can handle the example.com and example.net permanent IANA domains
        k: str = "source:       IANA"

        if self.pc.verbose:
            msg: str = f"i have seen {k}"
            print(msg, file=sys.stderr)

        whois_splitted: List[str] = self.dc.whoisStr.split(k)
        z: int = len(whois_splitted)
        if z > 2:

            self.dc.whoisStr = k.join(whois_splitted[1:])
            return None

        if z == 2 and whois_splitted[1].strip() != "":
            # if we see source: IANA and the part after is not only whitespace
            if self.pc.verbose:
                msg = f"after: {k} we see not only whitespace: {whois_splitted[1]}"
                print(msg, file=sys.stderr)

            self.dc.whoisStr = whois_splitted[1]
            return None

        self._doExtractPattensFromWhoisString()  # try to parse this as a IANA domain as after is only whitespace
        self._doExtractPattensIanaFromWhoisString()  # now handle the actual format if this whois response

        return self.resultDict

    def _doIfServerNameLookForDomainName(self) -> None:
        if self.dc.whoisStr is None:
            return

        # not often available anymore
        if not re.findall(r"Server Name:\s?(.+)", self.dc.whoisStr, re.IGNORECASE):
            return

        if self.pc.verbose:
            msg = "i have seen Server Name:, looking for Domain Name:"
            print(msg, file=sys.stderr)

        # this changes the whoisStr, we may want to keep the original as extra
        self.dc.whoisStr = self.dc.whoisStr[self.dc.whoisStr.find("Domain Name:") :]

    def _doDnsSec(
        self,
    ) -> bool:
        if self.dc.whoisStr is None:
            return False

        whoisDnsSecList: List[str] = self.dc.whoisStr.split("DNSSEC:")
        if len(whoisDnsSecList) >= 2:
            if self.pc.verbose:
                msg = "i have seen dnssec: {whoisDnsSecStr}"
                print(msg, file=sys.stderr)

            whoisDnsSecStr: str = whoisDnsSecList[1].split("\n")[0]
            if whoisDnsSecStr.strip() == "signedDelegation" or whoisDnsSecStr.strip() == "yes":
                return True

        return False

    def _handleShortResponse(
        self,
    ) -> Optional[Domain]:
        if self.dc.whoisStr is None:
            return None

        if self.pc.verbose:
            print(f"shortResponse:: {self.tldString} {self.dc.whoisStr}", file=sys.stderr)

        # TODO: some short responses are actually valid:
        # lookfor Domain: and Status but all other fields are missing so the regexec could fail
        # this domain is taken already or reserved

        # whois syswow.64-b.it
        # [Querying whois.nic.it]
        # [whois.nic.it]
        # Domain:             syswow.64-b.it
        # Status:             UNASSIGNABLE

        # ---------------------------------
        # NOTE: from here s is lowercase only
        s = self.dc.whoisStr.strip().lower()
        noneStrings = NoneStrings()
        for i in noneStrings:
            if i in s:
                return None

        # ---------------------------------
        # is there any error string in the result
        if s.count("error"):
            if self.pc.verbose:
                print("i see 'error' in the result, return: None", file=sys.stderr)
            return None

        # ---------------------------------
        quotaStrings = QuotaStrings()
        for i in quotaStrings:
            if i in s:
                if self.pc.simplistic:
                    msg = "WhoisQuotaExceeded"
                    self.dc.exeptionStr = msg

                    return Domain(
                        pc=self.pc,
                        dc=self.dc,
                    )
                raise WhoisQuotaExceeded(self.dc.whoisStr)

        if self.pc.simplistic:
            msg = "FailedParsingWhoisOutput"
            self.dc.exeptionStr = msg

            return Domain(
                pc=self.pc,
                dc=self.dc,
            )

        raise FailedParsingWhoisOutput(self.dc.whoisStr)

    def cleanupWhoisResponse(
        self,
    ) -> str:
        tmp2: List[str] = []
        self.dc.whoisStr = str(self.dc.whoisStr)

        tmp: List[str] = self.dc.whoisStr.split("\n")
        for line in tmp:
            # some servers respond with: % Quota exceeded in the comment section (lines starting with %)
            if "quota exceeded" in line.lower():
                raise WhoisQuotaExceeded(self.dc.whoisStr)

            if self.pc.with_cleanup_results is True and line.startswith("%"):  # only remove if requested
                continue

            if self.pc.withRedacted is False:
                if "REDACTED FOR PRIVACY" in line:  # these lines contibute nothing so ignore
                    continue

            if (
                "Please query the RDDS service of the Registrar of Record" in line
            ):  # these lines contibute nothing so ignore
                continue

            if line.startswith("Terms of Use:"):  # these lines contibute nothing so ignore
                continue

            tmp2.append(line.strip("\r"))

        self.dc.whoisStr = "\n".join(tmp2)
        return self.dc.whoisStr

    def parse(
        self,
    ) -> Union[Optional[Dict[str, Any]], Optional[Domain]]:
        # ) -> Tuple[Union[Optional[Dict[str, Any]], Optional[Domain]], str]:
        self.dc.whoisStr = str(self.dc.whoisStr)

        if self.dc.whoisStr.count("\n") < 5:
            result1 = self._handleShortResponse()  # may raise: FailedParsingWhoisOutput, WhoisQuotaExceeded,
            return result1
            #  return result1, self.dc.whoisStr

        if "source:       IANA" in self.dc.whoisStr:
            # historical IANA domains
            result2 = self._doSourceIana()
            if result2 is not None:
                return result2
                # return result2, self.dc.whoisStr

        if "Server Name" in self.dc.whoisStr:
            # old type Server Name (not very common anymore)
            self._doIfServerNameLookForDomainName()

        self._doExtractPattensFromWhoisString()

        # return self.resultDict, self.dc.whoisStr
        return self.resultDict
