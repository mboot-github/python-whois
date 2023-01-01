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
__all__ = ["query", "get"]

import sys
from functools import wraps
from typing import Optional, List, Dict

from ._1_query import do_query
from ._2_parse import do_parse, TLD_RE
from ._3_adjust import Domain
from .exceptions import (
    UnknownTld,
    FailedParsingWhoisOutput,
    UnknownDateFormat,
    WhoisCommandFailed,
    WhoisPrivateRegistry,
    WhoisQuotaExceeded,
)

CACHE_FILE = None
SLOW_DOWN = 0

Map2Underscore = {
    ".co.za": "co_za",  # south africa
    ".web.za": "web_za",  # south africa
    ".org.za": "org_za",  # south africa
    ".net.za": "net_za",  # south africa
    #
    ".com.eg": "com_eg",  # egypt
    ".ac.uk": "ac_uk",
    ".co.uk": "co_uk",
    ".co.il": "co_il",
    # uganda
    ".ca.ug": "ca_ug",
    ".co.ug": "co_ug",
    # th
    ".co.th": "co_th",
    ".in.th": "in_th",
    # .jp
    ".ac.jp": "ac_jp",
    ".ad.jp": "ad_jp",
    ".co.jp": "co_jp",
    ".ed.jp": "ed_jp",
    ".go.jp": "go_jp",
    ".gr.jp": "gr_jp",
    ".lg.jp": "lg_jp",
    ".ne.jp": "ne_jp",
    ".or.jp": "or_jp",
    ".geo.jp": "geo_jp",
    #
    ".com.au": "com_au",
    ".com.sg": "com_sg",
    ".com.do": "com_do",
    ".com.mo": "com_mo",
    # ph
    ".com.ph": "com_ph",
    ".org.ph": "org_ph",
    ".net.ph": "net_ph",
    #
    # TÜRKİYE (formerly Turkey)
    ".com.tr": "com_tr",
    ".edu.tr": "edu_tr",
    ".org.tr": "org_tr",
    ".net.tr": "net_tr",
    #
    ".edu.ua": "edu_ua",
    ".com.ua": "com_ua",
    ".net.ua": "net_ua",
    ".lviv.ua": "lviv_ua",
    # dynamic dns without whois
    ".hopto.org": "hopto_org",
    ".duckdns.org": "duckdns_org",
    ".no-ip.com": "noip_com",
    ".no-ip.org": "noip_org",
    # 2022-06-20: mboot
    ".ac.th": "ac_th",
    ".co.ke": "co_ke",
    ".com.bo": "com_bo",
    ".com.ly": "com_ly",
    ".com.tw": "com_tw",
    ".com.np": "com_np",
    ".go.th": "go_th",
    ".com.ec": "com_ec",
    ".gob.ec": "gob_ec",
    ".co.zw": "com_zw",
    ".org.zw": "org_zw",
    ".com.py": "com_py",
}

PythonKeyWordMap = {
    "global": "global_",
    ".id": "id_",
    ".in": "in_",
    ".is": "is_",
    ".as": "as_",
}

Utf8Map = {
    ".xn--p1ai": "ru_rf",
    ".xn--p1acf": "pyc_",  # .РУС
}


def validTlds():
    # --------------------------------------
    # we should map back to valid tld without underscore
    # but remove the starting . from the real domain
    rmap = {}  # build a reverse dict from the original tld translation maps
    for i in Map2Underscore:
        rmap[Map2Underscore[i]] = i.lstrip(".")

    for i in PythonKeyWordMap:
        rmap[PythonKeyWordMap[i]] = i.lstrip(".")

    for i in Utf8Map:
        rmap[Utf8Map[i]] = i.lstrip(".")

    # --------------------------------------
    tlds = []
    for tld in TLD_RE.keys():
        if tld in rmap:
            tlds.append(rmap[tld])
        else:
            tlds.append(tld)
    return sorted(tlds)


def filterTldToSupportedPattern(
    domain: str,
    d: List[str],
    verbose: bool = False,
) -> str:
    # the moment we have a valid tld we can leave:
    # no need for else or elif anymore
    # that is the "leave early" paradigm
    # also known as "dont overstay your welcome" or "don't linger"

    tld = None

    if len(d) > 2:
        for i in Map2Underscore:
            if domain.endswith(i):
                tld = Map2Underscore[i]
                return tld

    for i in PythonKeyWordMap:
        if domain.endswith(i):
            tld = PythonKeyWordMap[i]
            return tld

    for i in Utf8Map:
        if domain.endswith(i):
            tld = Utf8Map[i]
            return tld

    if domain.endswith(".name"):
        # some special case with xxx.name -> domain=xxx.name and tld is name
        d[0] = "domain=" + d[0]
        tld = d[-1]
        return tld

    # just take the last item as the top level
    return d[-1]


def internationalizedDomainNameToPunyCode(d: List[str]) -> List[str]:
    return [k.encode("idna").decode() or k for k in d]


def result2dict(func):
    @wraps(func)
    def _inner(*args, **kw):
        r = func(*args, **kw)
        return r and vars(r) or {}

    return _inner


def fromDomainStringToTld(domain: str, internationalized: bool, verbose: bool = False):
    domain = domain.lower().strip().rstrip(".")  # Remove the trailing dot to support FQDN.
    d = domain.split(".")
    if verbose:
        print(d, file=sys.stderr)

    if d[0] == "www":
        d = d[1:]

    if len(d) == 1:
        return None, None

    tld = filterTldToSupportedPattern(domain, d, verbose)

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


def query(
    domain: str,
    force: bool = False,
    cache_file: Optional[str] = None,
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
    tldLevel = tld.split("_")  # note while the top level domain may have a . the tld has a _ ( co.uk becomes co_uk )
    while 1:
        whois_str = do_query(
            dl=dl,
            force=force,
            cache_file=cache_file,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
        )

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
