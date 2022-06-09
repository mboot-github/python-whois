class UnknownTld(Exception):
    pass


class FailedParsingWhoisOutput(Exception):
    pass


class WhoisQuotaExceeded(Exception):
    pass


class UnknownDateFormat(Exception):
    pass


class WhoisCommandFailed(Exception):
    pass
