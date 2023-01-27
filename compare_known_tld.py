#! /usr/bin/env python3

# clone https://github.com/jophy/iana_tld_list in ./tmp

import urllib.request

from tmp.iana_tld_list.iana import IANA

import whois
from whois._1_query import _do_whois_query

# allow verbose messages during testing (all on stderr)
verbose = False

# by default the all tld file will be refreshed ever 24 hours,
# but you can force a new download anytime also
forceDownloadTld = False

# do you want to overwrite the results file ?
overwrite = True

# do you want interactive questions if files will be re-written?
interactive = False

# if autoProcessAll is True: all tld's will be processed (initial run > 20 minutes)
autoProcessAll = False

with_test_original = True

dirName = "/tmp/iana_data"

i = IANA(
    dirName=dirName,
    verbose=verbose,
    overwrite=overwrite,
    interactive=interactive,
    autoProcessAll=autoProcessAll,
    forceDownloadTld=forceDownloadTld,
)

# ge python whois known tld's and second level domains
known = sorted(whois.validTlds())

# get iana data
URL = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
response = urllib.request.urlopen(URL)
data = response.read().decode("utf-8").lower()
dataList = sorted(data.splitlines())

# filter out known names and try to detect names not known by iana
for name in known:
    if name in dataList:
        continue
    if "." in name:
        continue
    if name not in dataList:
        print(f"{name} tld name from python_whois is not known in IANA list")
        continue

dataList2 = []
for name in dataList:
    if name in known:
        continue
    dataList2.append(name)

# Try to auto detect new domains via IANA and some known common regex lists like .com
found = {}
for tld in dataList2:
    data, status = i.getInfoOnOneTld(tld)
    # print(status, data)

    if data and "whois" in data and data["whois"] and data["whois"] != "NULL":
        wh = data["whois"]
        if wh.endswith(f".{tld}"):
            dd = wh.split(".")[-2:]
        else:
            dd = ["meta", tld]

        zz = _do_whois_query(
            dd,
            ignore_returncode=False,
            server=wh,
        )

        pp = {"_server": wh, "extend": "com"}
        aDictToTestOverride = {tld: pp}

        whois.mergeExternalDictWithRegex(aDictToTestOverride)
        try:
            d = whois.query(".".join(dd))
            if d:
                print(d.__dict__)
                if len(d.name_servers) > 0:
                    found[tld] = pp
                    print(f"## ZZ['{tld}'] = {found[tld]} # auto-detected via IANA tld")
        except Exception as e:
            print(e)

    else:
        print(f"no whois info for tld: {tld}\n", data)
