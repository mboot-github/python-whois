#! /usr/bin/env python3
from typing import (
    Any,
)

import io
import re
from dns.resolver import (
    Resolver,
    LRUCache,
)

import json

from ianaCrawler import IanaCrawler
from pslGrabber import PslGrabber
from ianaDatabase import IanaDatabase


def xMain() -> None:
    verbose: bool = True
    dbFileName: str = "IanaDb.sqlite"

    iad: Any = IanaDatabase(verbose=verbose)
    iad.connectDb(dbFileName)
    iad.createTableTld()
    iad.createTablePsl()

    resolver: Resolver = Resolver()
    resolver.cache = LRUCache()  # type: ignore

    iac = IanaCrawler(verbose=verbose, resolver=resolver)
    iac.getTldInfo()
    iac.addInfoToAllTld()
    xx = iac.getResults()
    for item in xx["data"]:
        sql, data = iad.makeInsOrUpdSqlTld(xx["header"], item)
        iad.doSql(sql, data)
    if verbose:
        print(json.dumps(iac.getResults(), indent=2, ensure_ascii=False))

    pg = PslGrabber()
    response = pg.getData(pg.getUrl())
    text = response.text
    buf = io.StringIO(text)

    section = ""
    while True:
        line = buf.readline()
        if not line:
            break

        z = line.strip()
        if len(z):
            if "// ===END " in z:
                section = ""

            if "// ===BEGIN ICANN" in z:
                section = "ICANN"

            if "// ===BEGIN PRIVATE" in z:
                section = "PRIVATE"

            if section == "PRIVATE":
                continue

            if re.match(r"^\s*//", z):
                # print("SKIP", z)
                continue

            n = 0
            z = z.split()[0]
            if "." in z:
                tld = z.split(".")[-1]
                n = len(z.split("."))
            else:
                tld = z

            sql, data = iad.makeInsOrUpdSqlPsl(pg.ColumnsPsl(), [tld, z, n, section, None])
            if verbose:
                print(data)
            iad.doSql(sql, data)


xMain()
