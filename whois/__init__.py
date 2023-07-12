import sys
import os
from functools import wraps
from typing import (
    cast,
    Optional,
    List,
    Dict,
    Tuple,
    Any,
    Callable,
)

from ._1_query import (
    do_query,
)

from ._2_parse import (
    do_parse,
    NoneStrings,
    NoneStringsAdd,
    QuotaStrings,
    QuotaStringsAdd,
    cleanupWhoisResponse,
)

from ._3_adjust import (
    Domain,
)

from .tld_regexpr import (
    ZZ,
)

from ._0_init_tld import (
    TLD_RE,
    validTlds,
    filterTldToSupportedPattern,
    mergeExternalDictWithRegex,
)

from .exceptions import (
    UnknownTld,
    FailedParsingWhoisOutput,
    UnknownDateFormat,
    WhoisCommandFailed,
    WhoisPrivateRegistry,
    WhoisQuotaExceeded,
    WhoisCommandTimeout,
)

from .version import (
    VERSION,
)

__all__ = [
    # from exceptions
    "UnknownTld",
    "FailedParsingWhoisOutput",
    "UnknownDateFormat",
    "WhoisCommandFailed",
    "WhoisPrivateRegistry",
    "WhoisQuotaExceeded",
    "WhoisCommandTimeout",
    # from init_tld
    "validTlds",
    "TLD_RE",
    # from version
    "VERSION",
    # from this file
    "get_last_raw_whois_data",
    "getVersion",
    "query",
    # from parse
    "NoneStrings",
    "NoneStringsAdd",
    "QuotaStrings",
    "QuotaStringsAdd",
    "cleanupWhoisResponse",
]

WHOISDOMAIN: str = ""
if os.getenv("WHOISDOMAIN"):
    WHOISDOMAIN = str(os.getenv("WHOISDOMAIN"))

WD = WHOISDOMAIN.upper().split(":")

SIMPLISTIC = False
if "SIMPISTIC" in WD:
    SIMPLISTIC = True

CACHE_FILE = None
SLOW_DOWN = 0

LastWhois: Dict[str, Any] = {
    "Try": [],
}


# PRIVATE


def _internationalizedDomainNameToPunyCode(d: List[str]) -> List[str]:
    return [k.encode("idna").decode() or k for k in d]


def _result2dict(func: Any) -> Any:
    @wraps(func)
    def _inner(*args: str, **kw: Any) -> Dict[str, Any]:
        r = func(*args, **kw)
        return r and vars(r) or {}

    return _inner


def _fromDomainStringToTld(
    domain: str,
    internationalized: bool,
    verbose: bool = False,
    simplistic: bool = False,
) -> Tuple[Optional[str], Optional[List[str]]]:
    domain = domain.lower().strip().rstrip(".")  # Remove the trailing dot to support FQDN.
    d: List[str] = domain.split(".")
    if verbose:
        print(d, file=sys.stderr)

    if d[0] == "www":
        d = d[1:]

    if len(d) == 1:
        return None, None

    tld: str = filterTldToSupportedPattern(domain, d, verbose)  # may raise UnknownTld
    if verbose:
        print(f"filterTldToSupportedPattern returns tld: {tld}", file=sys.stderr)

    if internationalized and isinstance(internationalized, bool):
        d = _internationalizedDomainNameToPunyCode(d)

    if verbose:
        print(tld, d, file=sys.stderr)

    return tld, d


def _validateWeKnowTheToplevelDomain(
    tld: str,
    return_raw_text_for_unsupported_tld: bool = False,
) -> Optional[str]:
    # may raise UnknownTld
    if return_raw_text_for_unsupported_tld:
        # we dont raise we return None so we can handle unsupported domains anyway
        return None

    a = f"The TLD {tld} is currently not supported by this package."
    b = "Use validTlds() to see what toplevel domains are supported."
    msg = f"{a} {b}"
    return msg


def _verifyPrivateRegistry(
    thisTld: Dict[str, Any],
    simplistic: bool = False,
) -> bool:
    # may raise WhoisPrivateRegistry
    # signal we know the tld but it has no whos or does not respond with any information
    if thisTld.get("_privateRegistry"):
        if simplistic is False:
            msg = "WhoisPrivateRegistry"
            raise WhoisPrivateRegistry(msg)
        return True
    return False


def _doServerHintsForThisTld(
    tld: str,
    thisTld: Dict[str, Any],
    server: Optional[str],
    verbose: bool = False,
) -> Optional[str]:
    # allow server hints using "_server" from the tld_regexpr.py file
    thisTldServer = thisTld.get("_server")
    if server is None and thisTldServer:
        server = thisTldServer
        if verbose:
            print(f"using _server hint {server} for tld: {tld}", file=sys.stderr)
    return server


def _doSlowdownHintForThisTld(
    tld: str,
    thisTld: Dict[str, Any],
    slow_down: int,
    verbose: bool = False,
) -> int:
    # allow a configrable slowdown for some tld's
    slowDown = thisTld.get("_slowdown")
    if slow_down == 0 and slowDown and slowDown > 0:
        slow_down = slowDown
        if verbose:
            print(f"using _slowdown hint {slowDown} for tld: {tld}", file=sys.stderr)
    return slow_down


def _doUnsupportedTldAnyway(
    tld: str,
    dl: List[str],
    ignore_returncode: bool = False,
    slow_down: int = 0,
    server: Optional[str] = None,
    verbose: bool = False,
    wh: str = "whois",
    simplistic: bool = False,
) -> Optional[Domain]:
    include_raw_whois_text = True

    # we will not hunt for possible valid first level domains as we have no actual feedback

    whois_str = do_query(
        dl=dl,
        slow_down=slow_down,
        ignore_returncode=ignore_returncode,
        server=server,
        verbose=verbose,
        wh=wh,
        simplistic=simplistic,
    )

    # we will only return minimal data
    data = {
        "tld": tld,
        "domain_name": [],
    }
    data["domain_name"] = [".".join(dl)]  # note the fields are default all array, except tld

    if verbose:
        print(data, file=sys.stderr)

    return Domain(
        data=data,
        whois_str=whois_str,
        verbose=verbose,
        include_raw_whois_text=include_raw_whois_text,
        return_raw_text_for_unsupported_tld=True,
    )


def _doOneLookup(
    tld: str,
    dl: List[str],
    force: bool = False,
    cache_file: Optional[str] = None,
    cache_age: int = 60 * 60 * 48,
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    include_raw_whois_text: bool = False,
    timeout: Optional[float] = None,
    wh: str = "whois",
    simplistic: bool = False,
    withRedacted: bool = False,
) -> Optional[Domain]:

    try:
        whois_str = do_query(
            dl=dl,
            force=force,
            cache_file=cache_file,
            cache_age=cache_age,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
            timeout=timeout,
            wh=wh,
            simplistic=simplistic,
        )
    except Exception as e:
        if simplistic:
            return Domain(
                data={},
                whois_str=None,
                verbose=verbose,
                include_raw_whois_text=include_raw_whois_text,
                exeptionStr=f"{e}",
            )

        raise e

    LastWhois["Try"].append(
        {
            "Domain": ".".join(dl),
            "rawData": whois_str,
            "server": server,
        }
    )

    data = do_parse(
        whois_str=whois_str,
        tld=tld,
        dl=dl,
        verbose=verbose,
        with_cleanup_results=with_cleanup_results,
        simplistic=simplistic,
        include_raw_whois_text=include_raw_whois_text,
        withRedacted=withRedacted,
    )

    if isinstance(data, Domain):
        return data

    # do we have a result and does it have a domain name
    if data and data["domain_name"][0]:
        return Domain(
            data=data,
            whois_str=whois_str,
            verbose=verbose,
            include_raw_whois_text=include_raw_whois_text,
        )
    return None


# PUBLIC


def get_last_raw_whois_data() -> Dict[str, Any]:
    global LastWhois
    return LastWhois


def query(
    domain: str,
    force: bool = False,
    cache_file: Optional[str] = None,
    cache_age: int = 60 * 60 * 48,
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    internationalized: bool = False,
    include_raw_whois_text: bool = False,
    return_raw_text_for_unsupported_tld: bool = False,
    timeout: Optional[float] = None,
    cmd: str = "whois",
    simplistic: bool = False,
    withRedacted: bool = False,
) -> Optional[Domain]:
    """
    force=True          Don't use cache.
    cache_file=<path>   Use file to store cache not only memory.
    cache_age=172800    Cache expiration time for given domain, in seconds
    slow_down=0         Time [s] it will wait after you query WHOIS database.
                        This is useful when there is a limit to the number of requests at a time.
    server:             if set use the whois server explicitly for making the query:
                        propagates on linux to "whois -h <server> <domain>"
                        propagates on Windows to whois.exe <domain> <server>
    with_cleanup_results: cleanup lines starting with % and REDACTED FOR PRIVACY
    internationalized:  if true convert with internationalizedDomainNameToPunyCode().
    ignore_returncode:  if true and the whois command fails with code 1, still process the data returned as normal.
    verbose:            if true, print relevant information on steps taken to standard error
    include_raw_whois_text:
                        if reqested the full response is also returned.
    return_raw_text_for_unsupported_tld:
                        if the tld is unsupported, just try it anyway but return only the raw text.
    timeout:            timeout in seconds for the whois command to return a result.
    cmd:                explicitly specify the path to the whois you want to use.
    simplistic:         when simplistic is True we return None for most exceptions and dont pass info why we have no data.
    withRedacted:       show redacted output , default no redacted data is shown
    """

    global LastWhois
    LastWhois["Try"] = []  # init on start of query

    wh: str = cmd  # make it compatible with python-whois-extended

    assert isinstance(domain, str), Exception("`domain` - must be <str>")
    return_raw_text_for_unsupported_tld = bool(return_raw_text_for_unsupported_tld)

    try:
        tld, dl = _fromDomainStringToTld(  # may raise UnknownTld
            domain,
            internationalized,
            verbose,
        )

        if tld is None:
            return None
    except Exception as e:
        if simplistic:
            return Domain(
                data={},
                whois_str=None,
                verbose=verbose,
                include_raw_whois_text=include_raw_whois_text,
                exeptionStr="UnknownTld",
            )

        raise (e)

    dl = cast(List[str], dl)
    if tld not in TLD_RE.keys():
        msg = _validateWeKnowTheToplevelDomain(tld, return_raw_text_for_unsupported_tld)

        if msg is None:
            return _doUnsupportedTldAnyway(
                tld,
                dl,
                ignore_returncode=ignore_returncode,
                slow_down=slow_down,
                server=server,
                verbose=verbose,
                wh=wh,
                simplistic=simplistic,
            )
        if simplistic:
            return Domain(
                data={},
                whois_str=None,
                verbose=verbose,
                include_raw_whois_text=include_raw_whois_text,
                exeptionStr="UnknownTld",
            )

        raise UnknownTld(msg)

    thisTld = cast(Dict[str, Any], TLD_RE.get(tld))

    if _verifyPrivateRegistry(thisTld, simplistic):  # may raise WhoisPrivateRegistry
        msg = "This tld has either no whois server or responds only with minimal information"
        return Domain(
            data={},
            whois_str=None,
            verbose=verbose,
            include_raw_whois_text=include_raw_whois_text,
            exeptionStr=msg,
        )

    server = _doServerHintsForThisTld(tld, thisTld, server, verbose)

    slow_down = slow_down or SLOW_DOWN
    slow_down = _doSlowdownHintForThisTld(tld, thisTld, slow_down, verbose)

    # if the tld is a multi level we should not move further down than the tld itself
    # we currently allow progressive lookups until we find something:
    # so xxx.yyy.zzz will try both xxx.yyy.zzz and yyy.zzz
    # but if the tld is yyy.zzz we should only try xxx.yyy.zzz

    cache_file = cache_file or CACHE_FILE
    tldLevel = tld.split(".")
    while 1:
        result = _doOneLookup(
            tld=tld,
            dl=dl,
            force=force,
            cache_file=cache_file,
            cache_age=cache_age,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
            with_cleanup_results=with_cleanup_results,
            include_raw_whois_text=include_raw_whois_text,
            timeout=timeout,
            wh=wh,
            simplistic=simplistic,
            withRedacted=withRedacted,
        )
        if result:
            return result

        if len(dl) > (len(tldLevel) + 1):
            dl = dl[1:]  # strip one element from the front and try again
            if verbose:
                print(f"try again with {dl}, {len(dl)}, {len(tldLevel) + 1}", file=sys.stderr)
            continue

        # no result or no domain but we can not reduce any further so we have None
        return None

    return None


# Add get function to support return result in dictionary form
get = _result2dict(query)


def getVersion() -> str:
    return VERSION
