#! /usr/bin/env python3
from typing import (
    Optional,
    List,
    Dict,
    Any,
    # Tuple,
)

import sys
from bs4 import BeautifulSoup
import time
import requests_cache


class IanaCrawler:
    URL: str = "https://www.iana.org/domains/root/db"
    CacheTime: int = 3600 * 24  # default 24 hours
    Session: Any = None
    cacheName: str = ".iana_cache"
    verbose: bool = False
    cacheBackend: str = "filesystem"
    records: List[Any] = []
    columns: List[Any] = []

    resolver: Any = None

    def __init__(
        self,
        verbose: bool = False,
        resolver: Any = None,
    ):
        self.verbose = verbose
        self.resolver = resolver
        self.Session = requests_cache.CachedSession(
            self.cacheName,
            backend=self.cacheBackend,
        )

    def getUrl(self) -> str:
        return self.URL

    def getBasicBs(
        self,
        url: str,
    ) -> BeautifulSoup:
        try:
            response = self.Session.get(url)
        except Exception as e:
            # in case of no data, sleep and try again
            print(e, file=sys.stderr)
            time.sleep(15)
            response = self.Session.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def getAdditionalItem(
        self,
        what: str,
        data: List[str],
    ) -> Optional[str]:

        for i in [0, 1]:
            try:
                z: str = f"{what}:"
                if z in data[i]:
                    return data[i].replace(z, "").strip()
            except Exception as _:
                _ = _
                return None
        return None

    def getTldInfo(self) -> None:
        soup = self.getBasicBs(self.getUrl())
        table: Any = soup.find("table")  # the first table has the tld data

        self.records: List[Any] = []
        self.columns: List[Any] = []
        n = 0
        for tr in table.findAll("tr"):
            n += 1
            # extract header info if present
            ths = tr.findAll("th")
            if ths != []:
                for each in ths:
                    self.columns.append(each.text)
                continue

            # extrct data
            trs = tr.findAll("td")
            record = []
            for each in trs:
                try:
                    link = each.find("a")["href"]
                    aa = link.split("/")
                    record.append(aa[-1].replace(".html", ""))
                    record.append(each.text.strip())
                except Exception as _:
                    _ = _
                    record.append(each.text)
            self.records.append(record)

        self.columns.insert(0, "Link")

    def getTldPWithString(
        self,
        url: str,
        text: str,
    ) -> Optional[str]:
        soup = self.getBasicBs(url)
        gfg: List[Any] = soup.find_all(lambda tag: tag.name == "p" and text in tag.text)
        if len(gfg):
            s: str = gfg[0].text.strip()
            return s
        return None

    def resolveWhois(
        self,
        whois: str,
    ) -> List[Any]:
        ll: List[Any] = []
        if self.resolver:
            try:
                answer = list(self.resolver.resolve(whois, "A").response.answer)
            except Exception as e:
                print(whois, e, file=sys.stderr)
                time.sleep(30)
                answer = list(self.resolver.resolve(whois, "A").response.answer)

            for a in answer:
                s = str(a)
                if "\n" in s:
                    ss = s.split("\n")
                    ll.append(ss)
                else:
                    ll.append(s)

                if self.verbose:
                    print(a)
        return ll

    def addInfoToOneTld(
        self,
        tldItem: List[Any],
    ) -> List[str]:
        url = tldItem[0]

        if self.verbose:
            print(url, file=sys.stderr)

        if tldItem[3] == "Not assigned":
            tldItem[3] = None

        zz = {
            "Whois": "WHOIS Server",
            "RegistrationUrl": "URL for registration services",
        }
        for key, val in zz.items():
            regDataW = self.getTldPWithString(self.getUrl() + "/" + url + ".html", val)
            if regDataW:
                regDataW = regDataW.replace(val, key)
                regDataA = regDataW.split("\n")

                for s in [key]:
                    tldItem.append(self.getAdditionalItem(s, regDataA))
            else:
                tldItem.append(None)

        if tldItem[4]:
            ll = self.resolveWhois(tldItem[4])
            tldItem.append(ll)
        else:
            tldItem.append(None)

        if self.verbose:
            print(url, tldItem, file=sys.stderr)

        return tldItem

    def addInfoToAllTld(self) -> None:
        records2 = []
        for tldItem in self.records:
            rr = self.addInfoToOneTld(tldItem)
            if self.verbose:
                print(len(rr), rr)
            records2.append(rr)
        self.columns.insert(4, "Whois")
        self.columns.insert(5, "RegistrationUrl")
        self.columns.insert(6, "DnsResolve-A")
        self.records = records2
        self.columns[3] = self.columns[3].replace(" ", "_")

    def getResults(self) -> Dict[str, Any]:
        ll = list(self.columns)
        ll[3] = ll[3].replace(" ", "_")
        return {
            "header": ll,
            "data": self.records,
        }
