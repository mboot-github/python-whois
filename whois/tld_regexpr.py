from typing import Dict

ZZ: Dict = {}

# elements starting with _
# are meta patterns and are not processed as domains
# examples:  _donuts, _centralnic

# elements ending in _
# like id_ , is_, if_, in_, global_ are conflicting words in python without a trailing _
# and auto replaced with a non conflicting word by adding a _ at the end

# NOTE: many registrars use \r and some even have whitespace after the entry
# Some items can be multiple: status, emails, name_servers
# the remaining are always singular

# when we finally apply the regexes we use IGNORE CASE allways on all matches

# Commercial TLD - Original Big 7
ZZ["com"] = {
    "extend": None,
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s?(.+)",
    "registrant": r"Registrant\s*Organi(?:s|z)ation:\s?(.+)",
    "registrant_country": r"Registrant Country:\s?(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "name_servers": r"Name Server:\s*(.+)\s*",  # host -t ns <domain> often has more nameservers then the output of whois
    "status": r"Status:\s?(.+)",
    # the trailing domain must have minimal 2 parts firstname.lastname@fld.tld
    # it may actually have more then 4 levels
    # to match the dot in firstname.lastname we must use \.
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

# United Kingdom - academic sub-domain
ZZ["ac.uk"] = {
    "extend": "uk",
    "domain_name": r"Domain:\n\s?(.+)",
    "owner": r"Domain Owner:\n\s?(.+)",
    "registrar": r"Registered By:\n\s?(.+)",
    "registrant": r"Registered Contact:\n\s*(.+)",
    "expiration_date": r"Renewal date:\n\s*(.+)",
    "updated_date": r"Entry updated:\n\s*(.+)",
    "creation_date": r"Entry created:\n\s?(.+)",
    "name_servers": r"Servers:\s*(.+)\t\n\s*(.+)\t\n",
}

ZZ["co.uk"] = {
    "extend": "uk",
    "domain_name": r"Domain name:\s+(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "name_servers": r"Name servers:(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?\n\n",  # capture up to 4
    "status": r"Registration status:\s*(.+)",
    "creation_date": r"Registered on:(.+)",
    "expiration_date": r"Expiry date:(.+)",
    "updated_date": r"Last updated:(.+)",
    "owner": r"Domain Owner:\s+(.+)",
    "registrant": r"Registrant:\n\s+(.+)",  # example meta.co.uk has a registrar google.co.uk has not
}

# United Arab Emirates
# ae = {    "extend": "ar"}
# redefined below

# Anguilla
ZZ["ai"] = {
    "extend": "com",
    "_server": "whois.nic.ai",
}

# Armenia
ZZ["am"] = {
    "extend": None,
    "domain_name": r"Domain name:\s+(.+)",
    "status": r"Status:\s(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "registrant": r"Registrant:\s+(.+)",
    "registrant_country": r"Registrant:\n.+\n.+\n.+\n\s+(.+)",
    "creation_date": r"Registered:\s+(.+)",
    "expiration_date": r"Expires:\s+(.+)",
    "updated_date": r"Last modified:\s+(.+)",
    "name_servers": r"DNS servers.*:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?",
}

# Amsterdam
ZZ["amsterdam"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Domain Status:\s?(.+)",
}

ZZ["app"] = {
    "extend": "com",
    "_server": "whois.nic.google",
}

# Argentina
ZZ["ar"] = {
    "extend": "com",
    "domain_name": r"domain\s*:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "creation_date": r"registered:\s?(.+)",
    "expiration_date": r"expire:\s?(.+)",
    "updated_date": r"changed\s*:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)\s*",
}

ZZ["asia"] = {
    "extend": "com",
}

# Austria
ZZ["at"] = {
    "extend": "com",
    "_server": "whois.nic.at",
    "domain_name": r"domain:\s?(.+)",
    "updated_date": r"changed:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant": r"registrant:\s?(.+)",
}

# Australia
ZZ["au"] = {
    "extend": "com",
    "registrar": r"Registrar Name:\s?(.+)",
    "updated_date": r"Last Modified:([^\n]*)",  # fix empty LastModified
}

ZZ["ax"] = {
    "extend": "com",
    "domain_name": r"domain\.+:\s*(\S+)",
    "registrar": r"registrar\.+:\s*(.+)",
    "creation_date": r"created\.+:\s*(\S+)",
    "expiration_date": r"expires\.+:\s*(\S+)",
    "updated_date": r"modified\.+:\s?(\S+)",
    "name_servers": r"nserver\.+:\s*(\S+)",  # host -t ns gives back more then output of whois
    "status": r"status\.+:\s*(\S+)",
    "registrant": r"Holder\s+name\.+:\s*(.+)\r?\n",  # not always present see meta.ax and google.ax
    "registrant_country": r"country\.+:\s*(.+)\r?\n",  # not always present see meta.ax and google.ax
}

ZZ["aw"] = {
    "extend": "nl",
    "name_servers": r"Domain nameservers:\s+(\S+)[ \t]*\r?\n(?:\s+(\S+))?",
}

# Banking TLD - ICANN
ZZ["bank"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
}

ZZ["be"] = {
    "extend": "pl",
    "domain_name": r"\nDomain:\s*(.+)",
    "registrar": r"Company Name:\n?(.+)",
    "creation_date": r"Registered:\s*(.+)\n",
    "status": r"Status:\s?(.+)",
    "name_servers": r"Nameservers:(?:\n[ \t]+(\S+))?(?:\n[ \t]+(\S+))?(?:\n[ \t]+(\S+))?(?:\n[ \t]+(\S+))?\n\n",  # fix missing and wrong output
}

ZZ["biz"] = {
    "extend": "com",
    "registrar": r"Registrar:\s?(.+)",
    "registrant": r"Registrant Organization:\s?(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": None,
}

ZZ["br"] = {
    "extend": "com",
    "domain_name": r"domain:\s?(.+)",
    "registrar": "nic.br",
    "registrant": None,
    "owner": r"owner:\s?(.+)",
    "creation_date": r"created:\s?(.+)",
    "expiration_date": r"expires:\s?(.+)",
    "updated_date": r"changed:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)",
    "status": r"status:\s?(.+)",
}

ZZ["by"] = {  # fix multiple dns by removing test for \n at the beginning as it is not needed
    "extend": "com",
    "domain_name": r"Domain Name:\s*(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "registrant": r"Org:\s*(.+)",
    "registrant_country": r"Country:\s*(.+)",
    "creation_date": r"Creation Date:\s*(.+)",
    "expiration_date": r"Expiration Date:\s*(.+)",
    "updated_date": r"Updated Date:\s*(.+)",
    "name_servers": r"Name Server:\s+(\S+)\n",
}

# Brittany (French Territory)
# Some personal data could be obfuscated at request from the registrant
ZZ["bzh"] = {
    "extend": "fr",
    "domain_name": r"Domain Name:\s*(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "registrant": r"Registrant Organization:\s*(.+)",
    "registrant_country": r"Registrant Country:\s*(.*)",
    "creation_date": r"Creation Date:\s*(.*)",
    "expiration_date": r"Registry Expiry Date:\s*(.*)",
    "updated_date": r"Updated Date:\s*(.*)",
    "name_servers": r"Name Server:\s*(.*)",
    "status": r"Domain Status:\s*(.*)",
}

ZZ["ca"] = {
    "extend": "com",
}

ZZ["cat"] = {
    "extend": "com",
    "_server": "whois.nic.cat",
}

ZZ["cc"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

ZZ["cl"] = {
    "extend": "com",
    "registrar": "nic.cl",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "name_servers": r"Name Server:\s*(.+)\s*",
}

ZZ["click"] = {
    "extend": "com",
}

ZZ["cloud"] = {
    "extend": "com",
}

ZZ["club"] = {
    "extend": "com",
}

ZZ["cn"] = {
    "extend": "com",
    "registrar": r"Sponsoring Registrar:\s?(.+)",
    "registrant": r"Registrant:\s?(.+)",
    "creation_date": r"Registration Time:\s?(.+)",
    "expiration_date": r"Expiration Time:\s?(.+)",
}

ZZ["co"] = {
    "extend": "biz",
    "status": r"Status:\s?(.+)",
}

ZZ["com.au"] = {
    "extend": "au",
}

ZZ["com.tr"] = {
    "extend": "com",
    "domain_name": r"\*\* Domain Name:\s?(.+)",
    "registrar": r"Organization Name\s+:\s?(.+)",
    "registrant": r"\*\* Registrant:\s+?(.+)",
    "registrant_country": None,
    "creation_date": r"Created on\.+:\s?(.+).",
    "expiration_date": r"Expires on\.+:\s?(.+).",  # note the trailing . on both dates fields
    "updated_date": "",
    "name_servers": r"\*\* Domain Servers:\n(?:(\S+)\n)(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)\n?",
    "status": None,
}

ZZ["edu.tr"] = {"extend": "com.tr"}

ZZ["org.tr"] = {"extend": "com.tr"}

ZZ["net.tr"] = {"extend": "com.tr"}

ZZ["co.il"] = {
    "extend": "com",
    "domain_name": r"domain:\s*(.+)",
    "registrar": r"registrar name:\s*(.+)",
    "registrant": None,
    "registrant_country": None,
    "creation_date": None,
    "expiration_date": r"validity:\s*(.+)",
    "updated_date": None,
    "name_servers": r"nserver:\s*(.+)",
    "status": r"status:\s*(.+)",
}

ZZ["co.jp"] = {  # is redefined later with english
    "extend": "jp",
    "domain_name": r"\[ドメイン名\]\s?(.+)",
    "creation_date": r"\[登録年月\]\s?(.+)",
    "expiration_date": r"\[状態\].+\((.+)\)",
    "updated_date": r"\[最終更新\]\s?(.+)",
}

ZZ["courses"] = {"extend": "com"}

ZZ["cr"] = {"extend": "cz"}

ZZ["cz"] = {
    "extend": "com",
    "domain_name": r"domain:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant": r"registrant:\s?(.+)",
    "registrant_country": None,
    "creation_date": r"registered:\s?(.+)",
    "expiration_date": r"expire:\s?(.+)",
    "updated_date": r"changed:\s?(.+)",
    "name_servers": r"nserver:\s+(\S+)",
    "status": r"status:\s*(.+)",
}

# The .de NIC whois servers no longer provide any PII data for domains in the TLD.
# To obtains "personal" data, one must use the web interface: http://www.denic.de/en/domains/whois-service/web-whois.html
ZZ["de"] = {
    "extend": "com",
    "domain_name": r"\ndomain:\s*(.+)",
    "updated_date": r"\nChanged:\s?(.+)",
    "name_servers": r"Nserver:\s*(.+)",
}

# Developer
ZZ["dev"] = {"extend": "com"}

# Denmark
ZZ["dk"] = {
    "extend": None,
    "domain_name": r"Domain:\s?(.+)",
    "registrar": None,
    "registrant": r"Registrant\s*Handle:\s*\w*\s*Name:\s?(.+)",
    "registrant_country": r"Country:\s?(.+)",
    "creation_date": r"Registered:\s?(.+)",
    "expiration_date": r"Expires:\s?(.+)",
    "updated_date": None,
    "name_servers": r"Hostname:\s*(.+)\s*",
    "status": r"Status:\s?(.+)",
    "emails": None,
}

ZZ["download"] = {
    "extend": "amsterdam",
    "name_servers": r"Name Server:[ \t]+(\S+)",  # fix needed after strip(\r) in _2_parse.py in version 0.19
    "status": r"Domain Status:\s*([a-zA-z]+)",
}

ZZ["edu"] = {
    "extend": "com",
    "registrant": r"Registrant:\s*(.+)",
    "creation_date": r"Domain record activated:\s?(.+)",
    "updated_date": r"Domain record last updated:\s?(.+)",
    "expiration_date": r"Domain expires:\s?(.+)",
    "name_servers": r"Name Servers:\s?\t(.+)\n\t(.+)\n",
}

# estonian
ZZ["ee"] = {
    "extend": "com",
    "domain_name": r"Domain:\nname:\s+(.+\.ee)\n",
    "registrar": r"Registrar:\nname:\s+(.+)\n",
    "registrant": r"Registrant:\nname:\s+(.+)\n",
    "registrant_country": r"Registrant:(?:\n+.+\n*)*country:\s+(.+)\n",
    "creation_date": r"Domain:(?:\n+.+\n*)*registered:\s+(.+)\n",
    "expiration_date": r"Domain:(?:\n+.+\n*)*expire:\s+(.+)\n",
    "updated_date": r"Domain:(?:\n+.+\n*)*changed:\s+(.+)\n",
    "name_servers": r"nserver:\s*(.+)",
    "status": r"Domain:(?:\n+.+\n*)*status:\s+(.+)\n",
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

ZZ["eu"] = {
    "extend": "com",
    "registrar": r"Name:\s?(.+)",
    "domain_name": r"\nDomain:\s*(.+)",
    "name_servers": r"Name servers:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?",
}

ZZ["fi"] = {
    "extend": None,
    "domain_name": r"domain\.+:\s?(.+)",
    "registrar": r"registrar\.+:\s?(.+)",
    "registrant_country": None,
    "creation_date": r"created\.+:\s?(.+)",
    "expiration_date": r"expires\.+:\s?(.+)",
    "updated_date": r"modified\.+:\s?(.+)",
    "name_servers": r"nserver\.+:\s*(.+)",
    "status": r"status\.+:\s?(.+)",
}

ZZ["fit"] = {
    "extend": "com",
}

ZZ["fm"] = {
    "extend": "com",
}

ZZ["fo"] = {
    "extend": "com",
    "registrant": None,
}

ZZ["fr"] = {
    "extend": "com",
    "domain_name": r"domain:\s?(.+)",
    "registrar": r"registrar:\s*(.+)",
    "registrant": r"contact:\s?(.+)",
    "creation_date": r"created:\s?(.+)",
    "expiration_date": r"Expiry Date:\s?(.+)",
    "updated_date": r"last-update:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)",
    "status": r"status:\s?(.+)",
}

ZZ["game"] = {
    "extend": "amsterdam",
}

ZZ["global"] = {
    "extend": "amsterdam",
    "name_servers": r"Name Server: (.+)",
}

# Honduras
ZZ["hn"] = {
    "extend": "com",
}

# Hong Kong
ZZ["hk"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s+(.+)",
    "registrar": r"Registrar Name:\s?(.+)",
    "registrant": r"Company English Name.*:\s?(.+)",
    "registrant_country": None,
    "creation_date": r"Domain Name Commencement Date:\s?(.+)",
    "expiration_date": r"Expiry Date:\s?(.+)",
    "updated_date": None,
    #  name servers have trailing whitespace, lines are \n only
    "name_servers": r"Name Servers Information:\s*(?:(\S+)[ \t]*\n)(?:(\S+)[ \t]*\n)?(?:(\S+)[ \t]*\n)?(?:(\S+)[ \t]*\n)?",
    "status": None,
}

ZZ["id"] = {
    "extend": "com",
    "registrar": r"Sponsoring Registrar Organization:\s?(.+)",
    "creation_date": r"Created On:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "updated_date": r"Last Updated On:\s?(.+)$",
}

# Ireland
ZZ["ie"] = {
    "extend": "com",
}

ZZ["im"] = {
    "domain_name": r"Domain Name:\s+(.+)",
    "status": None,
    "registrar": None,
    "registrant_country": None,
    "creation_date": "",
    "expiration_date": r"Expiry Date:\s?(.+)",
    "updated_date": "",
    "name_servers": r"Name Server:(.+)",
}

ZZ["in"] = {
    "extend": "com",
}

ZZ["info"] = {
    "extend": "com",
}

ZZ["ink"] = {
    "extend": "amsterdam",
}

ZZ["io"] = {
    "extend": "com",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
}

ZZ["ir"] = {
    "extend": None,
    "domain_name": r"domain:\s?(.+)",
    "registrar": "nic.ir",
    "registrant_country": None,
    "creation_date": None,
    "status": None,
    "expiration_date": r"expire-date:\s?(.+)",
    "updated_date": r"last-updated:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)\s*",
}

ZZ["is"] = {
    "domain_name": r"domain:\s?(.+)",
    "registrar": None,
    "registrant": r"registrant:\s?(.+)",
    "registrant_country": None,
    "creation_date": r"created:\s?(.+)",
    "expiration_date": r"expires:\s?(.+)",
    "updated_date": None,
    "name_servers": r"nserver:\s?(.+)",
    "status": None,
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

ZZ["it"] = {
    "extend": "com",
    "domain_name": r"Domain:\s?(.+)",
    "registrar": r"Registrar\s*Organization:\s*(.+)",
    "registrant": r"Registrant\s*Organization:\s*(.+)",
    "creation_date": r"Created:\s?(.+)",
    "expiration_date": r"Expire Date:\s?(.+)",
    "updated_date": r"Last Update:\s?(.+)",
    # "name_servers": r"Nameservers\s?(.+)\s?(.+)\s?(.+)\s?(.+)",
    "name_servers": r"Nameservers(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?",
    "status": r"Status:\s?(.+)",
}

# The Japanese whois servers always return English unless a Japanese locale is specified in the user's LANG environmental variable.
# See: https://www.computerhope.com/unix/uwhois.htm
# Additionally, whois qeuries can explicitly request english:
# 	To suppress Japanese output, add'/e' at the end of command, e.g. 'whois -h whois.jprs.jp xxx/e'.
#
ZZ["jp"] = {
    "domain_name": r"\[Domain Name\]\s?(.+)",
    #    'registrar':                None,
    "registrar": r"\[ (.+) database provides information on network administration. Its use is    \]",
    "registrant": r"\[Registrant\]\s?(.+)",
    "registrant_country": None,
    #    'creation_date':            r'\[登録年月日\]\s?(.+)',
    #    'expiration_date':          r'\[有効期限\]\s?(.+)',
    #    'updated_date':             r'\[最終更新\]\s?(.+)',
    "creation_date": r"\[Created on\]\s?(.+)",
    "expiration_date": r"\[Expires on\]\s?(.+)",
    "updated_date": r"\[Last Updated\]\s?(.+)",
    "name_servers": r"\[Name Server\]\s*(.+)",
    #    'status':                   r'\[状態\]\s?(.+)',
    "status": r"\[Status\]\s?(.+)",
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

# The Japanese whois servers always return English unless a Japanese locale is specified in the user's LANG environmental variable.
# See: https://www.computerhope.com/unix/uwhois.htm
# Additionally, whois qeuries can explicitly request english:
# 	To suppress Japanese output, add'/e' at the end of command, e.g. 'whois -h whois.jprs.jp xxx/e'.
#
ZZ["co.jp"] = {
    "extend": "jp",
    #    'domain_name':              r'\[ドメイン名\]\s?(.+)',
    "domain_name": r"\[Domain Name\]\s?(.+)",
    #    'creation_date':            r'\[登録年月\]\s?(.+)',
    #    'expiration_date':          r'\[状態\].+\((.+)\)',
    #    'updated_date':             r'\[最終更新\]\s?(.+)',
    "creation_date": r"\[Registered Date\]\s?(.+)",
    "expiration_date": None,
    "updated_date": r"\[Last Update\]\s?(.+)",
    "status": r"\[State\]\s?(.+)",
}

# All Japanese Sub-TLDs. See: https://jprs.co.jp/en/jpdomain.html
ZZ["ne.jp"] = {"extend": "co.jp"}
ZZ["or.jp"] = {"extend": "co.jp"}
ZZ["go.jp"] = {"extend": "co.jp"}
ZZ["ac.jp"] = {"extend": "co.jp"}
ZZ["ad.jp"] = {"extend": "co.jp"}
ZZ["ed.jp"] = {"extend": "co.jp"}
ZZ["gr.jp"] = {"extend": "co.jp"}
ZZ["lg.jp"] = {"extend": "co.jp"}
ZZ["geo.jp"] = {"extend": "co.jp"}
ZZ["kiwi"] = {"extend": "com"}

ZZ["kg"] = {
    "domain_name": r"Domain\s+(\S+)",
    "registrar": r"Billing\sContact:\n.*\n\s+Name:\s(.+)\n",
    "registrant_country": None,
    "expiration_date": r"Record expires on:\s+(.+)",
    "creation_date": r"Record created:\s+(.+)",
    "updated_date": r"Record last updated on:\s+(.+)",
    # name servers have trailing whitespace
    "name_servers": r"Name servers in the listed order:\n\n(?:(\S+)[ \t]*\S*\n)(?:(\S+)[ \t]*\S*\n)?(?:(\S+)[ \t]*\S*\n)?\n",
    # nameservers can have trailing ip (e.g. google.kg)
    "status": r"Domain\s+\S+\s+\((\S+)\)",
}

# Saint Kitts and Nevis
ZZ["kn"] = {
    "extend": "com",
}

ZZ["kr"] = {
    "extend": "com",
    "domain_name": r"Domain Name\s*:\s?(.+)",
    "registrar": r"Authorized Agency\s*:\s*(.+)",
    "registrant": r"Registrant\s*:\s*(.+)",
    "creation_date": r"Registered Date\s*:\s?(.+)",
    "expiration_date": r"Expiration Date\s*:\s?(.+)",
    "updated_date": r"Last Updated Date\s*:\s?(.+)",
    "status": r"status\s*:\s?(.+)",
    "name_servers": r"Host Name\s+:\s+(\S+)\n",
}

ZZ["kz"] = {
    "extend": None,
    "domain_name": r"Domain name\.+:\s(.+)",
    "registrar": r"Current Registar:\s(.+)",
    "registrant_country": r"Country\.+:\s?(.+)",
    "expiration_date": None,
    "creation_date": r"Domain created:\s(.+)",
    "updated_date": r"Last modified :\s(.+)",
    "name_servers": r"ary server\.+:\s+(\S+)",
    "status": r"Domain status :(?:\s+([^\n]+)\n)",
}

ZZ["link"] = {
    "extend": "amsterdam",
}

ZZ["lt"] = {
    "extend": "com",
    "domain_name": r"Domain:\s?(.+)",
    "creation_date": r"Registered:\s?(.+)",
    "expiration_date": r"Expires:\s?(.+)",
    "name_servers": r"Nameserver:\s*(.+)\s*",
    "status": r"\nStatus:\s?(.+)",
}

ZZ["lv"] = {
    "extend": "ru",
    "creation_date": r"Registered:\s*(.+)\n",
    "updated_date": r"Changed:\s*(.+)\n",
    "status": r"Status:\s?(.+)",
}

ZZ["me"] = {
    # lines have \r
    "extend": "biz",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiry Date:\s?(.+)",
    "updated_date": None,  # some entries have no date string but not always
    "name_servers": r"Name Server:\s*(\S+)\r?\n",
    "status": r"Domain Status:\s?(.+)",
}

ZZ["ml"] = {
    "extend": "com",
    "domain_name": r"Domain name:\s*([^(i|\n)]+)",
    "registrar": r"(?<=Owner contact:\s)[\s\S]*?Organization:(.*)",
    "registrant_country": r"(?<=Owner contact:\s)[\s\S]*?Country:(.*)",
    "registrant": r"(?<=Owner contact:\s)[\s\S]*?Name:(.*)",
    "creation_date": r"Domain registered: *(.+)",
    "expiration_date": r"Record will expire on: *(.+)",
    "name_servers": r"Domain Nameservers:\s*(.+)\n\s*(.+)\n",
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

ZZ["mobi"] = {
    "extend": "com",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
    "updated_date": r"\nUpdated Date:\s?(.+)",
}

ZZ["mx"] = {
    "extend": None,
    "domain_name": r"Domain Name:\s?(.+)",
    "creation_date": r"Created On:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "updated_date": r"Last Updated On:\s?(.+)",
    "registrar": r"Registrar:\s?(.+)",
    # "registrant": r"Registrant:\n\s*(.+)",
    "name_servers": r"\sDNS:\s*(.+)",
    "registrant_country": None,
    "status": None,
}

ZZ["name"] = {
    "extend": "com",
    "status": r"Domain Status:\s?(.+)",
}

# New-Caledonia (French Territory)
ZZ["nc"] = {
    "extend": "fr",
    "domain_name": r"Domain\s*:\s(.+)",
    "registrar": r"Registrar\s*:\s(.+)",
    "registrant": r"Registrant name\s*:\s(.+)",
    "registrant_country": None,
    "creation_date": r"Created on\s*:\s(.*)",
    "expiration_date": r"Expires on\s*:\s(.*)",
    "updated_date": r"Last updated on\s*:\s(.*)",
    "name_servers": r"Domain server [0-9]{1,}\s*:\s(.*)",
    "status": None,
}

ZZ["net"] = {
    "extend": "com",
}

ZZ["nl"] = {
    "extend": "com",
    "expiration_date": None,
    "registrant_country": None,
    "domain_name": r"Domain name:\s?(.+)",
    "name_servers": (
        r"""(?x:
            Domain\ nameservers:\s+(\S+)\r?\n # the first
            (?:\s+(\S+)\r?\n)?  # a optional 2th
            (?:\s+(\S+)\r?\n)?  # a optional 3th
            (?:\s+(\S+)\r?\n)?  # a optional 4th
            (?:\s+(\S+)\r?\n)?  # a optional 5th
            # there may be more, best use host -t ns <domain> to get the actual nameservers
        )"""
    ),
    # the format with [A] or [AAAA] is no longer in use
    #    "name_servers": (
    #        r"""(?x:
    #            Domain\ nameservers:[ \t]*\n
    #            (?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n       # ns1.tld.nl [A?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [A?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [AAAA?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [A?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [AAAA?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [A?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [AAAA?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [A?]
    #            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [AAAA?]
    #            # Don't check for final LF; there might be even more records..
    #        )"""
    #    ),
    "reseller": r"Reseller:\s?(.+)",
    "abuse_contact": r"Abuse Contact:\s?(.+)",
}

# Norway
ZZ["no"] = {
    "extend": None,
    "domain_name": r"Domain Name\.+:\s?(.+)",
    "registrar": r"Registrar Handle\.+:\s?(.+)",
    "registrant": None,
    "registrant_country": None,
    "creation_date": r"Created:\s?(.+)",
    "expiration_date": None,
    "updated_date": r"Last Updated:\s?(.+)",
    "name_servers": r"Name Server Handle\.+:\s*(.+)\s*",
    "status": None,
    "emails": None,
}

ZZ["nu"] = {
    "extend": "se",
}

ZZ["nyc"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

ZZ["nz"] = {
    "extend": None,
    "domain_name": r"domain_name:\s?(.+)",
    "registrar": r"registrar_name:\s?(.+)",
    "registrant": r"registrant_contact_name:\s?(.+)",
    "registrant_country": None,
    "creation_date": r"domain_dateregistered:\s?(.+)",
    "expiration_date": r"domain_datebilleduntil:\s?(.+)",
    "updated_date": r"domain_datelastmodified:\s?(.+)",
    "name_servers": r"ns_name_[0-9]{2}:\s?(.+)",
    "status": r"query_status:\s?(.+)",
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

ZZ["org"] = {
    "extend": "com",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
    "updated_date": r"\nLast Updated On:\s?(.+)",
    "name_servers": r"Name Server:\s?(.+)\s*",
}

ZZ["ovh"] = {
    "extend": "com",
}

ZZ["pe"] = {
    "extend": "com",
    "registrant": r"Registrant Name:\s?(.+)",
    "admin": r"Admin Name:\s?(.+)",
}

ZZ["pharmacy"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"status:\s?(.+)",
}

ZZ["pl"] = {
    # pl has lines ending in multiple line feeds \r and trailing whitespace
    "extend": "uk",
    "registrar": r"\nREGISTRAR:\s*(.+)\n",
    "creation_date": r"\ncreated:\s*(.+)\n",
    "updated_date": r"\nlast modified:\s*(.+)\n",
    "expiration_date": r"\noption expiration date:\s*(.+)\n",
    # ns: match up to 4
    "name_servers": r"nameservers:(?:\s+(\S+)[^\n]*\n)(?:\s+(\S+)[^\n]*\n)?(?:\s+(\S+)[^\n]*\n)?(?:\s+(\S+)[^\n]*\n)?",
    "status": r"\nStatus:\n\s*(.+)",
}

ZZ["pro"] = {
    "extend": "com",
}

ZZ["pt"] = {
    # mboot 2022-11-16
    # from aws frankfurt all ok, looks like network limitations
    # actually it sometimes works, most of the time though we get: connect: Network is unreachable
    # looks like this is now a privateRegistry mboot: 2022-06-10,
    # manual lookup: use the website at whois.dns.pt
    "_server": "whois.dns.pt",
    # "_privateRegistry": True,
    "extend": "com",
    "domain_name": r"Domain:\s?(.+)",
    "registrar": None,
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "updated_date": None,
    # nameservers have trailing info: Name Server: ns1.dnscpanel.com | IPv4:  and IPv6:
    "name_servers": r"Name Server:(?:\s*(\S+)[^\n]*\n)(?:\s*(\S+)[^\n]*\n)?",
    "status": r"Domain Status:\s?(.+)",
}

ZZ["pw"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

ZZ["radio"] = {
    "extend": "com",
    "_server": "whois.nic.radio",
}

ZZ["red"] = {
    "extend": "com",
}

ZZ["ru"] = {
    "extend": "com",
    "domain_name": r"\ndomain:\s*(.+)",
    "creation_date": r"\ncreated:\s*(.+)",
    "expiration_date": r"\npaid-till:\s*(.+)",
    "name_servers": r"\nnserver:\s*(.+)",
    "status": r"\nstate:\s*(.+)",
}

# Rossíyskaya Federátsiya) is the Cyrillic country code top-level domain for the Russian Federation,
# In the Domain Name System it has the ASCII DNS name xn--p1ai.

ZZ["ru.rf"] = {"extend": "ru", "_server": "whois.tcinet.ru"}
ZZ["рф"] = {"extend": "ru", "_server": "whois.tcinet.ru"}
ZZ["xn--p1ai"] = {"extend": "ru", "_server": "whois.tcinet.ru"}

ZZ["sa"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s*(.+\.sa)\s",
    "registrant": r"Registrant:\n*(.+)\n",
    "name_servers": r"Name Servers:\s*(.+)\s*(.+)?",
    "registrant_country": None,
    "registrar": None,
    "creation_date": None,
    "expiration_date": None,
    "updated_date": None,
    "status": None,
    "emails": None,
}

ZZ["sh"] = {
    "extend": "com",
    "registrant": r"\nRegistrant Organization:\s?(.+)",
    "expiration_date": r"\nRegistry Expiry Date:\s*(.+)",
    "status": r"\nDomain Status:\s?(.+)",
}

ZZ["shop"] = {
    "extend": "com",
}

ZZ["se"] = {
    "extend": None,
    "domain_name": r"domain:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant_country": None,
    "creation_date": r"created:\s?(.+)",
    "expiration_date": r"expires:\s?(.+)",
    "updated_date": r"modified:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)",
    "status": r"status:\s?(.+)",
}

# Singapore - Commercial sub-domain
ZZ["com.sg"] = {
    # uses \r nameservers have trailing whitespace
    "extend": None,
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s?(.+)",
    "registrant": r"Registrant:\r?\n\r?\n\s*Name:\s*(.+)\r?\n",
    "registrant_country": None,
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "updated_date": r"Modified Date:\s?(.+)",
    # fix needed after strip(\r) in _2_parse.py in version 0.19
    # "name_servers": r"Name Servers:\r\n(?:\s*(\S+)[ \t\r]*\n)(?:\s*(\S+)[ \t\r]*\n)?(?:\s*(\S+)[ \t\r]*\n)?",
    "name_servers": r"Name Servers:(?:\s+(\S+))(?:\s+(\S+))?(?:\s+(\S+))?(?:\s+([\.\w]+)\s+)?",
    # this seems ok for 2 and 3 ns and does not catch the dnssec: line
    "status": r"Domain Status:\s*(.*)\r?\n",
    # "emails": r"(\S+@\S+)",
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

# Slovakia
ZZ["sk"] = {
    "extend": "com",
    "domain_name": r"Domain:\s?(.+)",
    "creation_date": r"Created:\s?(.+)",
    "expiration_date": r"Valid Until:\s?(.+)",
    "updated_date": r"Updated:\s?(.+)",
    "name_servers": r"Nameserver:\s*(\S+)",  # fix needed after strip(\r) in _2_parse.py in version 0.19
    "registrant": r"Contact:\s?(.+)",
    "registrant_country": r"Country Code:\s?(.+)\nRegistrar:",
}

ZZ["study"] = {
    "extend": "com",
}

ZZ["tel"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

# Thailand - Commercial sub-domain
ZZ["co.th"] = {
    "_server": "whois.thnic.co.th",
    "extend": "com",
    "registrant": r"Domain Holder Organization:\s?(.+)",
    "registrant_country": r"Domain Holder Country:\s?(.+)",
    "creation_date": r"Created date:\s?(.+)",
    "expiration_date": r"Exp date:\s?(.+)",
    "updated_date": r"Updated date:\s?(.+)",
}

ZZ["go.th"] = {
    "extend": "co.th",
}

ZZ["in.th"] = {
    "extend": "co.th",
}

ZZ["ac.th"] = {
    "extend": "co.th",
}

ZZ["tn"] = {
    "extend": "com",
    "domain_name": r"Domain name\.+:(.+)\s*",
    "registrar": r"Registrar\.+:(.+)\s*",
    "registrant": r"Owner Contact\n+Name\.+:\s?(.+)",
    "registrant_country": r"Owner Contact\n(?:.+\n)+Country\.+:\s(.+)",
    "creation_date": r"Creation date\.+:\s?(.+)",
    "expiration_date": None,
    "updated_date": None,
    "name_servers": r"DNS servers\n(?:Name\.+:\s*(\S+)\n)(?:Name\.+:\s*(\S+)\n)?(?:Name\.+:\s*(\S+)\n)?(?:Name\.+:\s*(\S+)\n)?",
    "status": r"Domain status\.+:(.+)",
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

ZZ["tokyo"] = {
    "extend": "com",
    "_server": "whois.nic.tokyo",
}

ZZ["top"] = {
    "extend": "com",
}

ZZ["trade"] = {
    "extend": "amsterdam",
}

ZZ["tv"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

ZZ["tz"] = {
    "domain_name": r"\ndomain:\s*(.+)",
    "registrar": r"\nregistrar:\s?(.+)",
    "registrant": r"\nregistrant:\s*(.+)",
    "registrant_country": None,
    "creation_date": r"\ncreated:\s*(.+)",
    "expiration_date": r"expire:\s?(.+)",
    "updated_date": r"\nchanged:\s*(.+)",
    "status": None,
    "name_servers": r"\nnserver:\s*(.+)",
}

ZZ["ua"] = {
    "extend": "com",
    "domain_name": r"\ndomain:\s*(.+)",
    "registrar": r"\nregistrar:\s*(.+)",
    "registrant_country": r"\ncountry:\s*(.+)",
    "creation_date": r"\ncreated:\s+(.+)",
    "expiration_date": r"\nexpires:\s*(.+)",
    "updated_date": r"\nmodified:\s*(.+)",
    "name_servers": r"\nnserver:\s*(.+)",
    "status": r"\nstatus:\s*(.+)",
}

ZZ["edu.ua"] = {
    "extend": "ua",
    "creation_date": r"\ncreated:\s+0-UANIC\s+(.+)",
}
ZZ["com.ua"] = {"extend": "ua"}
ZZ["net.ua"] = {"extend": "ua"}

ZZ["lviv.ua"] = {"extend": "com"}

ZZ["uk"] = {
    "extend": "com",
    "registrant": r"Registrant:\n\s*(.+)",
    "creation_date": r"Registered on:\s*(.+)",
    "expiration_date": r"Expiry date:\s*(.+)",
    "updated_date": r"Last updated:\s*(.+)",
    "name_servers": r"Name Servers:\s*(\S+)\r?\n(?:\s+(\S+)\r?\n)?(?:\s+(\S+)\r?\n)?(?:\s+(\S+)\r?\n)?",
    "status": r"Registration status:\n\s*(.+)",
}

ZZ["us"] = {"extend": "name"}

ZZ["uz"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
    "name_servers": r"Domain servers in listed order:(?:\n\s+(\S+))(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?\n\n",
    # sometimes 'not.defined is returned as a nameserver (e.g. google.uz)
}

ZZ["vip"] = {
    "_server": "whois.nic.vip",
    "extend": "com",
    "updated_date": None,
}

ZZ["wiki"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

ZZ["win"] = {
    "extend": "com",
}

ZZ["work"] = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
}

ZZ["xin"] = {
    "extend": "com",
    "_server": "whois.nic.xin",
}

ZZ["za"] = {
    "extend": "com",
}

ZZ["web.za"] = {"extend": "za", "_server": "web-whois.registry.net.za"}
ZZ["org.za"] = {"extend": "za", "_server": "org-whois.registry.net.za"}
ZZ["net.za"] = {"extend": "za", "_server": "net-whois.registry.net.za"}
ZZ["co.za"] = {"extend": "za", "_server": "coza-whois.registry.net.za"}

ZZ["gy"] = {"extend": "com"}

# Multiple initialization
ZZ["ca"] = {"extend": "bank"}
ZZ["rw"] = {"extend": "bank"}
ZZ["mu"] = {"extend": "bank"}
ZZ["mu"] = {"extend": "bank"}

# Registry operator: donuts.domains
# WHOIS server: whois.donuts.co
ZZ["_donuts"] = {
    "extend": "com",
    "_server": "whois.donuts.co",
    "registrant": r"Registrant Organization:\s?(.+)",
    "status": r"Domain Status:\s?(.+)",
}

ZZ["academy"] = {"extend": "_donuts"}
ZZ["accountants"] = {"extend": "_donuts"}
ZZ["actor"] = {"extend": "_donuts"}
ZZ["agency"] = {"extend": "_donuts"}
ZZ["airforce"] = {"extend": "_donuts"}
ZZ["apartments"] = {"extend": "_donuts"}
ZZ["army"] = {"extend": "_donuts"}
ZZ["associates"] = {"extend": "_donuts"}
ZZ["attorney"] = {"extend": "_donuts"}
ZZ["auction"] = {"extend": "_donuts"}
ZZ["band"] = {"extend": "_donuts"}
ZZ["bargains"] = {"extend": "_donuts"}
ZZ["bike"] = {"extend": "_donuts"}
ZZ["bingo"] = {"extend": "_donuts"}
ZZ["boutique"] = {"extend": "_donuts"}
ZZ["builders"] = {"extend": "_donuts"}
ZZ["business"] = {"extend": "_donuts"}
ZZ["cab"] = {"extend": "_donuts"}
ZZ["cafe"] = {"extend": "_donuts"}
ZZ["camera"] = {"extend": "_donuts"}
ZZ["camp"] = {"extend": "_donuts"}
ZZ["capital"] = {"extend": "_donuts"}
ZZ["cards"] = {"extend": "_donuts"}
ZZ["careers"] = {"extend": "_donuts"}
ZZ["care"] = {"extend": "_donuts"}
ZZ["cash"] = {"extend": "_donuts"}
ZZ["casino"] = {"extend": "_donuts"}
ZZ["catering"] = {"extend": "_donuts"}
ZZ["center"] = {"extend": "_donuts"}
ZZ["charity"] = {"extend": "_donuts"}
ZZ["chat"] = {"extend": "_donuts"}
ZZ["cheap"] = {"extend": "_donuts"}
ZZ["church"] = {"extend": "_donuts"}
ZZ["city"] = {"extend": "_donuts"}
ZZ["claims"] = {"extend": "_donuts"}
ZZ["cleaning"] = {"extend": "_donuts"}
ZZ["clinic"] = {"extend": "_donuts"}
ZZ["clothing"] = {"extend": "_donuts"}
ZZ["coach"] = {"extend": "_donuts"}
ZZ["codes"] = {"extend": "_donuts"}
ZZ["coffee"] = {"extend": "_donuts"}
ZZ["community"] = {"extend": "_donuts"}
ZZ["company"] = {"extend": "_donuts"}
ZZ["computer"] = {"extend": "_donuts"}
ZZ["condos"] = {"extend": "_donuts"}
ZZ["construction"] = {"extend": "_donuts"}
ZZ["consulting"] = {"extend": "_donuts"}
ZZ["contact"] = {"extend": "_donuts"}
ZZ["contractors"] = {"extend": "_donuts"}
ZZ["cool"] = {"extend": "_donuts"}
ZZ["coupons"] = {"extend": "_donuts"}
ZZ["creditcard"] = {"extend": "_donuts"}
ZZ["credit"] = {"extend": "_donuts"}
ZZ["cruises"] = {"extend": "_donuts"}
ZZ["dance"] = {"extend": "_donuts"}
ZZ["dating"] = {"extend": "_donuts"}
ZZ["deals"] = {"extend": "_donuts"}
ZZ["degree"] = {"extend": "_donuts"}
ZZ["delivery"] = {"extend": "_donuts"}
ZZ["democrat"] = {"extend": "_donuts"}
ZZ["dental"] = {"extend": "_donuts"}
ZZ["dentist"] = {"extend": "_donuts"}
ZZ["diamonds"] = {"extend": "_donuts"}
ZZ["digital"] = {"extend": "_donuts"}
ZZ["direct"] = {"extend": "_donuts"}
ZZ["directory"] = {"extend": "_donuts"}
ZZ["discount"] = {"extend": "_donuts"}
ZZ["doctor"] = {"extend": "_donuts"}
ZZ["dog"] = {"extend": "_donuts"}
ZZ["domains"] = {"extend": "_donuts"}
ZZ["education"] = {"extend": "_donuts"}
ZZ["email"] = {"extend": "_donuts"}
ZZ["energy"] = {"extend": "_donuts"}
ZZ["engineer"] = {"extend": "_donuts"}
ZZ["engineering"] = {"extend": "_donuts"}
ZZ["enterprises"] = {"extend": "_donuts"}
ZZ["equipment"] = {"extend": "_donuts"}
ZZ["estate"] = {"extend": "_donuts"}
ZZ["events"] = {"extend": "_donuts"}
ZZ["exchange"] = {"extend": "_donuts"}
ZZ["expert"] = {"extend": "_donuts"}
ZZ["exposed"] = {"extend": "_donuts"}
ZZ["express"] = {"extend": "_donuts"}
ZZ["fail"] = {"extend": "_donuts"}
ZZ["family"] = {"extend": "_donuts"}
ZZ["fan"] = {"extend": "_donuts"}
ZZ["farm"] = {"extend": "_donuts"}
ZZ["finance"] = {"extend": "_donuts"}
ZZ["financial"] = {"extend": "_donuts"}
ZZ["fish"] = {"extend": "_donuts"}
ZZ["fitness"] = {"extend": "_donuts"}
ZZ["flights"] = {"extend": "_donuts"}
ZZ["florist"] = {"extend": "_donuts"}
ZZ["football"] = {"extend": "_donuts"}
ZZ["forsale"] = {"extend": "_donuts"}
ZZ["foundation"] = {"extend": "_donuts"}
ZZ["fund"] = {"extend": "_donuts"}
ZZ["furniture"] = {"extend": "_donuts"}
ZZ["futbol"] = {"extend": "_donuts"}
ZZ["fyi"] = {"extend": "_donuts"}
ZZ["gallery"] = {"extend": "_donuts"}
ZZ["games"] = {"extend": "_donuts"}
ZZ["gifts"] = {"extend": "_donuts"}
ZZ["gives"] = {"extend": "_donuts"}
ZZ["glass"] = {"extend": "_donuts"}
ZZ["gmbh"] = {"extend": "_donuts"}
ZZ["gold"] = {"extend": "_donuts"}
ZZ["golf"] = {"extend": "_donuts"}
ZZ["graphics"] = {"extend": "_donuts"}
ZZ["gratis"] = {"extend": "_donuts"}
ZZ["gripe"] = {"extend": "_donuts"}
ZZ["group"] = {"extend": "_donuts"}
ZZ["guide"] = {"extend": "_donuts"}
ZZ["guru"] = {"extend": "_donuts"}
ZZ["haus"] = {"extend": "_donuts"}
ZZ["healthcare"] = {"extend": "_donuts"}
ZZ["hockey"] = {"extend": "_donuts"}
ZZ["holdings"] = {"extend": "_donuts"}
ZZ["holiday"] = {"extend": "_donuts"}
ZZ["hospital"] = {"extend": "_donuts"}
ZZ["house"] = {"extend": "_donuts"}
ZZ["immobilien"] = {"extend": "_donuts"}
ZZ["immo"] = {"extend": "_donuts"}
ZZ["industries"] = {"extend": "_donuts"}
ZZ["institute"] = {"extend": "_donuts"}
ZZ["insure"] = {"extend": "_donuts"}
ZZ["international"] = {"extend": "_donuts"}
ZZ["investments"] = {"extend": "_donuts"}
ZZ["irish"] = {"extend": "_donuts"}
ZZ["jetzt"] = {"extend": "_donuts"}
ZZ["jewelry"] = {"extend": "_donuts"}
ZZ["kaufen"] = {"extend": "_donuts"}
ZZ["kitchen"] = {"extend": "_donuts"}
ZZ["land"] = {"extend": "_donuts"}
ZZ["lawyer"] = {"extend": "_donuts"}
ZZ["lease"] = {"extend": "_donuts"}
ZZ["legal"] = {"extend": "_donuts"}
ZZ["life"] = {"extend": "_donuts"}
ZZ["lighting"] = {"extend": "_donuts"}
ZZ["limited"] = {"extend": "_donuts"}
ZZ["limo"] = {"extend": "_donuts"}
ZZ["live"] = {"extend": "_donuts"}
ZZ["loans"] = {"extend": "_donuts"}
ZZ["ltd"] = {"extend": "_donuts"}
ZZ["maison"] = {"extend": "_donuts"}
ZZ["management"] = {"extend": "_donuts"}
ZZ["market"] = {"extend": "_donuts"}
ZZ["marketing"] = {"extend": "_donuts"}
ZZ["mba"] = {"extend": "_donuts"}
ZZ["media"] = {"extend": "_donuts"}
ZZ["memorial"] = {"extend": "_donuts"}
ZZ["moda"] = {"extend": "_donuts"}
ZZ["money"] = {"extend": "_donuts"}
ZZ["mortgage"] = {"extend": "_donuts"}
ZZ["movie"] = {"extend": "_donuts"}
ZZ["navy"] = {"extend": "_donuts"}
ZZ["network"] = {"extend": "_donuts"}
ZZ["news"] = {"extend": "_donuts"}
ZZ["ninja"] = {"extend": "_donuts"}
ZZ["partners"] = {"extend": "_donuts"}
ZZ["parts"] = {"extend": "_donuts"}
ZZ["pet"] = {"extend": "_donuts"}
ZZ["photography"] = {"extend": "_donuts"}
ZZ["photos"] = {"extend": "_donuts"}
ZZ["pictures"] = {"extend": "_donuts"}
ZZ["pizza"] = {"extend": "_donuts"}
ZZ["place"] = {"extend": "_donuts"}
ZZ["plumbing"] = {"extend": "_donuts"}
ZZ["plus"] = {"extend": "_donuts"}
ZZ["productions"] = {"extend": "_donuts"}
ZZ["properties"] = {"extend": "_donuts"}
ZZ["pub"] = {"extend": "_donuts"}
ZZ["recipes"] = {"extend": "_donuts"}
ZZ["rehab"] = {"extend": "_donuts"}
ZZ["reise"] = {"extend": "_donuts"}
ZZ["reisen"] = {"extend": "_donuts"}
ZZ["rentals"] = {"extend": "_donuts"}
ZZ["repair"] = {"extend": "_donuts"}
ZZ["report"] = {"extend": "_donuts"}
ZZ["republican"] = {"extend": "_donuts"}
ZZ["restaurant"] = {"extend": "_donuts"}
ZZ["reviews"] = {"extend": "_donuts"}
ZZ["rip"] = {"extend": "_donuts"}
ZZ["rocks"] = {"extend": "_donuts"}
ZZ["run"] = {"extend": "_donuts"}
ZZ["sale"] = {"extend": "_donuts"}
ZZ["salon"] = {"extend": "_donuts"}
ZZ["sarl"] = {"extend": "_donuts"}
ZZ["school"] = {"extend": "_donuts"}
ZZ["schule"] = {"extend": "_donuts"}
ZZ["services"] = {"extend": "_donuts"}
ZZ["shoes"] = {"extend": "_donuts"}
ZZ["shopping"] = {"extend": "_donuts"}
ZZ["show"] = {"extend": "_donuts"}
ZZ["singles"] = {"extend": "_donuts"}
ZZ["soccer"] = {"extend": "_donuts"}
ZZ["social"] = {"extend": "_donuts"}
ZZ["software"] = {"extend": "_donuts"}
ZZ["solar"] = {"extend": "_donuts"}
ZZ["solutions"] = {"extend": "_donuts"}
ZZ["studio"] = {"extend": "_donuts"}
ZZ["style"] = {"extend": "_donuts"}
ZZ["supplies"] = {"extend": "_donuts"}
ZZ["supply"] = {"extend": "_donuts"}
ZZ["support"] = {"extend": "_donuts"}
ZZ["surgery"] = {"extend": "_donuts"}
ZZ["systems"] = {"extend": "_donuts"}
ZZ["tax"] = {"extend": "_donuts"}
ZZ["taxi"] = {"extend": "_donuts"}
ZZ["team"] = {"extend": "_donuts"}
ZZ["technology"] = {"extend": "_donuts"}
ZZ["tennis"] = {"extend": "_donuts"}
ZZ["theater"] = {"extend": "_donuts"}
ZZ["tienda"] = {"extend": "_donuts"}
ZZ["tips"] = {"extend": "_donuts"}
ZZ["tires"] = {"extend": "_donuts"}
ZZ["today"] = {"extend": "_donuts"}
ZZ["tools"] = {"extend": "_donuts"}
ZZ["tours"] = {"extend": "_donuts"}
ZZ["town"] = {"extend": "_donuts"}
ZZ["toys"] = {"extend": "_donuts"}
ZZ["training"] = {"extend": "_donuts"}
ZZ["travel"] = {"extend": "_donuts"}
ZZ["university"] = {"extend": "_donuts"}
ZZ["vacations"] = {"extend": "_donuts"}
ZZ["ventures"] = {"extend": "_donuts"}
ZZ["vet"] = {"extend": "_donuts"}
ZZ["viajes"] = {"extend": "_donuts"}
ZZ["video"] = {"extend": "_donuts"}
ZZ["villas"] = {"extend": "_donuts"}
ZZ["vin"] = {"extend": "_donuts"}
ZZ["vision"] = {"extend": "_donuts"}
ZZ["voyage"] = {"extend": "_donuts"}
ZZ["watch"] = {"extend": "_donuts"}
ZZ["wine"] = {"extend": "_donuts"}
ZZ["works"] = {"extend": "_donuts"}
ZZ["world"] = {"extend": "_donuts"}
ZZ["wtf"] = {"extend": "_donuts"}
ZZ["zone"] = {"extend": "_donuts"}

# Registry operator: CentralNic
# WHOIS server: whois.centralnic.com
ZZ["_centralnic"] = {
    "extend": "com",
    "_server": "whois.centralnic.com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Domain Status:\s?(.+)",
}

ZZ["art"] = {"extend": "_centralnic"}
ZZ["auto"] = {"extend": "_centralnic"}
ZZ["autos"] = {"extend": "_centralnic"}
ZZ["baby"] = {"extend": "_centralnic"}
ZZ["bar"] = {"extend": "_centralnic"}
ZZ["beauty"] = {"extend": "_centralnic"}
ZZ["best"] = {"extend": "_centralnic"}
ZZ["blog"] = {"extend": "_centralnic"}
ZZ["boats"] = {"extend": "_centralnic"}
ZZ["bond"] = {"extend": "_centralnic"}
ZZ["build"] = {"extend": "_centralnic"}
ZZ["cam"] = {"extend": "_centralnic"}
ZZ["car"] = {"extend": "_centralnic"}
ZZ["cars"] = {"extend": "_centralnic"}
ZZ["ceo"] = {"extend": "_centralnic"}
ZZ["cfd"] = {"extend": "_centralnic"}
ZZ["college"] = {"extend": "_centralnic"}
ZZ["coop"] = {"extend": "_centralnic"}
ZZ["cyou"] = {"extend": "_centralnic"}
ZZ["dealer"] = {"extend": "_centralnic"}
ZZ["desi"] = {"extend": "_centralnic"}
ZZ["fans"] = {"extend": "_centralnic"}
ZZ["feedback"] = {"extend": "_centralnic"}
ZZ["forum"] = {"extend": "_centralnic"}
ZZ["frl"] = {"extend": "_centralnic"}
ZZ["fun"] = {"extend": "_centralnic"}
ZZ["gent"] = {"extend": "_centralnic"}
ZZ["hair"] = {"extend": "_centralnic"}
ZZ["homes"] = {"extend": "_centralnic"}
ZZ["host"] = {"extend": "_centralnic"}
ZZ["icu"] = {"extend": "_centralnic"}
ZZ["inc"] = {"extend": "_centralnic"}
ZZ["kred"] = {"extend": "_centralnic"}
ZZ["london"] = {"extend": "_centralnic"}
ZZ["luxury"] = {"extend": "_centralnic"}
ZZ["makeup"] = {"extend": "_centralnic"}
ZZ["monster"] = {"extend": "_centralnic"}
ZZ["motorcycles"] = {"extend": "_centralnic"}
ZZ["online"] = {"extend": "_centralnic"}
ZZ["ooo"] = {"extend": "_centralnic"}
ZZ["press"] = {"extend": "_centralnic"}
ZZ["protection"] = {"extend": "_centralnic"}
ZZ["qpon"] = {"extend": "_centralnic"}
ZZ["quest"] = {"extend": "_centralnic"}
ZZ["reit"] = {"extend": "_centralnic"}
ZZ["rent"] = {"extend": "_centralnic"}
ZZ["rest"] = {"extend": "_centralnic"}
ZZ["saarland"] = {"extend": "_centralnic"}
ZZ["sbs"] = {"extend": "_centralnic"}
ZZ["security"] = {"extend": "_centralnic"}
ZZ["site"] = {"extend": "_centralnic"}
ZZ["skin"] = {"extend": "_centralnic"}
ZZ["space"] = {"extend": "_centralnic"}
ZZ["storage"] = {"extend": "_centralnic"}
ZZ["store"] = {"extend": "_centralnic"}
ZZ["tech"] = {"extend": "_centralnic"}
ZZ["theatre"] = {"extend": "_centralnic"}
ZZ["tickets"] = {"extend": "_centralnic"}
ZZ["uno"] = {"extend": "_centralnic"}
ZZ["website"] = {"extend": "_centralnic"}
ZZ["xyz"] = {"extend": "_centralnic"}
ZZ["yachts"] = {"extend": "_centralnic"}
ZZ["zuerich"] = {"extend": "_centralnic"}

# mboot added start
# note i extract the whois server for each toplevel domain using: https://github.com/jophy/iana_tld_list
# of which i am a contributer

ZZ["ac"] = {
    "extend": None,
    "domain_name": r"Domain Name:\s+(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "status": r"Domain Status:\s(.+)",
    "name_servers": r"Name Server:\s+(\S+)",
    "registrant_country": r"Registrant Country:\s*(.*)\r?\n",
    "updated_date": r"Updated Date:\s+(.+)",
    "creation_date": r"Creation Date:\s+(.+)",
    "expiration_date": r"Registry Expiry Date:\s+(.+)",
}

ZZ["ae"] = {
    "extend": "ar",
    "domain_name": r"Domain Name:\s+(.+)",
    "registrar": r"Registrar Name:\s+(.+)",
    "status": r"Status:\s(.+)",
    "name_servers": r"Name Server:\s+(\S+)",  # host -t ns gives back more, but whois output only has 2
    "registrant_country": None,
    "creation_date": None,
    "expiration_date": None,
    "updated_date": None,
}

ZZ["aero"] = {
    "extend": "ac",
    "_server": "whois.aero",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}


ZZ["af"] = {
    "extend": "ac",
}

ZZ["ag"] = {
    "extend": "ac",
}

ZZ["bet"] = {
    "extend": "ac",
    "_server": "whois.nic.bet",
}

ZZ["bg"] = {
    "extend": None,
    "_server": "whois.register.bg",
    "domain_name": r"DOMAIN\s+NAME:\s+(.+)",
    "status": r"registration\s+status:\s(.+)",
    "name_servers": r"NAME SERVER INFORMATION:\n(?:(.+)\n)(?:(.+)\n)?(?:(.+)\n)?(?:(.+)\n)?",
    "creation_date": None,
    "expiration_date": None,
    "updated_date": None,
    "registrar": None,
    "registrant_country": None,
}

ZZ["bid"] = {
    "extend": "ac",
    "_server": "whois.nic.bid",
}

# Benin
# WHOIS server: whois.nic.bj
# by: https://github.com/LickosA

ZZ["bj"] = {
    "_server": "whois.nic.bj",
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
    "name_servers": r"Name Server:\s+(\S+)\n",
}

ZZ["buzz"] = {
    "extend": "amsterdam",
}

ZZ["casa"] = {
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

ZZ["cd"] = {
    "extend": "ac",
    "_server": "whois.nic.cd",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

ZZ["cf"] = {
    "extend": None,
    "domain_name": None,
    "name_servers": r"Domain Nameservers:\n(?:(.+)\n)(?:(.+)\n)?(?:(.+)\n)?(?:(.+)\n)?",
    "registrar": r"Record maintained by:\s+(.+)",
    "creation_date": r"Domain registered:\s?(.+)",
    "expiration_date": r"Record will expire:\s?(.+)",
    "updated_date": None,
    "registrant_country": None,
    # very restrictive, after a few queries it will refuse with try again later
    "_slowdown": 5,
}

ZZ["design"] = {
    "extend": "ac",
}

ZZ["eus"] = {
    "extend": "ac",
}

ZZ["ge"] = {
    "_server": "whois.nic.ge",
    "extend": "ac",
    "updated_date": None,
}

ZZ["gq"] = {
    "extend": "ml",
    "_server": "whois.domino.gq",
}

ZZ["la"] = {
    "extend": "com",
}

ZZ["lol"] = {
    "extend": "amsterdam",
}

ZZ["love"] = {
    "extend": "ac",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

ZZ["ly"] = {
    "extend": "ac",
    "_server": "whois.nic.ly",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

ZZ["com.ly"] = {
    "extend": "ly",  # host -t ns <domain> often has more nameservers then output of whois
}

ZZ["ma"] = {
    "extend": "ac",
    "_server": "whois.registre.ma",
    "registrar": r"Sponsoring Registrar:\s*(.+)",
}

ZZ["mg"] = {
    "extend": "ac",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

ZZ["moe"] = {
    "extend": "ac",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

ZZ["ng"] = {
    "_server": "whois.nic.net.ng",
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

ZZ["ong"] = {
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

ZZ["pics"] = {
    "extend": "ac",
}

ZZ["re"] = {
    "extend": "ac",
    "registrant_country": None,
    "domain_name": r"domain:\s+(.+)",
    "registrar": r"registrar:\s+(.+)",
    "name_servers": r"nserver:\s+(.+)",
    "status": r"status:\s(.+)",
    "creation_date": r"created:\s+(.+)",
    "expiration_date": r"Expiry Date:\s+(.+)",
    "updated_date": r"last-update:\s+(.*)",
    "registrant_country": None,
}

ZZ["ro"] = {
    "extend": None,
    "domain_name": r"\s+Domain name:\s+(.+)",
    "registrar": r"\s+Registrar:\s+(.+)",
    "creation_date": r"\s+Registered On:\s+(.+)",
    "expiration_date": r"\s+Expires On:\s+(.+)",
    "status": r"\s+Domain Status:\s(.+)",
    "name_servers": r"\s+NameServer:\s+(.+)",
    "registrant_country": None,
    "updated_date": None,
}

ZZ["rs"] = {
    "domain_name": r"Domain name:\s+(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "status": r"Domain status:\s(.+)",
    "creation_date": r"Registration date:\s+(.+)",
    "expiration_date": r"Expiration date:\s+(.+)",
    "updated_date": r"Modification date:\s+(.+)",
    "name_servers": r"DNS:\s+(.+)",
    "registrant_country": None,
}

# singapore
ZZ["sg"] = {
    "_server": "whois.sgnic.sg",
    "registrar": r"Registrar:\s+(.+)",
    "domain_name": r"\s+Domain name:\s+(.+)",
    "creation_date": r"\s+Creation Date:\s+(.+)",
    "expiration_date": r"\s+Expiration Date:\s+(.+)",
    "updated_date": r"\s+Modified Date:\s+(.+)",
    "status": r"\s+Domain Status:\s(.+)",
    "registrant_country": None,
    "name_servers": r"Name Servers:(?:\n[ \t]+(\S+)[^\n]*)(?:\n[ \t]+(\S+)[^\n]*)?(?:\n[ \t]+(\S+)[^\n]*)?(?:\n[ \t]+(\S+)[^\n]*)?",
    # make sure the dnssec is not matched
}

ZZ["srl"] = {
    "_server": "whois.afilias-srs.net",
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

ZZ["su"] = {
    "extend": "ru",
}

ZZ["td"] = {
    "_server": "whois.nic.td",
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

ZZ["tw"] = {
    "extend": None,
    "domain_name": r"Domain Name:\s+(.+)",
    "creation_date": r"\s+Record created on\s+(.+)",
    "expiration_date": r"\s+Record expires on\s+(.+)",
    "status": r"\s+Domain Status:\s+(.+)",
    "registrar": r"Registration\s+Service\s+Provider:\s+(.+)",
    "updated_date": None,
    "registrant_country": None,
    "name_servers": r"Domain servers in listed order:\s*(\S+)[ \t]*\r?\n(?:\s+(\S+)[ \t]*\r?\n)?(?:\s+(\S+)[ \t]*\r?\n)?(?:\s+(\S+)[ \t]*\r?\n)?",
}

ZZ["com.tw"] = {
    "extend": "tw",
}

ZZ["ug"] = {
    "_server": "whois.co.ug",
    "domain_name": r"Domain name:\s+(.+)",
    "creation_date": r"Registered On:\s+(.+)",
    "expiration_date": r"Expires On:\s+(.+)",
    "status": r"Status:\s+(.+)",
    "name_servers": r"Nameserver:\s+(.+)",
    "registrant_country": r"Registrant Country:\s+(.+)",
    "updated_date": r"Renewed On:\s+(.+)",
    "registrar": None,
}

ZZ["co.ug"] = {
    "extend": "ug",
}

ZZ["ca.ug"] = {
    "extend": "ug",
}

ZZ["ws"] = {
    "extend": None,
    "domain_name": r"Domain Name:\s+(.+)",
    "creation_date": r"Creation Date:\s+(.+)",
    "expiration_date": r"Registrar Registration Expiration Date:\s+(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "status": r"Domain Status:\s(.+)",
    "name_servers": r"Name Server:\s+(.+)",
    "registrant_country": None,
}

ZZ["re"] = {
    "domain_name": r"domain:\s+(.+)",
    "status": r"status:\s+(.+)",
    "registrar": r"registrar:\s+(.+)",
    "name_servers": r"nserver:\s+(.+)",
    "creation_date": r"created:\s+(.+)",
    "expiration_date": r"Expiry Date:\s+(.+)",
    "updated_date": r"last-update:\s+(.+)",
    "registrant_country": None,
}

ZZ["bo"] = {
    "domain_name": r"\s*NOMBRE DE DOMINIO:\s+(.+)",
    "registrant_country": r"País:\s+(.+)",
    "creation_date": r"Fecha de activación:\s+(.+)",
    "expiration_date": r"Fecha de corte:\s+(.+)",
    "extend": None,
    "registrar": None,
    "status": None,
    "name_servers": None,  # bo has no nameservers, use host -t ns <domain>
    "updated_date": None,
}

ZZ["com.bo"] = {"extend": "bo"}

ZZ["hr"] = {
    "domain_name": r"Domain Name:\s+(.+)",
    "name_servers": r"Name Server:\s+(.+)",
    "creation_date": r"Creation Date:\s+(.+)",
    "updated_date": r"Updated Date:\s+(.+)",
    "status": None,
    "registrar": None,
    "expiration_date": None,
    "registrant_country": None,
}

# 2022-06-20: mboot
# com_ec = {}
# gob_ec = {}

# Registry operator: Zodiac Wang Limited
# WHOIS server: whois.gtld.knet.cn
ZZ["_gtldKnet"] = {
    "extend": "com",
    "_server": "whois.gtld.knet.cn",
    "admin": r"Admin\s*Name:\s+(.+)",
}

ZZ["wang"] = {"extend": "_gtldKnet"}

# we DONT have xn--45q11c 八卦 (gossip) fix
ZZ["八卦"] = {"extend": "_gtldKnet"}
ZZ["xn--45q11c"] = {"extend": "_gtldKnet"}

# we DONT have xn--czru2d 商城 (mall) fix
ZZ["商城"] = {"extend": "_gtldKnet"}
ZZ["xn--czru2d"] = {"extend": "_gtldKnet"}

# we DONT have xn--hxt814e 网店 (webshop) fix
ZZ["网店"] = {"extend": "_gtldKnet"}
ZZ["xn--hxt814e"] = {"extend": "_gtldKnet"}

ZZ["accountant"] = {"extend": "com", "_server": "whois.nic.accountant"}
ZZ["cricket"] = {"extend": "com", "_server": "whois.nic.cricket"}
ZZ["date"] = {"extend": "com", "_server": "whois.nic.date"}
ZZ["faith"] = {"extend": "com", "_server": "whois.nic.faith"}
ZZ["hiphop"] = {"extend": "com", "_server": "whois.nic.hiphop"}
ZZ["loan"] = {"extend": "com", "_server": "whois.nic.loan"}
ZZ["party"] = {"extend": "com", "_server": "whois.nic.party"}
ZZ["racing"] = {"extend": "com", "_server": "whois.nic.racing"}
ZZ["ren"] = {"extend": "com", "_server": "whois.nic.ren"}
ZZ["review"] = {"extend": "com", "_server": "whois.nic.review"}
ZZ["science"] = {"extend": "com", "_server": "whois.nic.science"}
ZZ["webcam"] = {"extend": "com", "_server": "whois.nic.webcam"}
ZZ["fashion"] = {"extend": "com", "_server": "whois.nic.fashion"}

# Registry operator: UNR Corp.
# WHOIS server: whois.uniregistry.net
ZZ["_uniregistry"] = {
    "extend": "com",
    "_server": "whois.uniregistry.net",
}

ZZ["help"] = {"extend": "_uniregistry"}
ZZ["photo"] = {"extend": "_uniregistry"}
ZZ["sexy"] = {"extend": "_uniregistry"}
ZZ["gift"] = {"extend": "_uniregistry"}
ZZ["tattoo"] = {"extend": "_uniregistry"}
ZZ["property"] = {"extend": "_uniregistry"}
ZZ["juegos"] = {"extend": "_uniregistry"}
ZZ["hosting"] = {"extend": "_uniregistry"}
ZZ["guitars"] = {"extend": "_uniregistry"}
ZZ["flowers"] = {"extend": "_uniregistry"}
ZZ["diet"] = {"extend": "_uniregistry"}
ZZ["christmas"] = {"extend": "_uniregistry"}
ZZ["blackfriday"] = {"extend": "_uniregistry"}
ZZ["audio"] = {"extend": "_uniregistry"}

# Registry operator: TLD REGISTRY LIMITED.
# WHOIS server: whois.teleinfo.cn
ZZ["_teleinfo"] = {
    "extend": "com",
    "_server": "whois.teleinfo.cn",
}

# we DONT have xn--fiq228c5hs 中文网 (website) fix
ZZ["中文网"] = {"extend": "_teleinfo"}
ZZ["xn--fiq228c5hs"] = {"extend": "_teleinfo"}
# we DONT have xn--3ds443g 在线 (online) fix
ZZ["在线"] = {"extend": "_teleinfo"}
ZZ["xn--3ds443g"] = {"extend": "_teleinfo"}


# RESTRICTED: now known as PrivateRegistry
# restricted domains never answer or never show information sufficient for parsing
# some only show if the domain is free, most allow using a website but some have no web
# but you may have to prove you are not a robot and limits apply also on the website
# some actually dont have a working whois server
# details can be found at:
# (https://www.iana.org/domains/root/db/<tld>.html)

ZZ["_privateReg"] = {"_privateRegistry": True}

ZZ["al"] = {"extend": "_privateReg"}
ZZ["az"] = {"extend": "_privateReg"}
ZZ["ba"] = {"extend": "_privateReg"}
ZZ["ch"] = {"extend": "_privateReg"}
ZZ["cv"] = {"extend": "_privateReg"}  # Cape Verde
ZZ["cw"] = {"extend": "_privateReg"}
ZZ["es"] = {"extend": "_privateReg"}
ZZ["ga"] = {"extend": "_privateReg"}
ZZ["gr"] = {"extend": "_privateReg"}
ZZ["hu"] = {"extend": "_privateReg"}
ZZ["li"] = {"extend": "_privateReg"}
ZZ["mp"] = {"extend": "_privateReg"}
ZZ["my"] = {"extend": "_privateReg"}
ZZ["pk"] = {"extend": "_privateReg"}
ZZ["py"] = {"extend": "_privateReg"}  # Paraguay:https://www.iana.org/domains/root/db/py.html
ZZ["com.py"] = {"extend": "_privateReg"}
ZZ["sr"] = {"extend": "_privateReg"}
ZZ["ke"] = {"extend": "_privateReg"}  # Kenia
ZZ["co.ke"] = {"extend": "_privateReg"}

# https://www.iana.org/domains/root/db/td.html
# td = {"extend": "_privateReg"} # Chad (French: Tchad) made available for use in 1997.

ZZ["tk"] = {"extend": "_privateReg"}
ZZ["to"] = {"extend": "_privateReg"}  #
ZZ["uy"] = {"extend": "_privateReg"}  # Uruguay
ZZ["va"] = {"extend": "_privateReg"}  # This TLD has no whois server.
ZZ["vu"] = {"extend": "_privateReg"}  # all dates 1970 , no furter relevant info
ZZ["vn"] = {"extend": "_privateReg"}
#
ZZ["zw"] = {"extend": "_privateReg"}  # Zimbabwe ; # This TLD has no whois server
ZZ["com.zw"] = {"extend": "zw"}
ZZ["org.zw"] = {"extend": "zw"}

# Nepal
ZZ["np"] = {
    "extend": "_privateReg"
}  # This TLD has no whois server, but you can access the whois database at https://www.mos.com.np/
ZZ["com.np"] = {"extend": "np"}

# Ecuador
ZZ["ec"] = {"extend": "_privateReg"}
ZZ["com.ec"] = {"extend": "ec"}
ZZ["gob.ec"] = {"extend": "ec"}

# https://umbrella.cisco.com/blog/on-the-trail-of-malicious-dynamic-dns-domains
ZZ["hopto.org"] = {"extend": "_privateReg"}  # dynamic dns without any whois
ZZ["duckdns.org"] = {"extend": "_privateReg"}  # dynamic dns without any whois
# changeip_com = {"extend": "_privateReg"}  # dynamic dns without any whois
# dnsdynamic_org = {"extend": "_privateReg"}  # dynamic dns without any whois
ZZ["noip.com"] = {"extend": "_privateReg"}  # dynamic dns without any whois
ZZ["noip.org"] = {"extend": "_privateReg"}  # dynamic dns without any whois
# freedns_afraid_org = {"extend": "_privateReg"}  # dynamic dns without any whois
# dyndns_com = {"extend": "_privateReg"}  # dynamic dns without any whois
# sitelutions_com = {"extend": "_privateReg"}  # dynamic dns without any whois
# 3322_org = {"extend": "_privateReg"}  # dynamic dns without any whois

# https://en.wikipedia.org/wiki/.onion, a "official" fake domain
ZZ["onion"] = {"extend": "_privateReg"}

# backend registry for domain names ending in GG, JE, and AS.
# lines may have \r actually before \n , updated all 3 domains return all nameservers
ZZ["gg"] = {
    "domain_name": r"Domain:\s*\n\s+(.+)",
    "status": r"Domain Status:\s*\n\s+(.+)",
    "registrar": r"Registrar:\s*\n\s+(.+)",
    "name_servers": r"Name servers:(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?(?:\n\s+(\S+))?\n",
    "creation_date": r"Relevant dates:\s*\n\s+Registered on(.+)",
    "expiration_date": None,
    "updated_date": None,
    "registrant_country": None,
}

ZZ["as"] = {"extend": "gg"}
ZZ["je"] = {"extend": "gg"}

ZZ["sn"] = {
    "_server": "whois.nic.sn",
    "domain_name": r"Nom de domaine:\s+(.+)",
    "status": r"Statut:\s+(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "name_servers": r"Serveur de noms:\s*(.+)",
    "creation_date": r"Date de création:\s+(.+)",
    "expiration_date": r"Date d'expiration:\s+(.+)",
    "updated_date": r"Dernière modification:\s+(.+)",
    "registrant_country": None,
}

ZZ["si"] = {
    "domain_name": r"domain:\s+(.+)",
    "status": r"status:\s+(.+)",
    "registrar": r"registrar:\s+(.+)",
    "name_servers": r"nameserver:\s*(.+)",
    "creation_date": r"created:\s+(.+)",
    "expiration_date": r"expire:\s+(.+)",
    "updated_date": None,
    "registrant_country": None,
}

ZZ["do"] = {"extend": "_privateReg"}
ZZ["com.do"] = {"extend": "_privateReg"}
ZZ["cx"] = {"extend": "com"}
ZZ["dz"] = {"extend": "_privateReg"}
ZZ["gd"] = {"extend": "com"}
ZZ["mn"] = {"extend": "com"}
ZZ["tl"] = {"extend": "com"}
ZZ["gay"] = {"extend": "com", "_server": "whois.nic.gay"}
ZZ["tt"] = {"extend": "_privateReg"}
ZZ["mo"] = {
    "extend": "com",
    "creation_date": r"created on\s+(.+)",
    "expiration_date": r"expires on\s+(.+)",
    "name_servers": r"Domain name servers:\s*\-+(?:\s*(\S+)\n)(?:\s*(\S+)\n)?(?:\s*(\S+)\n)?(?:\s*(\S+)\n)?",
}
ZZ["com.mo"] = {"extend": "mo"}
ZZ["st"] = {
    # .ST domains can now be registered with many different competing registrars. and hence different formats
    # >>> line appears quite early, valid info after would have been suppressed with the ^>>> cleanup rule: switched off
    "extend": "com",
    "registrant_country": r"registrant-country:\s+(\S+)",
    "registrant": r"registrant-organi(?:s|z)ation:\s*(.+)\r?\n",
}

ZZ["so"] = {"extend": "com"}
ZZ["nrw"] = {"extend": "com"}
ZZ["lat"] = {"extend": "com"}
ZZ["realestate"] = {"_server": "whois.nic.realestate", "extend": "com"}
ZZ["ph"] = {"extend": "_privateReg"}
ZZ["com.ph"] = {"extend": "ph"}
ZZ["org.ph"] = {"extend": "ph"}
ZZ["net.ph"] = {"extend": "ph"}
ZZ["zm"] = {"extend": "com"}
ZZ["sy"] = {"extend": "_privateReg", "_server": "whois.tld.sy"}
ZZ["tr"] = {"extend": "_privateReg"}
ZZ["onl"] = {"extend": "com"}
ZZ["blue"] = {"extend": "com"}
ZZ["garden"] = {"extend": "com", "_server": "whois.nic.garden"}
ZZ["promo"] = {"extend": "com", "_server": "whois.nic.promo"}

ZZ["pyc"] = {"extend": "com"}

ZZ["mn"] = {"extend": "com", "_server": "whois.nic.mn"}

ZZ["africa"] = {"extend": "com", "_server": "whois.nic.africa"}

ZZ["green"] = {"extend": "com"}

ZZ["mk"] = {
    "extend": None,
    "_server": "whois.marnet.mk",
    "domain_name": r"domain:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant": r"registrant:\s?(.+)",
    "registrant_country": r"Registrant Country:\s?(.+)",
    "creation_date": r"registered:\s?(.+)",
    "expiration_date": r"expire:\s?(.+)",
    "updated_date": r"changed:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)\s*",
    "status": r"Status:\s?(.+)",
    # the trailing domain must have minimal 2 parts firstname.lastname@fld.tld
    # it may actually have more then 4 levels
    # to match the dot in firstname.lastname we must use \.
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

ZZ["observer"] = {"extend": "com", "_server": "whois.nic.observer"}
ZZ["one"] = {"extend": "com", "_server": "whois.nic.one"}
ZZ["page"] = {"extend": "com", "_server": "whois.nic.google"}

ZZ["bf"] = {
    "extend": "com",
    "_server": "whois.nic.bf",
    "registrant": r"Registrant Name:\s?(.+)",
}
ZZ["bz"] = {"extend": "_privateReg"}

ZZ["si"] = {
    "extend": None,
    "_server": "whois.register.si",
    "domain_name": r"domain:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant": r"registrant:\s?(.+)",
    "registrant_country": r"Registrant Country:\s?(.+)",
    "creation_date": r"created:\s?(.+)",
    "expiration_date": r"expire:\s?(.+)",
    "updated_date": r"changed:\s?(.+)",
    "name_servers": r"nameserver:\s*(.+)\s*",
    "status": r"Status:\s?(.+)",
    # the trailing domain must have minimal 2 parts firstname.lastname@fld.tld
    # it may actually have more then 4 levels
    # to match the dot in firstname.lastname we must use \.
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

ZZ["sx"] = {"extend": "com", "_server": "whois.sx"}

ZZ["tc"] = {
    "extend": "com",
    "_server": "whois.nic.tc",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Sponsoring Registrar:\s?(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "name_servers": r"Name Server:\s*(.+)\s*",
    "status": r"Domain Status:\s?(.+)",
}

ZZ["wf"] = {
    "extend": "com",
    "_server": "whois.nic.wf",
    "domain_name": r"domain:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant": r"registrant:\s?(.+)",
    "registrant_country": r"Registrant Country:\s?(.+)",
    "creation_date": r"created:\s?(.+)",
    "expiration_date": r"Expiry Date:\s?(.+)",
    "updated_date": r"last-update:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)\s*",
    "status": r"\nstatus:\s?(.+)",
}

ZZ["lk"] = {"extend": "_privateReg"}  # Sri Lanka, whois.nic.lk exists but does not answer
ZZ["eg"] = {"extend": "_privateReg"}  # Egipt
ZZ["com.eg"] = {"extend": "_privateReg"}  # Egipt

ZZ["mo"] = {
    "extend": "com",
    "_server": "whois.monic.mo",
    "name_servers": r"Domain name servers:\s+-+\s+(\S+)\n(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?",
    "creation_date": r"Record created on (.+)",
    "expiration_date": r"Record expires on (.+)",
}

ZZ["ph"] = {"extend": "_privateReg"}

ZZ["vc"] = {"extend": "com"}
ZZ["cm"] = {"extend": "com"}

# russian speaking community
ZZ["xn--p1acf"] = {"extend": "ru", "_server": "whois.nic.xn--p1acf"}
ZZ["РУС"] = {"extend": "ru", "_server": "whois.nic.xn--p1acf"}
ZZ["рус"] = {"extend": "ru", "_server": "whois.nic.xn--p1acf"}
