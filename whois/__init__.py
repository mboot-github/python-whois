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


from .version import (
    VERSION,
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

from ._0_init_tld import (
    TLD_RE,
    validTlds,
    filterTldToSupportedPattern,
    mergeExternalDictWithRegex,
)

from .processWhoisDomainRequest import ProcessWhoisDomainRequest
from .lastWhois import (
    get_last_raw_whois_data,
    initLastWhois,
)
from .doWhoisCommand import setMyCache
from .domain import Domain

from .strings.noneStrings import NoneStrings, NoneStringsAdd
from .strings.quotaStrings import QuotaStrings, QuotaStringsAdd
from .tldDb.tld_regexpr import ZZ
from .context.dataContext import DataContext
from .context.parameterContext import ParameterContext
from .cache.simpleCacheBase import SimpleCacheBase
from .cache.simpleCacheWithFile import SimpleCacheWithFile
from .cache.dummyCache import DummyCache
from .cache.dbmCache import DBMCache

HAS_REDIS = False
try:
    import redis

    HAS_REDIS = True
except Exception as e:
    _ = e

if HAS_REDIS:
    from .cache.redisCache import RedisCache

WHOISDOMAIN: str = ""
if os.getenv("WHOISDOMAIN"):
    WHOISDOMAIN = str(os.getenv("WHOISDOMAIN"))

WD = WHOISDOMAIN.upper().split(":")

SIMPLISTIC = False
if "SIMPLISTIC" in WD:
    SIMPLISTIC = True

TLD_LIB_PRESENT: bool = False
try:
    import tld as libTld

    TLD_LIB_PRESENT = True
except Exception as e:
    _ = e  # ignore any error

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
    # from parameterContext
    "ParameterContext",
    # from doQuery
    "query",
    "q2",
    "get_last_raw_whois_data",
    # fromm this file
    "getVersion",
    "getTestHint",
    # from doWhoisCommand
    "setMyCache",  # to build your own caching interface
    # from doParse
    "NoneStrings",
    "NoneStringsAdd",
    "QuotaStrings",
    "QuotaStringsAdd",
    "cleanupWhoisResponse",  # we will drop this most likely
    # from Cache
    "SimpleCacheBase",
    "SimpleCacheWithFile",
    "DummyCache",
    "DBMCache",
    "RedisCache",
]


def _result2dict(func: Any) -> Any:
    @wraps(func)
    def _inner(*args: str, **kw: Any) -> Dict[str, Any]:
        r = func(*args, **kw)
        return r and vars(r) or {}

    return _inner


def q2(
    domain: str,
    pc: ParameterContext,
) -> Optional[Domain]:

    initLastWhois()

    dc = DataContext(
        pc=pc,
        domain=domain,
    )
    pwdr = ProcessWhoisDomainRequest(
        domain=domain,
        pc=pc,
        dc=dc,
    )

    return pwdr.processRequest()


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
    parse_partial_response: bool = False,
    cmd: str = "whois",
    simplistic: bool = False,
    withRedacted: bool = False,
    pc: Optional[ParameterContext] = None,
    # if you use pc as argument all above params (except domain are ignored)
) -> Optional[Domain]:
    # see documentation about paramaters in parameterContext.py

    assert isinstance(domain, str), Exception("`domain` - must be <str>")

    if pc is None:
        pc = ParameterContext(
            force=force,
            cache_file=cache_file,
            cache_age=cache_age,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
            with_cleanup_results=with_cleanup_results,
            internationalized=internationalized,
            include_raw_whois_text=include_raw_whois_text,
            return_raw_text_for_unsupported_tld=return_raw_text_for_unsupported_tld,
            timeout=timeout,
            parse_partial_response=parse_partial_response,
            cmd=cmd,
            simplistic=simplistic,
            withRedacted=withRedacted,
        )

    if verbose:
        print(pc, file=sys.stderr)

    return q2(domain=domain, pc=pc)


# Add get function to support return result in dictionary form
get = _result2dict(query)


def getVersion() -> str:
    return VERSION


def getTestHint(tldString: str) -> Optional[str]:
    if tldString not in ZZ:
        return None

    k: str = "_test"
    if k not in ZZ[tldString]:
        return None

    return str(ZZ[tldString][k])


def cleanupWhoisResponse(
    whoisStr: str,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    withRedacted: bool = False,
    pc: Optional[ParameterContext] = None,
) -> str:
    tmp2: List[str] = []

    if pc is None:
        pc = ParameterContext(
            verbose=verbose,
            withRedacted=withRedacted,
            with_cleanup_results=with_cleanup_results,
        )

    skipFromHere = False
    tmp: List[str] = whoisStr.split("\n")
    for line in tmp:
        if skipFromHere is True:
            continue

        # some servers respond with: % Quota exceeded in the comment section (lines starting with %)
        if "quota exceeded" in line.lower():
            raise WhoisQuotaExceeded(whoisStr)

        if pc.with_cleanup_results is True and line.startswith("%"):  # only remove if requested
            continue

        if pc.withRedacted is False:
            if "REDACTED FOR PRIVACY" in line:  # these lines contibute nothing so ignore
                continue

        if (
            "Please query the RDDS service of the Registrar of Record" in line
        ):  # these lines contibute nothing so ignore
            continue

        # regular responses may at the end have meta info starting with a line >>> some texte <<<
        # similar trailing info exists with lines starting with -- but we wil handle them later
        # unfortunalery we have domains (google.st) that have this early at the top
        if 0:
            if line.startswith(">>>"):
                skipFromHere = True
                continue

        if line.startswith("Terms of Use:"):  # these lines contibute nothing so ignore
            continue

        tmp2.append(line.strip("\r"))

    return "\n".join(tmp2)
