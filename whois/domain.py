#! /usr/bin/env python3

from typing import (
    Any,
    List,
    Dict,
    Optional,
)

from .parameterContext import ParameterContext

from .handleDateStrings import str_to_date


class Domain:
    # mandatory: fields we expect always to be present (but can be None or '')
    name: Optional[str] = None
    tld: Optional[str] = None
    registrar: Optional[str] = None
    registrant_country: Optional[str] = None

    creation_date = None
    expiration_date = None
    last_updated = None

    status: Optional[str] = None
    statuses: List[str] = []

    dnssec: bool = False
    name_servers: List[str] = []

    # optional: fields that may not be present at all, many have no regex
    owner: Optional[str] = None
    abuse_contact = None
    reseller = None
    registrant = None
    admin = None
    emails: List[str] = []
    _exception: Optional[str] = None

    def _cleanupArray(
        self,
        data: List[str],
    ) -> List[str]:
        if "" in data:
            index = data.index("")
            data.pop(index)
        return data

    def _doNameservers(
        self,
        data: Dict[str, Any],
    ) -> None:
        tmp: List[str] = []
        for x in data["name_servers"]:
            if isinstance(x, str):
                tmp.append(x.strip().lower())
                continue
            # not a string but an array
            for y in x:
                tmp.append(y.strip().lower())

        self.name_servers = []
        for x in tmp:
            x = x.strip(" .")  # remove any leading or trailing spaces and/or dots
            if x:
                if " " in x:
                    x, _ = x.split(" ", 1)
                    x = x.strip(" .")

                x = x.lower()
                if x not in self.name_servers:
                    self.name_servers.append(x)
        self.name_servers = sorted(self.name_servers)

    def _doStatus(
        self,
        data: Dict[str, Any],
    ) -> None:
        self.status = data["status"][0].strip()
        self.statuses = sorted(  # sorted added to get predictable output during test
            list(  # list(set(...))) to deduplicate results
                set(
                    [s.strip() for s in data["status"]],
                ),
            ),
        )
        if "" in self.statuses:
            self.statuses = self._cleanupArray(self.statuses)

    def _doOptionalFields(
        self,
        data: Dict[str, Any],
    ) -> None:
        # optional fiels
        if "owner" in data:
            self.owner = data["owner"][0].strip()

        if "abuse_contact" in data:
            self.abuse_contact = data["abuse_contact"][0].strip()

        if "reseller" in data:
            self.reseller = data["reseller"][0].strip()

        if "registrant" in data:
            self.registrant = data["registrant"][0].strip()

        if "admin" in data:
            self.admin = data["admin"][0].strip()

        if "emails" in data:
            self.emails = sorted(  # sorted added to get predictable output during test
                list(  # list(set(...))) to deduplicate results
                    set(
                        [s.strip() for s in data["emails"]],
                    ),
                ),
            )
            if "" in self.emails:
                self.emails = self._cleanupArray(self.emails)

    def __init__(
        self,
        data: Dict[str, Any],
        pc: ParameterContext,
        whoisStr: Optional[str] = None,
        exeptionStr: Optional[str] = None,
    ):
        if pc.include_raw_whois_text and whoisStr is not None:
            self.text = whoisStr

        if exeptionStr is not None:
            self._exception = exeptionStr
            return

        self.name = data["domain_name"][0].strip().lower()
        self.tld = data["tld"].lower()

        if pc.return_raw_text_for_unsupported_tld is True:
            return

        # process mandatory fields that we expect always to be present
        # even if we have None or ''
        self.registrar = data["registrar"][0].strip()
        self.registrant_country = data["registrant_country"][0].strip()

        # date time items
        self.creation_date = str_to_date(
            data["creation_date"][0],
            self.tld,
            verbose=pc.verbose,
        )
        self.expiration_date = str_to_date(
            data["expiration_date"][0],
            self.tld,
            verbose=pc.verbose,
        )
        self.last_updated = str_to_date(
            data["updated_date"][0],
            self.tld,
            verbose=pc.verbose,
        )

        self.dnssec = data["DNSSEC"]
        self._doStatus(data)
        self._doNameservers(data)

        # optional fiels
        self._doOptionalFields(data)
