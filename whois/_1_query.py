import subprocess
import time
import sys
import os
import platform
import json

from typing import (
    Dict,
    List,
    Optional,
    Tuple,
)

from .exceptions import WhoisCommandFailed


# PYTHON_VERSION = sys.version_info[0]
CACHE: Dict[str, Tuple[int, str]] = {}
CACHE_MAX_AGE = 60 * 60 * 48  # 48h


def cache_load(cf: str) -> None:
    if not os.path.isfile(cf):
        return

    global CACHE
    f = open(cf, "r")

    try:
        CACHE = json.load(f)
    except Exception as e:
        print(f"ignore lson load err: {e}", file=sys.stderr)

    f.close()


def cache_save(cf: str) -> None:
    global CACHE

    f = open(cf, "w")
    json.dump(CACHE, f)
    f.close()


def _autoInstallWhoisOnWindows(verbose: bool = False):
    folder = os.getcwd()
    copy_command = r"copy \\live.sysinternals.com\tools\whois.exe " + folder

    if verbose:
        print("missing whois.exe; try automatic install", file=sys.stderr)
        print(copy_command, file=sys.stderr)

    subprocess.call(
        copy_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )


def _makeWhoisCommand2Run(
    domainAsList: List,
    server: Optional[str] = None,
    verbose: bool = False,
) -> List:
    domainStr = ".".join(domainAsList)

    if platform.system() == "Windows":
        """
        Windows 'whois' command wrapper, with auto install if missing
        https://docs.microsoft.com/en-us/sysinternals/downloads/whois
        Usage: whois [-v] domainname [whois.server]
        """
        if not os.path.exists("whois.exe"):
            _autoInstallWhoisOnWindows(verbose)

        if server:
            return [r".\whois.exe ", domainStr, "-v", server]
        return [r".\whois.exe ", domainStr]

    # default 'whois' command wrapper
    if server:
        return ["whois", domainStr, "-h", server]
    return ["whois", domainStr]


def _do_whois_query(
    domainAsList: List[str],
    ignore_returncode: bool,
    server: Optional[str] = None,
    verbose: bool = False,
) -> str:

    cmdList = _makeWhoisCommand2Run(domainAsList, server, verbose)

    # LANG=en is added to make the ".jp" output consist across all environments
    p = subprocess.Popen(
        cmdList,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env={"LANG": "en"} if domainAsList[-1] in ".jp" else None,
    )

    rawResultString = p.communicate()[0].decode(errors="ignore")
    if ignore_returncode is False and p.returncode not in [0, 1]:
        raise WhoisCommandFailed(rawResultString)

    return rawResultString


def do_query(
    domainAsList: List[str],
    force: bool = False,
    cache_file: Optional[str] = None,
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
    verbose: bool = False,
) -> str:
    domainStr = ".".join(domainAsList)

    if cache_file:
        cache_load(cache_file)

    # actually also whois uses cache, so if you really dont want to use cache
    # you should also pass the --force-lookup flag (on linux)

    if force or domainStr not in CACHE or CACHE[domainStr][0] < time.time() - CACHE_MAX_AGE:
        # slow down before so we can force individual domains at a slower tempo
        if slow_down:
            time.sleep(slow_down)

        # populate a fresh cache entry
        rawResultString = _do_whois_query(
            domainAsList=domainAsList,
            ignore_returncode=ignore_returncode,
            server=server,
            verbose=verbose,
        )
        CACHE[domainStr] = (int(time.time()), rawResultString)

        if cache_file:
            cache_save(cache_file)

    return CACHE[domainStr][1]
