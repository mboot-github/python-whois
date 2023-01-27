#! /usr/bin/env python3

import sys
import re
from typing import (
    # Optional,
    # List,
    Dict,
)

# most likely we can now introduce trailing whitespace trim on all lines from whois,
# and simplefy trailing whitespace rules
# as \r is already gone now and that was the most disticnt line ending
# occasionally we need to detect \n\s+ for groups that belong together
# mostly with indented blocks of nameservers

# import whois
from whois.tld_regexpr import ZZ


def buildRegCollection(zz: Dict):
    regCollection = {}
    # get all regexes
    for name in zz:
        # print(name)
        z = zz[name]
        for key in z:
            if key is None:
                continue

            if key.startswith("_"):
                continue

            if key in ["extend"]:
                continue

            if key not in regCollection:
                regCollection[key] = {}

            reg = z[key]
            if reg is None:
                continue

            regCollection[key][reg] = None
            if isinstance(reg, str):
                regCollection[key][reg] = re.compile(reg, flags=re.IGNORECASE)

    return regCollection


if __name__ == "__main__":
    regCollection = buildRegCollection(ZZ)

    for name in sorted(regCollection.keys()):
        print(f"## {name}", file=sys.stderr)
        for key in sorted(regCollection[name].keys()):
            if key:
                print(f"{name}: {key}")
