#! /usr/bin/env python3

from typing import (
    List,
    Dict,
    Any,
    Optional,
)

from .parameterContext import ParameterContext


class DataContext:
    def __init__(
        self,
        domain: str,
        pc: ParameterContext,
    ) -> None:
        self.pc = pc
        self.domain = domain

        self.data: Dict[str, Any] = {}
        self.lastWhoisStr: str = ""
        self.whoisStr: str = ""
        self.exeptionStr: Optional[str] = None
        self.dList: List[str] = []
