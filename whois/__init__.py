"""
    Python module/library for retrieving WHOIS information of domains.

    By DDarko.org  ddarko@ddarko.org  http://ddarko.org/
    License MIT  http://www.opensource.org/licenses/mit-license.php

    Usage example
    >>> import whois
    >>> domain = whois.query('google.com')
    >>> print(domain.__dict__)

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
import sys
from ._1_query import do_query
from ._2_parse import do_parse, TLD_RE
from ._3_adjust import Domain
from .exceptions import UnknownTld, FailedParsingWhoisOutput, UnknownDateFormat, WhoisCommandFailed

from typing import Optional, List


CACHE_FILE = None
SLOW_DOWN = 0

Map2underscore = {
    ".ac.uk": "ac_uk",
    ".co.il": "co_il",
    ".co.jp": "co_jp",
    ".ne.jp": "ne_jp",
    ".or.jp": "or_jp",
    ".go.jp": "go_jp",
    ".ac.jp": "ac_jp",
    ".ad.jp": "ad_jp",
    ".ed.jp": "ed_jp",
    ".gr.jp": "gr_jp",
    ".lg.jp": "lg_jp",
    ".geo.jp": "geo_jp",
    ".com.au": "com_au",
    ".co.th": "co_th",
    ".com.tr": "com_tr",
    ".com.sg": "com_sg",
}

PythonKeyWordMap = {
    "global": "global_",
    ".id": "id_",
    ".in": "in_",
    ".is": "is_",
}

Utf8Map = {
    ".xn--p1ai": "ru_rf",
}


def validTlds():
    # we should map back to valid tld without underscore
    # but remove the starting . from the real domain
    rmap = {}
    for i in Map2underscore:
        rmap[Map2underscore[i]] = i.lstrip(".")
    for i in PythonKeyWordMap:
        rmap[PythonKeyWordMap[i]] = i.lstrip(".")
    for i in Utf8Map:
        rmap[Utf8Map[i]] = i.lstrip(".")

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
    # also known as "dont overstay your welcome"

    tld = None

    if len(d) > 2:
        for i in Map2underscore:
            if domain.endswith(i):
                tld = Map2underscore[i]
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


def query(
    domain: str,
    force: bool = False,
    cache_file: Optional[str] = None,
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
    verbose: bool = False,
) -> Optional[Domain]:
    """
    force=True          Don't use cache.
    cache_file=<path>   Use file to store cache not only memory.
    slow_down=0         Time [s] it will wait after you query WHOIS database.
                        This is useful when there is a limit to the number of requests at a time.
    server:             if set use the whois server explicitly for making the query:
                        propagates on linux to "whois -h <server> <domain>"
                        propagates on Windows to whois.exe <domain> <server>
    """
    assert isinstance(domain, str), Exception("`domain` - must be <str>")

    cache_file = cache_file or CACHE_FILE
    slow_down = slow_down or SLOW_DOWN

    domain = domain.lower().strip().rstrip(".")  # Remove the trailing dot to support FQDN.
    d = domain.split(".")

    if d[0] == "www":
        d = d[1:]

    if len(d) == 1:
        return None

    """
    #  google.com.vn currently not vn nor com.vn is supported
    tld = None
    if len(d) > 2:
        if domain.endswith(".ac.uk"):
            tld = "ac_uk"
        elif domain.endswith("co.il"):
            tld = "co_il"
        elif domain.endswith(".co.jp"):
            tld = "co_jp"
        elif domain.endswith(".ne.jp"):
            tld = "ne_jp"
        elif domain.endswith(".or.jp"):
            tld = "or_jp"
        elif domain.endswith(".go.jp"):
            tld = "go_jp"
        elif domain.endswith(".ac.jp"):
            tld = "ac_jp"
        elif domain.endswith(".ad.jp"):
            tld = "ad_jp"
        elif domain.endswith(".ed.jp"):
            tld = "ed_jp"
        elif domain.endswith(".gr.jp"):
            tld = "gr_jp"
        elif domain.endswith(".lg.jp"):
            tld = "lg_jp"
        elif domain.endswith(".geo.jp"):
            tld = "geo_jp"
        elif domain.endswith(".com.au"):
            tld = "com_au"
        elif domain.endswith("co.th"):
            tld = "co_th"
        elif domain.endswith("com.tr"):
            tld = "com_tr"
        elif domain.endswith("com.sg"):
            tld = "com_sg"

    if tld is None:
        if domain.endswith("global"):
            tld = "global_"
        elif domain.endswith(".id"):
            tld = "id_"
        elif domain.endswith(".in"):
            tld = "in_"
        elif domain.endswith(".is"):
            tld = "is_"
        elif domain.endswith(".name"):
            d[0] = "domain=" + d[0]
            tld = d[-1]
        elif domain.endswith(".xn--p1ai"):
            tld = "ru_rf"

    if tld is None:
        # just take the last item as the top level
        tld = d[-1]
    """

    tld = filterTldToSupportedPattern(domain, d, verbose)

    if tld not in TLD_RE.keys():
        a = f"The TLD {tld} is currently not supported by this package."
        b = "Use validTlds() to see what toplevel domains are supported."
        msg = f"{a} {b}"
        raise UnknownTld(msg)

    # allow server hints using "_server" from the tld_regexpr.py file
    thisTld = TLD_RE.get(tld)
    thisTldServer = thisTld.get("_server")
    if server is None and thisTldServer:
        server = thisTldServer
        if verbose:
            print(f"using _server hint {server} for tld: {tld}", file=sys.stderr)

    while 1:
        q = do_query(
            dl=d,
            force=force,
            cache_file=cache_file,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
        )

        pd = do_parse(
            whois_str=q,
            tld=tld,
            verbose=verbose,
        )

        if (not pd or not pd["domain_name"][0]) and len(d) > 2:
            d = d[1:]
        else:
            break

    if pd and pd["domain_name"][0]:
        return Domain(
            pd,
            verbose=verbose,
        )

    return None
