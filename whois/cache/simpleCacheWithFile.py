#! /usr/bin/env python3

import sys
import os
import json


from typing import (
    Optional,
    # Tuple,
)

from .simpleCacheBase import (
    SimpleCacheBase,
)


class SimpleCacheWithFile(SimpleCacheBase):
    cacheFilePath: Optional[str] = None

    def __init__(
        self,
        verbose: bool = False,
        cacheFilePath: Optional[str] = None,
        cacheMaxAge: int = (60 * 60 * 48),
    ) -> None:
        super().__init__(verbose=verbose, cacheMaxAge=cacheMaxAge)
        self.cacheFilePath = cacheFilePath
        if self.verbose:
            print("init SimpleCacheWithFile", file=sys.stderr)

    def _fileLoad(
        self,
    ) -> None:
        if self.cacheFilePath is None:
            return

        if not os.path.isfile(self.cacheFilePath):
            return

        if self.verbose:
            print(f"fileLoad: {self.cacheFilePath}", file=sys.stderr)

        with open(self.cacheFilePath, "r") as f:
            try:
                self.memCache = json.load(f)
            except Exception as e:
                print(f"ignore json load err: {e}", file=sys.stderr)

    def _fileSave(
        self,
    ) -> None:
        if self.cacheFilePath is None:
            return

        if self.verbose:
            print(f"_fileSave: {self.cacheFilePath}", file=sys.stderr)

        with open(self.cacheFilePath, "w") as f:
            json.dump(self.memCache, f)

    def put(
        self,
        keyString: str,
        data: str,
    ) -> str:
        super().put(keyString=keyString, data=data)
        self._fileSave()
        return data

    def get(
        self,
        keyString: str,
    ) -> Optional[str]:
        self._fileLoad()
        return super().get(keyString=keyString)


if __name__ == "__main__":
    pass
