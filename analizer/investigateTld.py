#! /usr/bin/env python3

# should run after a valida database is created with analizeIanaTld.py

from typing import (
    Dict,
    Any,
)

import re
import idna as idna2

from ianaDatabase import IanaDatabase

import sys

sys.path.append("..")

from whoisdomain import tld_regexpr


def extractServers(aDict: Dict[str, Any]) -> Dict[str, Any]:
    servers: Dict[str, Any] = {}
    k = "_server"
    for key in aDict.keys():
        if k in aDict[key]:
            server = aDict[key][k]
            if server not in servers:
                servers[server] = []
            servers[server].append(key)
    return servers


def xMain() -> None:
    verbose = False
    dbFileName = "IanaDb.sqlite"

    iad = IanaDatabase(verbose=verbose)
    iad.connectDb(dbFileName)
    ss = extractServers(tld_regexpr.ZZ)

    # investigate all known iana tld and see if we have them

    sql = """
SELECT
    Link,
    Domain,
    Type,
    TLD_Manager,
    Whois,
    `DnsResolve-A`,
    RegistrationUrl
FROM
    IANA_TLD
"""

    rr, cur = iad.selectSql(sql)
    for row in cur:
        tld = row[0].replace("'", "")
        tld2 = "".join(map(lambda s: s and re.sub("[^\w\s]", "", s), row[1]))
        tld3 = row[1].replace(".", "").replace("'", "").replace("\u200f", "").replace("\u200e", "")
        tld4 = tld3
        try:
            tld3 = idna2.encode(tld3).decode() or tld3
        except Exception as e:
            print(f"## {tld} {tld2} {tld3}")
            continue

        tld4 = tld4.encode("idna").decode()
        if tld != tld2:
            if tld2 not in ss:
                print(tld, tld2, tld3, tld4, tld.encode("idna"))

        continue

        if tld != tld3:
            print(f"#SKIP {tld} {tld2} { tld3}")
            continue

        manager = row[3]
        w = row[4]
        resolve = row[5]
        reg = row[6]

        if tld2 == tld and tld in tld_regexpr.ZZ:
            continue

        if tld2 in tld_regexpr.ZZ and tld in tld_regexpr.ZZ:
            continue

        if manager == "NULL":
            if tld not in tld_regexpr.ZZ:
                print(f'ZZ["{tld}"] = ' + '{"_privateRegistry": True}')

            if tld2 != tld:
                if tld2 not in tld_regexpr.ZZ:
                    print(f'ZZ["{tld2}"] = ' + '{"_privateRegistry": True}')

            continue

        mm = {
            "com": [
                "whois.afilias-srs.net",
                "whois2.afilias-grs.net",
                "whois.nic.google",
                "whois.nic.gmo",
                "whois.gtld.knet.cn",
                "whois.registry.in",
                "whois.ngtld.cn",
            ],
            "sg": [
                "whois.sgnic.sg",
            ],
            "_teleinfo": [
                "whois.teleinfo.cn",
            ],
            "tw": [
                "whois.twnic.net.tw",
            ],
            "_centralnic": [
                "whois.centralnic.com",
            ],
        }

        found = False
        for key, value in mm.items():
            for n in value:
                if n in resolve:
                    if tld not in tld_regexpr.ZZ:
                        print(f'ZZ["{tld}"] = ' + '{"_server": "' + n + '", "extend": "' + key + '"}')
                    if tld2 != tld:
                        if tld2 not in tld_regexpr.ZZ:
                            print(f'ZZ["{tld2}"] = ' + '{"_server": "' + n + '", "extend": "' + key + '"}')
                    found = True

                if found:
                    break
            if found:
                break

        if found:
            continue

        if reg == "NULL" and w == "NULL":
            continue  # unclear, we have existing ns records indicating some tld's actually exist but have no whois, lets skip for now
            # TODO add ns records
            if tld not in tld_regexpr.ZZ:
                print(f'ZZ["{tld}"] = ' + '{"_privateRegistry": True}')

        if w == "NULL":
            continue

        w = w.replace("'", "")
        if w in ss:
            if tld not in tld_regexpr.ZZ:
                print(f'ZZ["{tld}"] = ' + '{"_server": "' + w + '", "extend": "' + ss[w][0] + '"}', "# ", w, ss[w])

            if tld2 != tld:
                if tld2 not in tld_regexpr.ZZ:
                    print(f'ZZ["{tld2}"] = ' + '{"_server": "' + w + '", "extend": "' + ss[w][0] + '"}', "# ", w, ss[w])
            continue

        print("# MISSING", tld, tld2, tld3, manager.replace("\n", ";"), w, resolve, reg)


xMain()
