import subprocess
import time
import sys
import os
import platform
import json
from .exceptions import WhoisCommandFailed

from typing import Dict, List, Optional, Tuple


PYTHON_VERSION = sys.version_info[0]
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


def do_query(
    dl: List[str],
    force: bool = False,
    cache_file: Optional[str] = None,
    cache_age: int = CACHE_MAX_AGE,
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
    verbose: bool = False,
) -> str:
    k = ".".join(dl)

    if cache_file:
        if verbose:
            print(f"using cache file: {cache_file}", file=sys.stderr)
        cache_load(cache_file)

    # actually also whois uses cache, so if you really dont want to use cache
    # you should also pass the --force-lookup flag (on linux)
    if force or k not in CACHE or CACHE[k][0] < time.time() - cache_age:
        if verbose:
            print(f"force = {force}", file=sys.stderr)

        # slow down before so we can force individual domains at a slower tempo
        if slow_down:
            time.sleep(slow_down)

        # populate a fresh cache entry
        CACHE[k] = (
            int(time.time()),
            _do_whois_query(
                dl=dl,
                ignore_returncode=ignore_returncode,
                server=server,
                verbose=verbose,
            ),
        )

        if cache_file:
            cache_save(cache_file)

    return CACHE[k][1]


def tryInstallMissingWhoisOnWindows(verbose: bool = False):
    """
    Windows 'whois' command wrapper
    https://docs.microsoft.com/en-us/sysinternals/downloads/whois
    """
    folder = os.getcwd()
    copy_command = r"copy \\live.sysinternals.com\tools\whois.exe " + folder
    if verbose:
        print("downloading dependencies", file=sys.stderr)
        print(copy_command, file=sys.stderr)

    subprocess.call(
        copy_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )


def makeWhoisCommandToRun(
    dl: List[str],
    server: Optional[str] = None,
    verbose: bool = False,
):
    domain = ".".join(dl)
    wh = "whois"  # default 'whois'

    if platform.system() == "Windows":
        # Usage: whois [-v] domainname [whois.server]

        if os.path.exists("whois.exe"):
            wh = r".\whois.exe "
        else:
            find = False
            paths = os.environ["path"].split(";")
            for path in paths:
                wpath = os.path.join(path, "whois.exe")
                if os.path.exists(wpath):
                    wh = wpath
                    find = True
                    break

            if not find:
                tryInstallMissingWhoisOnWindows(verbose)

        if server:
            return [wh, "-v", "-nobanner", domain, server]
        return [wh, "-v", "-nobanner", domain]

    if server:
        return [wh, domain, "-h", server]
    return [wh, domain]


def testWhoisPythonFromStaticTestData(
    dl: List[str],
    ignore_returncode: bool,
    server: Optional[str] = None,
    verbose: bool = False,
) -> str:
    domain = ".".join(dl)
    testDir = os.getenv("TEST_WHOIS_PYTHON")
    pathToTestFile = f"{testDir}/{domain}/input"
    if os.path.exists(pathToTestFile):
        with open(pathToTestFile, mode="rb") as f:  # switch to binary mode as that is what Popen uses
            # make sure the data is treated exactly the same as the output of Popen
            return f.read().decode(errors="ignore")

    raise WhoisCommandFailed("")


def _do_whois_query(
    dl: List[str],
    ignore_returncode: bool,
    server: Optional[str] = None,
    verbose: bool = False,
) -> str:
    # if getenv[TEST_WHOIS_PYTON] fake whois by reading static data from a file
    # this wasy we can actually implemnt a test run with known data in and expected data out
    if os.getenv("TEST_WHOIS_PYTHON"):
        return testWhoisPythonFromStaticTestData(dl, ignore_returncode, server, verbose)

    cmd = makeWhoisCommandToRun(dl, server, verbose)
    if verbose:
        print(cmd, file=sys.stderr)

    # LANG=en is added to make the ".jp" output consist across all environments
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env={"LANG": "en"} if dl[-1] in ".jp" else None,
    )

    r = p.communicate()[0].decode(errors="ignore")
    if verbose:
        print(r, file=sys.stderr)

    if ignore_returncode is False and p.returncode not in [0, 1]:
        raise WhoisCommandFailed(r)

    return r
