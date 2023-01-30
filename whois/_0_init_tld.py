import re
import sys

from typing import (
    Dict,
    List,
    Any,
)

from .tld_regexpr import ZZ
from .exceptions import (
    UnknownTld,
)

Verbose = False
TLD_RE: Dict[str, Any] = {}
REG_COLLECTION_BY_KEY: Dict = {}


def validTlds():
    return sorted(TLD_RE.keys())


def filterTldToSupportedPattern(
    domain: str,
    d: List[str],
    verbose: bool = False,
) -> str:
    # we have max 2 levels so first check if the last 2 are in our list
    tld = f"{d[-2]}.{d[-1]}"
    if tld in ZZ:
        print(f"we have {tld}", file=sys.stderr)
        return tld

    # if not check if the last item  we have
    tld = f"{d[-1]}"
    if tld in ZZ:
        print(f"we have {tld}", file=sys.stderr)
        return tld

    print(f"we DONT have {tld}", file=sys.stderr)

    # if not fail
    a = f"The TLD {tld} is currently not supported by this package."
    b = "Use validTlds() to see what toplevel domains are supported."
    msg = f"{a} {b}"
    raise UnknownTld(msg)


def get_tld_re(tld: str, override: bool = False) -> Any:
    if override is False:
        if tld in TLD_RE:
            return TLD_RE[tld]

    v = ZZ[tld]

    extend = v.get("extend")
    if extend:
        e = get_tld_re(extend)  # call recursive
        tmp = e.copy()
        tmp.update(v)  # and merge results in tmp with caller data in v
        # The update() method updates the dictionary with the elements
        # from another dictionary object or from an iterable of key/value pairs.
    else:
        tmp = v

    # finally we dont want to propagate the extend data
    # as it is only used to recursivly populate the dataset
    if "extend" in tmp:
        del tmp["extend"]

    # we want now to exclude _server hints
    tld_re = dict(
        # (k, re.compile(v, re.IGNORECASE) if (isinstance(v, str) and k[0] != "_") else v) for k, v in tmp.items()
        # dont recompile each re by themselves, reuse existing compiled re
        (k, REG_COLLECTION_BY_KEY[k][v] if (isinstance(v, str) and k[0] != "_") else v)
        for k, v in tmp.items()
    )

    # meta domains start with _: examples _centralnic and _donuts
    if tld[0] != "_":
        TLD_RE[tld] = tld_re

    return tld_re


def mergeExternalDictWithRegex(aDict: Dict = {}):
    # merge in ZZ, this extends ZZ with new tld's and overrides existing tld's
    for tld in aDict.keys():
        ZZ[tld] = aDict[tld]

    # reprocess te regexes we newly defined or overrode
    override = True
    for tld in aDict.keys():
        initOne(tld, override)


def initOne(tld, override: bool = False):
    if tld[0] == "_":  # skip meta domain patterns , these are not domains just handles we reuse
        return

    what = get_tld_re(tld, override)

    # test if the string is identical after idna conversion
    d = tld.split(".")
    j = [k.encode("idna").decode() or k for k in d]
    tld2 = ".".join(j)
    if tld == tld2:
        return

    # also automatically see if we can internationalize the domains to the official ascii string
    TLD_RE[tld2] = what
    if Verbose:
        print(f"{tld} -> {tld2}", file=sys.stderr)


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

            if reg in regCollection[key] and regCollection[key][reg] is not None:
                # we already have a compiled regex, no need to do it again
                continue

            regCollection[key][reg] = None
            if isinstance(reg, str):
                regCollection[key][reg] = re.compile(reg, flags=re.IGNORECASE)

    return regCollection


def initOnImport():
    global REG_COLLECTION_BY_KEY
    # here we run the import processing
    # we load all tld's on import so we dont lose time later
    # we keep ZZ so we can later reuse it if we want to aoverrid or update tld's
    REG_COLLECTION_BY_KEY = buildRegCollection(ZZ)
    override = False
    for tld in ZZ.keys():
        initOne(tld, override)


initOnImport()
