#! /usr/bin/env python3
from typing import (
    # Optional,
    List,
    # Dict,
    Any,
    Tuple,
)

import sys

import json
import sqlite3


class IanaDatabase:
    verbose: bool = False
    conn: Any = None

    def __init__(
        self,
        verbose: bool = False,
    ):
        self.verbose = verbose

    def connectDb(
        self,
        fileName: str,
    ) -> None:
        self.conn = sqlite3.connect(fileName)
        self.testValidConnection()

    def testValidConnection(self) -> None:
        if self.conn is None:
            raise Exception("No valid connection to the database exist")

    def selectSql(
        self,
        sql: str,
        data: Any = None,
    ) -> Tuple[Any, Any]:
        self.testValidConnection()
        cur: Any = self.conn.cursor()

        try:
            if data:
                result = cur.execute(sql, data)
            else:
                result = cur.execute(sql)

        except Exception as e:
            print(sql, data, e, file=sys.stderr)
            exit(101)
        return result, cur

    def doSql(
        self,
        sql: str,
        data: Any = None,
        withCommit: bool = True,
    ) -> Any:
        self.testValidConnection()
        cur: Any = self.conn.cursor()

        try:
            if data:
                result = cur.execute(sql, data)
            else:
                result = cur.execute(sql)

            if withCommit:
                self.conn.commit()

        except Exception as e:
            print(sql, e, file=sys.stderr)
            exit(101)
        return result

    def createTableTld(self) -> None:
        sql = """
CREATE TABLE IF NOT EXISTS IANA_TLD (
    Link            TEXT PRIMARY KEY,
    Domain          TEXT NOT NULL UNIQUE,
    Type            TEXT NOT NULL,
    TLD_Manager     TEXT,
    Whois           TEXT,
    'DnsResolve-A'  TEXT,
    RegistrationUrl TEXT
);
"""
        rr = self.doSql(sql)
        if self.verbose:
            print(rr, file=sys.stderr)

    def createTablePsl(self) -> None:
        sql = """
CREATE TABLE IF NOT EXISTS IANA_PSL (
    Tld             TEXT NOT NULL,
    Psl             TEXT UNIQUE,
    Level           INTEGER NOT NULL,
    Type            TEXT NOT NULL,
    Comment         TEXT,
    PRIMARY KEY (Tld, Psl)
);
"""
        rr = self.doSql(sql)
        if self.verbose:
            print(rr, file=sys.stderr)

    def prepData(
        self,
        columns: List[str],
        values: List[str],
    ) -> Tuple[str, str, List[Any]]:
        cc = "`" + "`,`".join(columns) + "`"

        data = []
        vvv = []
        i = 0
        while i < len(values):
            v = "NULL"
            if values[i] is not None:
                v = values[i]
                if not isinstance(v, str) and not isinstance(v, int):
                    v = json.dumps(v, ensure_ascii=False)
                if isinstance(v, str):
                    v = "'" + v + "'"
                if isinstance(v, int):
                    v = int(v)
            data.append(v)
            vvv.append("?")
            i += 1

        vv = ",".join(vvv)
        return cc, vv, data

    def makeInsOrUpdSqlTld(
        self,
        columns: List[str],
        values: List[str],
    ) -> Tuple[str, List[Any]]:
        cc, vv, data = self.prepData(columns, values)
        return (
            f"""
INSERT OR REPLACE INTO IANA_TLD (
    {cc}
) VALUES(
    {vv}
);
""",
            data,
        )

    def makeInsOrUpdSqlPsl(
        self,
        columns: List[str],
        values: List[str],
    ) -> Tuple[str, List[Any]]:
        cc, vv, data = self.prepData(columns, values)

        return (
            f"""
INSERT OR REPLACE INTO IANA_PSL (
    {cc}
) VALUES(
    {vv}
);
""",
            data,
        )
