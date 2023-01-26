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

known = sorted(whois.validTlds())

URL = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
response = urllib.request.urlopen(URL)
data = response.read().decode("utf-8").lower()
dataList = sorted(data.splitlines())

for name in known:
    # print(name)
    if name in dataList:
        del dataList[dataList.index(name)]

# Try to auto detect new domaisn via IANA and some known common regex lists like .com

found = {}
for tld in dataList:
    data, status = i.getInfoOnOneTld(tld)
    # print(data)

    if data and "whois" in data and data["whois"] and data["whois"] != "NULL":
        wh = data['whois']
        # print(tld, wh, data, status)
        if wh.endswith(f".{tld}"):
            dd = wh.split(".")[-2:]
        else:
            dd = ["meta", tld]

        # print(dd)
        zz = _do_whois_query(
            dd,
            ignore_returncode=False,
            server=wh,
        )
        # print(zz)

        pp = { "_server": wh, "extend": "com"}
        aDictToTestOverride = { tld: pp }

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

for tld in found:
    print(f"## ZZ['{tld}'] = {found[tld]} # auto-detected via IANA tld")

# TODO
# also make a list of all tld (without dot in them) that no longer exists in iana, we can remove them
