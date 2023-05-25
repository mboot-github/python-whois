#! /usr/bin/env python3
from typing import (
    # Optional,
    List,
    # Dict,
    Any,
    # Tuple,
)

import requests_cache


class PslGrabber:
    # notes: https://github.com/publicsuffix/list/wiki/Format

    URL: str = "https://publicsuffix.org/list/public_suffix_list.dat"
    CacheTime = 3600 * 24  # default 24 hours
    Session: Any = None
    cacheName = ".psl_cache"
    verbose: bool = False
    cacheBackend: str = "filesystem"

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.Session = requests_cache.CachedSession(
            self.cacheName,
            backend=self.cacheBackend,
        )

    def getUrl(self) -> str:
        return self.URL

    def getData(
        self,
        url: str,
    ) -> Any:
        response = self.Session.get(url)
        return response

    def ColumnsPsl(self) -> List[str]:
        return [
            "Tld",
            "Psl",
            "Level",
            "Type",
            "Comment",
        ]
