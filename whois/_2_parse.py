import re
import sys

from typing import (
    cast,
    Any,
    Dict,
    Optional,
    List,
    Tuple,
)

from ._0_init_tld import TLD_RE

from ._3_adjust import (
    Domain,
)

from .exceptions import (
    FailedParsingWhoisOutput,
    WhoisQuotaExceeded,
)

Verbose: bool = True

NONESTRINGS: List[str] = [
    "the domain has not been registered",
    "no match found for",
    "no matching record",
    "no match",
    "not found",
    "no data found",
    "no entries found",
    # "status: free", # we should not interprete the result if there is a result
    "no such domain",
    "the queried object does not exist",
    "domain you requested is not known",
    # "status: available", # we should not interprete the result if there is a result
    "no whois server is known for this kind of object",
    "nameserver not found",
    "malformed request",  # this means this domain is not in whois as it is on top of a registered domain
    "registration of this domain is restricted",
    "restricted",
    "this domain is currently available",
]

QUOTASTRINGS: List[str] = [
    "limit exceeded",
    "quota exceeded",
    "try again later",
    "please try again",
    "exceeded the maximum allowable number",
    "can temporarily not be answered",
    "please try again.",
    "queried interval is too short",
    "number of allowed queries exceeded",
]


def _handleShortResponse(
    tld: str,
    dl: List[str],
    whois_str: str,
    verbose: bool = False,
    simplistic: bool = False,
    include_raw_whois_text: bool = False,
) -> Optional[Domain]:
    if verbose:
        d = ".".join(dl)
        print(f"line count < 5:: {tld} {d} {whois_str}", file=sys.stderr)

    # TODO: some short responses are actually valid:
    # lookfor Domain: and Status but all other fields are missing so the regexec could fail
    # this domain is taken already or reserved

    # whois syswow.64-b.it
    # [Querying whois.nic.it]
    # [whois.nic.it]
    # Domain:             syswow.64-b.it
    # Status:             UNASSIGNABLE

    s = whois_str.strip().lower()

    # NOTE: from here s is lowercase only
    # ---------------------------------
    noneStrings = NoneStrings()
    for i in noneStrings:
        if i in s:
            return None

    # ---------------------------------
    # is there any error string in the result
    if s.count("error"):
        if verbose:
            print("i see 'error' in the result, return: None", file=sys.stderr)
        return None

    # ---------------------------------
    quotaStrings = QuotaStrings()
    for i in quotaStrings:
        if i in s:
            if simplistic:
                msg = "WhoisQuotaExceeded"
                return Domain(
                    data={},
                    whois_str=whois_str,
                    verbose=verbose,
                    include_raw_whois_text=include_raw_whois_text,
                    exeptionStr=msg,
                )
            raise WhoisQuotaExceeded(whois_str)

    if simplistic:
        msg = "FailedParsingWhoisOutput"
        return Domain(
            data={},
            whois_str=whois_str,
            verbose=verbose,
            include_raw_whois_text=include_raw_whois_text,
            exeptionStr=msg,
        )

    raise FailedParsingWhoisOutput(whois_str)


def _doDnsSec(
    whois_str: str,
) -> bool:
    whois_dnssec: Any = whois_str.split("DNSSEC:")
    if len(whois_dnssec) >= 2:
        whois_dnssec = whois_dnssec[1].split("\n")[0]
        if whois_dnssec.strip() == "signedDelegation" or whois_dnssec.strip() == "yes":
            return True
    return False


def _doIfServerNameLookForDomainName(
    whois_str: str,
    verbose: bool = False,
) -> str:
    # not often available anymore
    if re.findall(r"Server Name:\s?(.+)", whois_str, re.IGNORECASE):
        if verbose:
            msg = "i have seen Server Name:, looking for Domain Name:"
            print(msg, file=sys.stderr)
        whois_str = whois_str[whois_str.find("Domain Name:") :]
    return whois_str


def _doExtractPattensIanaFromWhoisString(
    tld: str,
    r: Dict[str, Any],
    whois_str: str,
    verbose: bool = False,
) -> Dict[str, Any]:
    # now handle the actual format if this whois response
    iana = {
        "domain_name": r"domain:\s?([^\n]+)",
        "registrar": r"organisation:\s?([^\n]+)",
        "creation_date": r"created:\s?([^\n]+)",
    }
    for k, v in iana.items():
        zz = re.findall(v, whois_str)
        if zz:
            if verbose:
                print(f"parsing iana data only for tld: {tld}, {zz}", file=sys.stderr)
            r[k] = zz
    return r


def _doExtractPattensFromWhoisString(
    tld: str,
    r: Dict[str, Any],
    whois_str: str,
    verbose: bool = False,
) -> Dict[str, Any]:
    for k, v in TLD_RE.get(tld, TLD_RE["com"]).items():  # use TLD_RE["com"] as default if a regex is missing
        if k.startswith("_"):  # skip meta element like: _server or _privateRegistry
            continue

        # Historical: here we use 'empty string' as default, not None
        if v is None:
            r[k] = [""]
        else:
            r[k] = v.findall(whois_str) or [""]

    return r


def _doSourceIana(
    tld: str,
    r: Dict[str, Any],
    whois_str: str,
    verbose: bool = False,
) -> Tuple[str, Optional[Dict[str, Any]]]:
    # here we can handle the example.com and example.net permanent IANA domains
    k = "source:       IANA"

    if verbose:
        msg = f"i have seen {k}"
        print(msg, file=sys.stderr)

    whois_splitted = whois_str.split(k)
    z = len(whois_splitted)
    if z > 2:
        return k.join(whois_splitted[1:]), None

    if z == 2 and whois_splitted[1].strip() != "":
        # if we see source: IANA and the part after is not only whitespace
        if verbose:
            msg = f"after: {k} we see not only whitespace: {whois_splitted[1]}"
            print(msg, file=sys.stderr)

        return whois_splitted[1], None

    # try to parse this as a IANA domain as after is only whitespace
    r = _doExtractPattensFromWhoisString(
        tld,
        r,
        whois_str,
        verbose,
    )  # set default values

    # now handle the actual format if this whois response
    r = _doExtractPattensIanaFromWhoisString(
        tld,
        r,
        whois_str,
        verbose,
    )

    return whois_str, r


# PUBLIC


def cleanupWhoisResponse(
    whois_str: str,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    withRedacted: bool = False,
) -> str:
    tmp2: List[str] = []

    # note we cannot do yet rstrip() on the lines as many registrars use \r and even trailing whitespace after entries
    # as the resulting matches are all stripped of leading and trailing whitespace this currently is fixed there
    # and relaxes the regexes: you will often see a capture with (.*)
    # we would have to fix all regexes to allow stripping all trailing whitespace
    # it would make many matches easier though.

    skipFromHere = False
    tmp: List[str] = whois_str.split("\n")
    for line in tmp:
        if skipFromHere is True:
            continue

        # some servers respond with: % Quota exceeded in the comment section (lines starting with %)
        if "quota exceeded" in line.lower():
            raise WhoisQuotaExceeded(whois_str)

        if with_cleanup_results is True and line.startswith("%"):  # only remove if requested
            continue

        if withRedacted is False:
            if "REDACTED FOR PRIVACY" in line:  # these lines contibute nothing so ignore
                continue

        if (
            "Please query the RDDS service of the Registrar of Record" in line
        ):  # these lines contibute nothing so ignore
            continue

        # regular responses may at the end have meta info starting with a line >>> some texte <<<
        # similar trailing info exists with lines starting with -- but we wil handle them later
        # unfortunalery we have domains (google.st) that have this early at the top
        if 0:
            if line.startswith(">>>"):
                skipFromHere = True
                continue

        if line.startswith("Terms of Use:"):  # these lines contibute nothing so ignore
            continue

        tmp2.append(line.strip("\r"))

    return "\n".join(tmp2)


def NoneStrings() -> List[str]:
    return NONESTRINGS


def NoneStringsAdd(aString: str) -> None:
    if aString and isinstance(aString, str) and len(aString) > 0:
        NONESTRINGS.append(aString)


def QuotaStrings() -> List[str]:
    return QUOTASTRINGS


def QuotaStringsAdd(aString: str) -> None:
    if aString and isinstance(aString, str) and len(aString) > 0:
        NONESTRINGS.append(aString)


def do_parse(
    whois_str: str,
    tld: str,
    dl: List[str],
    verbose: bool = False,
    with_cleanup_results: bool = False,
    simplistic: bool = False,
    include_raw_whois_text: bool = False,
    withRedacted: bool = False,
) -> Any:

    whois_str = cleanupWhoisResponse(
        whois_str=whois_str,
        verbose=verbose,
        with_cleanup_results=with_cleanup_results,
        withRedacted=withRedacted,
    )

    if whois_str.count("\n") < 5:
        result = _handleShortResponse(  # may raise:    FailedParsingWhoisOutput,    WhoisQuotaExceeded,
            tld=tld,
            dl=dl,
            whois_str=whois_str,
            verbose=verbose,
            simplistic=simplistic,
            include_raw_whois_text=include_raw_whois_text,
        )
        return result

    # this is the beginning of the return data
    r: Dict[str, Any] = {
        "tld": tld,
        "DNSSEC": _doDnsSec(whois_str),
    }

    if "source:       IANA" in whois_str:  # prepare for handling historical IANA domains
        whois_str, ianaDomain = _doSourceIana(tld, r, whois_str, verbose)
        if ianaDomain is not None:
            ianaDomain = cast(Optional[Dict[str, Any]], ianaDomain)
            return ianaDomain

    if "Server Name" in whois_str:  # handle old type Server Name (not very common anymore)
        whois_str = _doIfServerNameLookForDomainName(whois_str, verbose)

    return _doExtractPattensFromWhoisString(tld, r, whois_str, verbose)
