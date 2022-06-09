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


class WhoisPrivateRegistry(Exception):
    # also known as restricted : see comments at the bottom in tld_regexpr.py
    # almost no info is returned or there is no cli whois server at all:
    # see: https://www.iana.org/domains/root/db/<tld>.html
    pass
