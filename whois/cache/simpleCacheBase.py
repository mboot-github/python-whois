#! /usr/bin/env python3

import time
import sys


from typing import (
    Dict,
    Optional,
    Tuple,
)


class SimpleCacheBase:
    def __init__(
        self,
        verbose: bool = False,
        cacheMaxAge: int = (60 * 60 * 48),
    ) -> None:
        self.verbose = verbose
        self.memCache: Dict[str, Tuple[float, str]] = {}
        self.cacheMaxAge: int = cacheMaxAge

        if self.verbose:
            print("DEBUG cache init SimpleCacheBase", file=sys.stderr)

    def put(
        self,
        keyString: str,
        data: str,
    ) -> str:
        if self.verbose:
            print(f"DEBUG: cache put: {keyString}", file=sys.stderr)

        # store the currentTime and data tuple (time, data)
        self.memCache[keyString] = (
            int(time.time()),
            data,
        )
        return data

    def get(
        self,
        keyString: str,
    ) -> Optional[str]:
        if self.verbose:
            print(f"DEBUG cache get: {keyString}", file=sys.stderr)

        cData = self.memCache.get(keyString)
        if cData is None:
            if self.verbose:
                print("get: no data", file=sys.stderr)
            return None

        t = time.time()
        hasExpired = cData[0] < (t - self.cacheMaxAge)
        if hasExpired is True:
            if self.verbose:
                print(
                    f"DEBUG: cache get: data has expired {keyString} {cData[0]}, {t}, {self.cacheMaxAge}",
                    file=sys.stderr,
                )
            return None

        return cData[1]


if __name__ == "__main__":
    pass
