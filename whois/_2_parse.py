import re
import sys

from typing import Any, Dict, Optional, List

from .exceptions import FailedParsingWhoisOutput
from .exceptions import WhoisQuotaExceeded

from . import tld_regexpr

Verbose = True

TLD_RE: Dict[str, Any] = {}


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
) -> str:

    if 0:
        if verbose:
            print(f"BEFORE cleanup: \n{response}", file=sys.stderr)

    tmp: List = response.split("\n")

    tmp2 = []
    for line in tmp:
        # cleanup comment lines commonly used by whois
        if line.startswith("%"):
            continue
        if "REDACTED FOR PRIVACY" in line:
            continue

        tmp2.append(line)

    response = "\n".join(tmp2)
    if 0:
        if verbose:
            print(f"AFTER cleanup: \n{response}", file=sys.stderr)

    return response


def do_parse(
    whois_str: str,
    tld: str,
    verbose: bool = False,
) -> Optional[Dict[str, Any]]:
    r: Dict[str, Any] = {"tld": tld}

    whois_str = cleanupWhoisResponse(
        response=whois_str,
        verbose=verbose,
    )

    if whois_str.count("\n") < 5:
        if Verbose:
            print(f"line count < 5:: {whois_str}", file=sys.stderr)

        s = whois_str.strip().lower()
        if s == "not found":
            return None

        # No entries found
        if "no entries found" in s:
            return None

        # TODO: Status: free
        if "status: free" in s:
            return None

        if "no such domain" in s:
            return None

        if s.count("error"):
            return None

        if "connection limit exceeded" in s:
            raise WhoisQuotaExceeded(whois_str)

        # TODO: output has: Server too busy, try again later
        if "server too busy, try again later" in s:
            raise WhoisQuotaExceeded(whois_str)

        # TODO: You exceeded the maximum allowable number of whois lookups.
        if "exceeded the maximum allowable number" in s:
            raise WhoisQuotaExceeded(whois_str)

        # ToDo:  Name or service not known

        raise FailedParsingWhoisOutput(whois_str)

    # check the status of DNSSEC
    r["DNSSEC"] = False
    whois_dnssec: Any = whois_str.split("DNSSEC:")

    if len(whois_dnssec) >= 2:
        whois_dnssec = whois_dnssec[1].split("\n")[0]

        if whois_dnssec.strip() == "signedDelegation" or whois_dnssec.strip() == "yes":
            r["DNSSEC"] = True

    # split whois_str to remove first IANA part showing info for TLD only
    whois_splitted = whois_str.split("source:       IANA")

    if len(whois_splitted) == 2:
        whois_str = whois_splitted[1]

    sn = re.findall(r"Server Name:\s?(.+)", whois_str, re.IGNORECASE)
    if sn:
        whois_str = whois_str[whois_str.find("Domain Name:") :]

    # return TLD_RE["com"] as default if tld not exists in TLD_RE
    for k, v in TLD_RE.get(tld, TLD_RE["com"]).items():
        if k.startswith("_"):
            # skip meta element like: _server
            continue

        if v is None:
            r[k] = [""]
        else:
            r[k] = v.findall(whois_str) or [""]
            # print("DEBUG: Keyval = " + str(r[k]))

    return r
