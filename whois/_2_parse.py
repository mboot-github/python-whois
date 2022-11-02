import re
import sys

from typing import Any, Dict, Optional, List

from .exceptions import FailedParsingWhoisOutput
from .exceptions import WhoisQuotaExceeded

from . import tld_regexpr

Verbose = True

TLD_RE: Dict[str, Any] = {}

VERY_SMALL_RESPONSE_LINES = 5


def get_tld_re(tld: str) -> Any:
    if tld in TLD_RE:
        return TLD_RE[tld]

    if tld == "in":
        # is this actually used ?
        if Verbose:
            print("Verbose: directly returning tld: in_ for tld: in", file=sys.stderr)
        return "in_"

    v = getattr(tld_regexpr, tld)

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
        (k, re.compile(v, re.IGNORECASE) if (isinstance(v, str) and k[0] != "_") else v) for k, v in tmp.items()
    )

    # meta domains start with _: examples _centralnic and _donuts
    if tld[0] != "_":
        TLD_RE[tld] = tld_re

    return tld_re


# now fetch all defined data in
# The dir() method returns the list of valid attributes of the passed object

[get_tld_re(tld) for tld in dir(tld_regexpr) if tld[0] != "_"]


def cleanupWhoisResponse(
    response: str,
    verbose: bool = False,
    with_cleanup_results: bool = False,
) -> str:

    if 0:
        if verbose:
            print(f"BEFORE cleanup: \n{response}", file=sys.stderr)

    tmp: List = response.split("\n")

    tmp2 = []
    for line in tmp:
        # some servers respond with: % Quota exceeded in the comment section (lines starting with %)
        if "quota exceeded" in line.lower():
            raise WhoisQuotaExceeded(response)

        if with_cleanup_results is True and line.startswith("%"):
            continue

        if "REDACTED FOR PRIVACY" in line:
            continue

        if line.startswith("Terms of Use:"):
            continue

        tmp2.append(line)

    response = "\n".join(tmp2)
    if 0:
        if verbose:
            print(f"AFTER cleanup: \n{response}", file=sys.stderr)

    return response


def _doFilterVerySmallResponses(
    tld: str,
    whois_str: str,
    domainAsList: List,
    verbose: bool = False,
):
    if verbose:
        d = ".".join(domainAsList)
        print(f"line count < 5:: {tld} {d} {whois_str}", file=sys.stderr)

    s = whois_str.strip().lower()

    # NOTE: from here s is lowercase only
    # ---------------------------------
    noneStrings = [
        "not found",
        "no entries found",
        "status: free",
        "no such domain",
        "the queried object does not exist",
        "domain you requested is not known",
        "status: available",
    ]

    for i in noneStrings:
        if i in s:
            return None

    # ---------------------------------
    # is there any error string in the result
    if s.count("error"):
        return None

    # ---------------------------------
    quotaStrings = [
        "limit exceeded",
        "quota exceeded",
        "try again later",
        "please try again",
        "exceeded the maximum allowable number",
        "can temporarily not be answered",
        "please try again.",
        "queried interval is too short",
    ]

    for i in quotaStrings:
        if i in s:
            raise WhoisQuotaExceeded(whois_str)

    # ToDo:  Name or service not known

    raise FailedParsingWhoisOutput(whois_str)


def _doDnsSec(whois_str: str, verbose: bool = False):
    whois_dnssec: Any = whois_str.split("DNSSEC:")
    if len(whois_dnssec) >= 2:
        whois_dnssec = whois_dnssec[1].split("\n")[0]
        if whois_dnssec.strip() == "signedDelegation" or whois_dnssec.strip() == "yes":
            if verbose:
                msg = "detected valid dnssec entry in the raw string"
                print(msg, file=sys.stderr)
            return True
    return False


def _doSplitOnIanaPresent(whois_str: str, verbose: bool = False):
    # this is mostly not available in many tld's anymore, should be investigated
    # split whois_str to remove first IANA part showing info for TLD only
    whois_splitted = whois_str.split("source:       IANA")
    if len(whois_splitted) == 2:
        if verbose:
            msg = "stripping the raw string to remove 'source: IANA'"
            print(msg, file=sys.stderr)
        return whois_splitted[1]
    return whois_str


def _doIfServerNameThenStripUntilDomainName(whois_str: str, verbose: bool = False):
    # also not available for many modern tld's
    sn = re.findall(r"Server Name:\s?(.+)", whois_str, re.IGNORECASE)
    if sn:
        if verbose:
            print(f"found Server Name {sn}; looking for Domain Name", file=sys.stderr)
        index = whois_str.find("Domain Name:")
        return whois_str[index:]
    return whois_str


def do_parse(
    whois_str: str,
    tld: str,
    domainAsList: List[str],
    verbose: bool = False,
    with_cleanup_results=False,
) -> Optional[Dict[str, Any]]:

    whois_str = cleanupWhoisResponse(
        response=whois_str,
        verbose=verbose,
        with_cleanup_results=with_cleanup_results,
    )

    if whois_str.count("\n") < VERY_SMALL_RESPONSE_LINES:  # normally 5
        # may raise WhoisQuotaExceeded or FailedParsingWhoisOutput
        return _doFilterVerySmallResponses(tld, whois_str, domainAsList, verbose)

    result: Dict[str, Any] = {
        "tld": tld,
    }
    result["DNSSEC"] = _doDnsSec(whois_str, verbose)  # check the status of DNSSEC

    whois_str = _doSplitOnIanaPresent(whois_str, verbose)  # not very common anymore
    whois_str = _doIfServerNameThenStripUntilDomainName(whois_str, verbose)  # not very common anymore

    for k, v in TLD_RE.get(tld, TLD_RE["com"]).items():  # use TLD_RE["com"] as default
        if k.startswith("_"):  # skip meta element like: _server or _privateRegistry
            continue

        if v is None:  # we have no value for this element
            result[k] = [""]
            continue

        result[k] = v.findall(whois_str) or [""]

    return result
