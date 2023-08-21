#! /usr/bin/env python3

from typing import (
    # cast,
    Any,
    Dict,
    Optional,
    Tuple,
    List,
    Union,
)


from .exceptions import (
    WhoisQuotaExceeded,
)

from .domain import Domain
from .parameterContext import ParameterContext
from .whoisParser import WhoisParser


def cleanupWhoisResponse(
    whoisStr: str,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    withRedacted: bool = False,
    pc: Optional[ParameterContext] = None,
) -> str:
    tmp2: List[str] = []

    if pc is None:
        pc = ParameterContext(
            verbose=verbose,
            withRedacted=withRedacted,
            with_cleanup_results=with_cleanup_results,
        )

    skipFromHere = False
    tmp: List[str] = whoisStr.split("\n")
    for line in tmp:
        if skipFromHere is True:
            continue

        # some servers respond with: % Quota exceeded in the comment section (lines starting with %)
        if "quota exceeded" in line.lower():
            raise WhoisQuotaExceeded(whoisStr)

        if pc.with_cleanup_results is True and line.startswith("%"):  # only remove if requested
            continue

        if pc.withRedacted is False:
            if "REDACTED FOR PRIVACY" in line:  # these lines contibute nothing so ignore
                continue

        if "Please query the RDDS service of the Registrar of Record" in line:  # these lines contibute nothing so ignore
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


def do_parse(
    whoisStr: str,
    tldString: str,
    dList: List[str],
    pc: ParameterContext,
) -> Tuple[Union[Optional[Dict[str, Any]], Optional[Domain]], str]:  # was Any

    wp = WhoisParser(
        tldString=tldString,
        dList=dList,
        whoisStr=whoisStr,
        pc=pc,
    )

    return wp.parse()
