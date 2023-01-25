#! /usr/bin/env python3

import urllib.request
import whois

known = sorted(whois.validTlds())

URL = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
response = urllib.request.urlopen(URL)
data = response.read().decode("utf-8").lower()
dataList = sorted(data.splitlines())

for name in known:
    print(name)
    if name in dataList:
        del dataList[dataList.index(name)]

print(dataList)
