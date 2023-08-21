import sys

from typing import (
    Optional,
)


class DummyCache:
    def __init__(
        self,
        verbose: bool = False,
    ) -> None:
        self.verbose = verbose
        if self.verbose:
            print(f"{type(self).__name__} verbose: {self.verbose}", file=sys.stderr)

    def get(
        self,
        keyString: str,
    ) -> Optional[str]:
        if self.verbose:
            print(f"{type(self).__name__} get: {keyString}", file=sys.stderr)
        return None

    def put(
        self,
        keyString: str,
        data: str,
    ) -> str:
        if self.verbose:
            print(f"{type(self).__name__} put: {keyString}", file=sys.stderr)
        return data
