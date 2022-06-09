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

from typing import Optional


CACHE_FILE = None
SLOW_DOWN = 0


def validTlds():
    return sorted(
        list(
            TLD_RE.keys(),
        ),
    )


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

    if domain.endswith(".ac.uk") and len(d) > 2:
        tld = "ac_uk"
    elif domain.endswith("co.il") and len(d) > 2:
        tld = "co_il"
    elif domain.endswith(".co.jp") and len(d) > 2:
        tld = "co_jp"
    elif domain.endswith(".ne.jp") and len(d) > 2:
        tld = "ne_jp"
    elif domain.endswith(".or.jp") and len(d) > 2:
        tld = "or_jp"
    elif domain.endswith(".go.jp") and len(d) > 2:
        tld = "go_jp"
    elif domain.endswith(".ac.jp") and len(d) > 2:
        tld = "ac_jp"
    elif domain.endswith(".ad.jp") and len(d) > 2:
        tld = "ad_jp"
    elif domain.endswith(".ed.jp") and len(d) > 2:
        tld = "ed_jp"
    elif domain.endswith(".gr.jp") and len(d) > 2:
        tld = "gr_jp"
    elif domain.endswith(".lg.jp") and len(d) > 2:
        tld = "lg_jp"
    elif domain.endswith(".geo.jp") and len(d) > 2:
        tld = "geo_jp"
    elif domain.endswith(".com.au") and len(d) > 2:
        tld = "com_au"
    elif domain.endswith("co.th") and len(d) > 2:
        tld = "co_th"
    elif domain.endswith("com.tr") and len(d) > 2:
        tld = "com_tr"
    elif domain.endswith("com.sg") and len(d) > 2:
        tld = "com_sg"
    elif domain.endswith("global"):
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
    else:
        tld = d[-1]

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
        return Domain(pd)

    return None
