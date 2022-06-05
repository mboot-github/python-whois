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
    slow_down: int = 0,
    ignore_returncode: bool = False,
    server: Optional[str] = None,
) -> str:
    k = ".".join(dl)
    if cache_file:
        cache_load(cache_file)

    if force or k not in CACHE or CACHE[k][0] < time.time() - CACHE_MAX_AGE:
        CACHE[k] = (
            int(time.time()),
            _do_whois_query(
                dl,
                ignore_returncode,
                server,
            ),
        )

        if cache_file:
            cache_save(cache_file)

        if slow_down:
            time.sleep(slow_down)

    return CACHE[k][1]


def _do_whois_query(
    dl: List[str],
    ignore_returncode: bool,
    server: Optional[str] = None,
) -> str:
    if platform.system() == "Windows":
        """
        Windows 'whois' command wrapper
        https://docs.microsoft.com/en-us/sysinternals/downloads/whois
        Usage: whois [-v] domainname [whois.server]
        """
        if not os.path.exists("whois.exe"):
            print("downloading dependencies")
            folder = os.getcwd()

            copy_command = r"copy \\live.sysinternals.com\tools\whois.exe " + folder
            print(copy_command)
            subprocess.call(
                copy_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
            )

        if server:
            cmd = [r".\whois.exe ", ".".join(dl), server]
        else:
            cmd = [r".\whois.exe ", ".".join(dl)]

    else:
        """
        Linux 'whois' command wrapper
        """
        if server:
            cmd = ["whois", ".".join(dl), "-h", server]
        else:
            cmd = ["whois", ".".join(dl)]

    # LANG=en is added to make the ".jp" output consist across all environments
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env={"LANG": "en"},
    )

    # print(p.stdout.read()+' '+p.stderr.read())
    r = p.communicate()[0].decode(errors="ignore")
    if ignore_returncode is False and p.returncode not in [0, 1]:
        raise WhoisCommandFailed(r)

    return r
