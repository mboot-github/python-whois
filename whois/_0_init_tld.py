import re

from typing import (
    Dict,
    List,
    Any,
)

from .exceptions import (
    UnknownTld,
)

from .tldDb.tld_regexpr import ZZ


TLD_RE: Dict[str, Dict[str, Any]] = {}
REG_COLLECTION_BY_KEY: Dict[str, Any] = {}


def _get_tld_re(
    tld: str,
    override: bool = False,
) -> Dict[str, Any]:
    if override is False:
        if tld in TLD_RE:
            return TLD_RE[tld]

    v = ZZ[tld]

    extend = v.get("extend")
    if extend:
        e = _get_tld_re(extend)  # call recursive
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

    # we want now to exclude andy key starting with _ like _server,_test, ...
    # dont recompile each re by themselves, reuse existing compiled re
    tld_re = dict(
        (k, REG_COLLECTION_BY_KEY[k][v] if (isinstance(v, str) and k[0] != "_") else v) for k, v in tmp.items()
    )

    # meta domains start with _: examples _centralnic and _donuts
    if tld[0] != "_":
        TLD_RE[tld] = tld_re

    return tld_re


def _initOne(
    tld: str,
    override: bool = False,
) -> None:
    if tld[0] == "_":  # skip meta domain patterns , these are not domains just handles we reuse
        return

    what = _get_tld_re(tld, override)

    # test if the string is identical after idna conversion
    d = tld.split(".")
    j = [k.encode("idna").decode() or k for k in d]
    tld2 = ".".join(j)
    if tld == tld2:
        return

    # also automatically see if we can internationalize the domains to the official ascii string
    TLD_RE[tld2] = what


def _buildRegCollection(
    zz: Dict[str, Any],
) -> Dict[str, Any]:
    regCollection: Dict[str, Any] = {}

    # get all regexes
    for name in zz:
        # print(name)
        z = zz[name]
        for key in z:
            if key is None:
                continue

            if key.startswith("_"):  # skip meta keys, they are not regexes
                continue

            if key in ["extend"]:  # this actually should have been a meta key: "_extend"
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


def _initOnImport() -> None:
    global REG_COLLECTION_BY_KEY
    # here we run the import processing
    # we load all tld's on import so we dont lose time later
    # we keep ZZ so we can later reuse it if we want to aoverrid or update tld's
    REG_COLLECTION_BY_KEY = _buildRegCollection(ZZ)
    override = False
    for tld in ZZ.keys():
        _initOne(tld, override)


# ========================================
# external use


def filterTldToSupportedPattern(
    domain: str,
    d: List[str],
    verbose: bool = False,
) -> str:
    # we have max 2 levels so first check if the last 2 are in our list
    tld = f"{d[-2]}.{d[-1]}"
    if tld in ZZ:
        return tld

    # if not check if the last item  we have
    tld = f"{d[-1]}"
    if tld in ZZ:
        return tld

    # if not fail
    a = f"The TLD {tld} is currently not supported by this package."
    b = "Use validTlds() to see what toplevel domains are supported."
    msg = f"{a} {b}"
    raise UnknownTld(msg)


def mergeExternalDictWithRegex(
    aDict: Dict[str, Any] = {},
) -> None:
    # merge in ZZ, this extends ZZ with new tld's and overrides existing tld's
    for tld in aDict.keys():
        ZZ[tld] = aDict[tld]

    # reprocess the regexes we newly defined or overrode
    override = True
    for tld in aDict.keys():
        _initOne(tld, override)


def validTlds() -> List[str]:
    return sorted(TLD_RE.keys())


_initOnImport()
