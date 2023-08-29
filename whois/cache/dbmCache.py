import sys
import dbm

from typing import (
    Optional,
)


class DBMCache:
    def __init__(
        self,
        dbmFile: str,
        verbose: bool = False,
    ) -> None:
        self.verbose = verbose
        self.dbmFile = dbmFile
        if self.verbose:
            print(f"{type(self).__name__} verbose: {self.verbose}", file=sys.stderr)

    def get(
        self,
        keyString: str,
    ) -> Optional[str]:
        if self.verbose:
            print(f"{type(self).__name__} get: {keyString}", file=sys.stderr)

        with dbm.open(self.dbmFile, "c") as db:
            data = db.get(keyString, None)
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

        with dbm.open(self.dbmFile, "c") as db:
            db[keyString] = bytes(data, "utf-8")

        return data
