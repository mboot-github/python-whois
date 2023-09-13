#!  /usr/bin/env python3

import sys

from typing import (
    Optional,
    Any,
)

from .whoisCliInterface import WhoisCliInterface
from .cache.simpleCacheWithFile import SimpleCacheWithFile
from .context.parameterContext import ParameterContext
from .context.dataContext import DataContext

# actually also whois uses cache, so if you really dont want to use cache
# you should also pass the --force-lookup flag (on linux)

# Globals in Python are global to a module, not across all modules.
# (Many people are confused by this, because in, say, C, a global is the same across all implementation files unless you explicitly make it static.)
# see: https://stackoverflow.com/questions/15959534/visibility-of-global-variables-in-imported-modules
CACHE_STUB: Any = None


def setMyCache(myCache: Any) -> None:
    global CACHE_STUB

    if myCache:
        CACHE_STUB = myCache


def _initDefaultCache(
    pc: ParameterContext,
    dc: DataContext,
) -> Any:
    global CACHE_STUB

    if pc.verbose:
        print(f"DEBUG: CACHE_STUB {CACHE_STUB}", file=sys.stderr)

    # here you can override caching, if someone else already defined CACHE_STUB by this time, we use their caching
    if CACHE_STUB:
        if pc.verbose:
            print("DEBUG: cache already initialized", file=sys.stderr)
        return CACHE_STUB

    # if no cache defined init the default cache (optional with file storage based on pc)
    CACHE_STUB = SimpleCacheWithFile(
        verbose=pc.verbose,
        cacheFilePath=pc.cache_file,
        cacheMaxAge=pc.cache_age,
    )

    if pc.verbose:
        print("DEBUG: initializing default cache", file=sys.stderr)
    return CACHE_STUB


# TODO: future: can we use decorator for caching?
def doWhoisAndReturnString(
    pc: ParameterContext,
    dc: DataContext,
    wci: WhoisCliInterface,
) -> str:
    cache = _initDefaultCache(
        pc=pc,
        dc=dc,
    )
    keyString = ".".join(dc.dList)

    if pc.force is False:
        oldData: Optional[str] = cache.get(keyString)
        if oldData:
            return str(oldData)

    wci.init()
    return str(
        cache.put(
            keyString,
            wci.executeWhoisQueryOrReturnFileData(),
        )
    )


setMyCache(None)
