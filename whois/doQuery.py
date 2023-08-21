import os
import sys

from typing import (
    Optional,
)

from .domain import Domain
from .parameterContext import ParameterContext
from .processWhoisDomainRequest import ProcessWhoisDomainRequest
from .lastWhois import initLastWhois


WHOISDOMAIN: str = ""
if os.getenv("WHOISDOMAIN"):
    WHOISDOMAIN = str(os.getenv("WHOISDOMAIN"))

WD = WHOISDOMAIN.upper().split(":")

SIMPLISTIC = False
if "SIMPISTIC" in WD:
    SIMPLISTIC = True


def q2(
    domain: str,
    pc: ParameterContext,
) -> Optional[Domain]:

    initLastWhois()

    pwdr = ProcessWhoisDomainRequest(
        domain=domain,
        pc=pc,
    )

    return pwdr.processRequest()


def query(
    domain: str,
    force: bool = False,
    cache_file: Optional[str] = None,
    cache_age: int = 60 * 60 * 48,
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
    verbose: bool = False,
    with_cleanup_results: bool = False,
    internationalized: bool = False,
    include_raw_whois_text: bool = False,
    return_raw_text_for_unsupported_tld: bool = False,
    timeout: Optional[float] = None,
    parse_partial_response: bool = False,
    cmd: str = "whois",
    simplistic: bool = False,
    withRedacted: bool = False,
    pc: Optional[ParameterContext] = None,
    # if you use pc as argument all above params (except domain are ignored)
) -> Optional[Domain]:
    # see documentation about paramaters in parameterContext.py

    assert isinstance(domain, str), Exception("`domain` - must be <str>")

    if pc is None:
        pc = ParameterContext(
            force=force,
            cache_file=cache_file,
            cache_age=cache_age,
            slow_down=slow_down,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
            with_cleanup_results=with_cleanup_results,
            internationalized=internationalized,
            include_raw_whois_text=include_raw_whois_text,
            return_raw_text_for_unsupported_tld=return_raw_text_for_unsupported_tld,
            timeout=timeout,
            parse_partial_response=parse_partial_response,
            cmd=cmd,
            simplistic=simplistic,
            withRedacted=withRedacted,
        )

    if verbose:
        print(pc, file=sys.stderr)

    return q2(domain=domain, pc=pc)
