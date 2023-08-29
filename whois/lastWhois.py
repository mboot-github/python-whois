from typing import (
    List,
    Dict,
    Any,
)

from .context.parameterContext import ParameterContext

LastWhois: Dict[str, Any] = {}


def updateLastWhois(
    dList: List[str],
    whoisStr: str,
    pc: ParameterContext,
) -> None:
    global LastWhois
    LastWhois["Try"].append(
        {
            "Domain": ".".join(dList),
            "rawData": whoisStr,
            "server": pc.server,
        }
    )


def initLastWhois() -> None:
    global LastWhois
    LastWhois = {}
    LastWhois["Try"] = []  # init on start of query


def get_last_raw_whois_data() -> Dict[str, Any]:
    global LastWhois
    return LastWhois
