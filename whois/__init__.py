import sys
from functools import wraps
from typing import (
    Optional,
    List,
    Dict,
)

from ._1_query import do_query
from ._2_parse import do_parse
from ._3_adjust import Domain
from ._0_init_tld import (
    ZZ,
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
)

"""
    Python module/library for retrieving WHOIS information of domains.

    By DDarko.org  ddarko@ddarko.org  http://ddarko.org/
    License MIT  http://www.opensource.org/licenses/mit-license.php

    Usage example
    >>> import whois
    >>> domain = whois.query('google.com')
    >>> print(domain.__dict__)  # print(whois.get('google.com'))

    {
        'expiration_date':  datetime.datetime(2020, 9, 14, 0, 0),
        'last_updated':     datetime.datetime(2011, 7, 20, 0, 0),
        'registrar':        'MARKMONITOR INC.',
        'name':             'google.com',
        'creation_date':    datetime.datetime(1997, 9, 15, 0, 0)
    }

    >>> print(domain.name)
    google.com

    >>> print(domain.expiration_date)
    2020-09-14 00:00:00

"""
__all__ = [
    "query",
    "get",
    "validTlds",
    "mergeExternalDictWithRegex",
]


CACHE_FILE = None
SLOW_DOWN = 0


def internationalizedDomainNameToPunyCode(d: List[str]) -> List[str]:
    return [k.encode("idna").decode() or k for k in d]


def result2dict(func):
    @wraps(func)
    def _inner(*args, **kw):
        r = func(*args, **kw)
        return r and vars(r) or {}

    return _inner


def fromDomainStringToTld(
    domain: str,
    internationalized: bool,
    verbose: bool = False,
):
    domain = domain.lower().strip().rstrip(".")  # Remove the trailing dot to support FQDN.
    d = domain.split(".")
    if verbose:
        print(d, file=sys.stderr)

    if d[0] == "www":
        d = d[1:]

    if len(d) == 1:
        return None, None

    tld = filterTldToSupportedPattern(domain, d, verbose)
    if verbose:
        print(f"filterTldToSupportedPattern returns tld: {tld}", file=sys.stderr)

    if internationalized and isinstance(internationalized, bool):
        d = internationalizedDomainNameToPunyCode(d)

    if verbose:
        print(tld, d, file=sys.stderr)

    return tld, d


def validateWeKnowTheToplevelDomain(tld, return_raw_text_for_unsupported_tld: bool = False):  # may raise UnknownTld
    if tld not in TLD_RE.keys():
        if return_raw_text_for_unsupported_tld:
            return None
        a = f"The TLD {tld} is currently not supported by this package."
        b = "Use validTlds() to see what toplevel domains are supported."
        msg = f"{a} {b}"
        raise UnknownTld(msg)
    return TLD_RE.get(tld)


def verifyPrivateREgistry(thisTld: Dict):  # may raise WhoisPrivateRegistry
    # signal we know the tld but it has no whos or does not respond with any information
    if thisTld.get("_privateRegistry"):
        msg = "This tld has either no whois server or responds only with minimal information"
        raise WhoisPrivateRegistry(msg)


def doServerHintsForThisTld(tld: str, thisTld: Dict, server: Optional[str], verbose: bool = False):
    # allow server hints using "_server" from the tld_regexpr.py file
    thisTldServer = thisTld.get("_server")
    if server is None and thisTldServer:
        server = thisTldServer
        if verbose:
            print(f"using _server hint {server} for tld: {tld}", file=sys.stderr)
    return server


def doSlowdownHintForThisTld(tld: str, thisTld, slow_down: int, verbose: bool = False) -> int:
    # allow a configrable slowdown for some tld's
    slowDown = thisTld.get("_slowdown")
    if slow_down == 0 and slowDown and slowDown > 0:
        slow_down = slowDown
        if verbose:
            print(f"using _slowdown hint {slowDown} for tld: {tld}", file=sys.stderr)
    return slow_down


def doUnsupportedTldAnyway(
    tld: str,
    dl: Dict,
    ignore_returncode: bool = False,
    slow_down: int = 0,
    server: Optional[str] = None,
    verbose: bool = False,
):
    include_raw_whois_text = True

    # we will not hunt for possible valid first level domains as we have no actual feedback

    whois_str = do_query(
        dl=dl,
        slow_down=slow_down,
        ignore_returncode=ignore_returncode,
        server=server,
        verbose=verbose,
    )

    # we will only return minimal data
    data = {
        "tld": tld,
        "domain_name": "",
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


LastWhois: Dict = {
    "Try": [],
}

def get_last_raw_whois_data():
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
    with_cleanup_results=False,
    internationalized: bool = False,
    include_raw_whois_text: bool = False,
    return_raw_text_for_unsupported_tld: bool = False,
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
    """
    global LastWhois
    LastWhois["Try"] = [] # init on start of query

    assert isinstance(domain, str), Exception("`domain` - must be <str>")
    return_raw_text_for_unsupported_tld = bool(return_raw_text_for_unsupported_tld)

    tld, dl = fromDomainStringToTld(domain, internationalized, verbose)
    if tld is None:
        return None

    thisTld = validateWeKnowTheToplevelDomain(tld, return_raw_text_for_unsupported_tld)  # may raise UnknownTld
    if thisTld is None:
        return doUnsupportedTldAnyway(
            tld,
            dl,
            ignore_returncode=ignore_returncode,
            slow_down=slow_down,
            server=server,
            verbose=verbose,
        )

    verifyPrivateREgistry(thisTld)  # may raise WhoisPrivateRegistry
    server = doServerHintsForThisTld(tld, thisTld, server, verbose)

    slow_down = slow_down or SLOW_DOWN
    slow_down = doSlowdownHintForThisTld(tld, thisTld, slow_down, verbose)

    # if the tld is a multi level we should not move further down than the tld itself
    # we currently allow progressive lookups until we find something:
    # so xxx.yyy.zzz will try both xxx.yyy.zzz and yyy.zzz
    # but if the tld is yyy.zzz we should only try xxx.yyy.zzz

    cache_file = cache_file or CACHE_FILE
    tldLevel = tld.split(".")  # note while the top level domain may have a . the tld has a _ ( co.uk becomes co_uk )
    while 1:
        whois_str = do_query(
            dl=dl,
            force=force,
            cache_file=cache_file,
            cache_age=cache_age,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
        )
        tryMe = {
            "Domain": ".".join(dl),
            "rawData": whois_str,
            "server": server,
        }
        LastWhois["Try"].append(tryMe)

        data = do_parse(
            whois_str=whois_str,
            tld=tld,
            dl=dl,
            verbose=verbose,
            with_cleanup_results=with_cleanup_results,
        )

        # do we have a result and does it have a domain name
        if data and data["domain_name"][0]:
            return Domain(
                data=data,
                whois_str=whois_str,
                verbose=verbose,
                include_raw_whois_text=include_raw_whois_text,
            )

        if len(dl) > (len(tldLevel) + 1):
            dl = dl[1:]  # strip one element from the front and try again
            if verbose:
                print(f"try again with {dl}, {len(dl)}, {len(tldLevel) + 1}", file=sys.stderr)
            continue

        # no result or no domain but we can not reduce any further so we have None
        return None

    return None


# Add get function to support return result in dictionary form
get = result2dict(query)
