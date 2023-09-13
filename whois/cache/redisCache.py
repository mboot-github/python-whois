#! /usr/bin/env python3

import sys
from typing import (
    Optional,
)

HAS_REDIS = False
try:
    import redis

    HAS_REDIS = True
except Exception as e:
    _ = e

if HAS_REDIS:

    class RedisCache:
        def __init__(self, verbose: bool = False, host: str = "localhost", port: int = 6379, db: int = 0) -> None:
            self.verbose = verbose

            self.pool = redis.ConnectionPool(
                host=host,
                port=port,
                db=db,
            )
            self.redis = redis.Redis(
                connection_pool=self.pool,
            )

            if self.verbose:
                print(f"{type(self).__name__} verbose: {self.verbose}", file=sys.stderr)

        def get(
            self,
            keyString: str,
        ) -> Optional[str]:
            if self.verbose:
                print(f"{type(self).__name__} get: {keyString}", file=sys.stderr)

            data = self.redis.get(keyString)
            if data:
                sdata: str = data.decode("utf-8")
                if self.verbose:
                    print(sdata, file=sys.stderr)
                return sdata
            return None

        def put(
            self,
            keyString: str,
            data: str,
        ) -> str:
            if self.verbose:
                print(f"{type(self).__name__} put: {keyString}", file=sys.stderr)

            self.redis.set(
                keyString,
                bytes(data, "utf-8"),
            )

            return data
