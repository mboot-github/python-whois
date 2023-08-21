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

from .doQuery import query, q2
from .lastWhois import get_last_raw_whois_data
from .doWhoisCommand import setMyCache
from .noneStrings import NoneStrings, NoneStringsAdd
from .quotaStrings import QuotaStrings, QuotaStringsAdd


from .doParse import (
    cleanupWhoisResponse,
)

from .tld_regexpr import ZZ
from .domain import Domain
from .parameterContext import ParameterContext

from .simpleCacheBase import SimpleCacheBase
from .simpleCacheWithFile import SimpleCacheWithFile
from .dummyCache import DummyCache
from .dbmCache import DBMCache

# from .redisCache import RedisCache

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
