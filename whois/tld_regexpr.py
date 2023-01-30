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
    "domain_name": r"Domain Name\s*:\s*(.+)",
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
ZZ["com.cn"] = {
    "extend": "cn",
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
ZZ["xyz"] = {"extend": "_centralnic", "_server": "whois.nic.xyz"}
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
# https://www.rfc-editor.org/rfc/rfc7686.html
# .onion names are used to provide access to end to end encrypted, secure, anonymized services;
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

ZZ["vig"] = {"extend": "com", "_server": "whois.afilias-srs.net"}

# autodetect via compare_known_tld.py via IANA tld list and https://github.com/jophy/iana_tld_list
ZZ["aarp"] = {"_server": "whois.nic.aarp", "extend": "com"}
ZZ["abbvie"] = {"_server": "whois.nic.abbvie", "extend": "com"}
ZZ["abc"] = {"_server": "whois.nic.abc", "extend": "com"}
ZZ["abogado"] = {"_server": "whois.nic.abogado", "extend": "com"}
ZZ["abudhabi"] = {"_server": "whois.nic.abudhabi", "extend": "com"}
ZZ["aco"] = {"_server": "whois.nic.aco", "extend": "com"}
ZZ["adult"] = {"_server": "whois.nic.adult", "extend": "com"}
ZZ["aeg"] = {"_server": "whois.nic.aeg", "extend": "com"}
ZZ["afl"] = {"_server": "whois.nic.afl", "extend": "com"}
ZZ["airbus"] = {"_server": "whois.nic.airbus", "extend": "com"}
ZZ["airtel"] = {"_server": "whois.nic.airtel", "extend": "com"}
ZZ["alibaba"] = {"_server": "whois.nic.alibaba", "extend": "com"}
ZZ["alipay"] = {"_server": "whois.nic.alipay", "extend": "com"}
ZZ["allfinanz"] = {"_server": "whois.nic.allfinanz", "extend": "com"}
ZZ["ally"] = {"_server": "whois.nic.ally", "extend": "com"}
ZZ["alsace"] = {"_server": "whois.nic.alsace", "extend": "com"}
ZZ["alstom"] = {"_server": "whois.nic.alstom", "extend": "com"}
ZZ["amazon"] = {"_server": "whois.nic.amazon", "extend": "com"}
ZZ["americanfamily"] = {"_server": "whois.nic.americanfamily", "extend": "com"}
ZZ["anz"] = {"_server": "whois.nic.anz", "extend": "com"}
ZZ["aol"] = {"_server": "whois.nic.aol", "extend": "com"}
ZZ["aquarelle"] = {"_server": "whois.nic.aquarelle", "extend": "com"}
ZZ["arab"] = {"_server": "whois.nic.arab", "extend": "com"}
ZZ["archi"] = {"_server": "whois.nic.archi", "extend": "com"}
ZZ["arte"] = {"_server": "whois.nic.arte", "extend": "com"}
ZZ["asda"] = {"_server": "whois.nic.asda", "extend": "com"}
ZZ["audible"] = {"_server": "whois.nic.audible", "extend": "com"}
ZZ["auspost"] = {"_server": "whois.nic.auspost", "extend": "com"}
ZZ["author"] = {"_server": "whois.nic.author", "extend": "com"}
ZZ["aws"] = {"_server": "whois.nic.aws", "extend": "com"}
ZZ["barcelona"] = {"_server": "whois.nic.barcelona", "extend": "com"}
ZZ["barclaycard"] = {"_server": "whois.nic.barclaycard", "extend": "com"}
ZZ["barclays"] = {"_server": "whois.nic.barclays", "extend": "com"}
ZZ["barefoot"] = {"_server": "whois.nic.barefoot", "extend": "com"}
ZZ["basketball"] = {"_server": "whois.nic.basketball", "extend": "com"}
ZZ["bauhaus"] = {"_server": "whois.nic.bauhaus", "extend": "com"}
ZZ["bayern"] = {"_server": "whois.nic.bayern", "extend": "com"}
ZZ["bbc"] = {"_server": "whois.nic.bbc", "extend": "com"}
ZZ["bbt"] = {"_server": "whois.nic.bbt", "extend": "com"}
ZZ["bbva"] = {"_server": "whois.nic.bbva", "extend": "com"}
ZZ["bcg"] = {"_server": "whois.nic.bcg", "extend": "com"}
ZZ["bcn"] = {"_server": "whois.nic.bcn", "extend": "com"}
ZZ["beer"] = {"_server": "whois.nic.beer", "extend": "com"}
ZZ["bentley"] = {"_server": "whois.nic.bentley", "extend": "com"}
ZZ["berlin"] = {"_server": "whois.nic.berlin", "extend": "com"}
ZZ["bestbuy"] = {"_server": "whois.nic.bestbuy", "extend": "com"}
ZZ["bi"] = {"_server": "whois1.nic.bi", "extend": "com"}
ZZ["bible"] = {"_server": "whois.nic.bible", "extend": "com"}
ZZ["bio"] = {"_server": "whois.nic.bio", "extend": "com"}
ZZ["black"] = {"_server": "whois.nic.black", "extend": "com"}
ZZ["blockbuster"] = {"_server": "whois.nic.blockbuster", "extend": "com"}
ZZ["bms"] = {"_server": "whois.nic.bms", "extend": "com"}
ZZ["bmw"] = {"_server": "whois.nic.bmw", "extend": "com"}
ZZ["bofa"] = {"_server": "whois.nic.bofa", "extend": "com"}
ZZ["boo"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["book"] = {"_server": "whois.nic.book", "extend": "com"}
ZZ["bosch"] = {"_server": "whois.nic.bosch", "extend": "com"}
ZZ["bostik"] = {"_server": "whois.nic.bostik", "extend": "com"}
ZZ["boston"] = {"_server": "whois.nic.boston", "extend": "com"}
ZZ["bot"] = {"_server": "whois.nic.bot", "extend": "com"}
ZZ["box"] = {"_server": "whois.nic.box", "extend": "com"}
ZZ["bradesco"] = {"_server": "whois.nic.bradesco", "extend": "com"}
ZZ["bridgestone"] = {"_server": "whois.nic.bridgestone", "extend": "com"}
ZZ["broadway"] = {"_server": "whois.nic.broadway", "extend": "com"}
ZZ["broker"] = {"_server": "whois.nic.broker", "extend": "com"}
ZZ["brother"] = {"_server": "whois.nic.brother", "extend": "com"}
ZZ["brussels"] = {"_server": "whois.nic.brussels", "extend": "com"}
ZZ["buy"] = {"_server": "whois.nic.buy", "extend": "com"}
ZZ["call"] = {"_server": "whois.nic.call", "extend": "com"}
ZZ["canon"] = {"_server": "whois.nic.canon", "extend": "com"}
ZZ["capetown"] = {"_server": "whois.nic.capetown", "extend": "com"}
ZZ["capitalone"] = {"_server": "whois.nic.capitalone", "extend": "com"}
ZZ["career"] = {"_server": "whois.nic.career", "extend": "com"}
ZZ["case"] = {"_server": "whois.nic.case", "extend": "com"}
ZZ["catholic"] = {"_server": "whois.nic.catholic", "extend": "com"}
ZZ["cba"] = {"_server": "whois.nic.cba", "extend": "com"}
ZZ["cfa"] = {"_server": "whois.nic.cfa", "extend": "com"}
ZZ["chanel"] = {"_server": "whois.nic.chanel", "extend": "com"}
ZZ["channel"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["chintai"] = {"_server": "whois.nic.chintai", "extend": "com"}
ZZ["ci"] = {"_server": "whois.nic.ci", "extend": "com"}
ZZ["circle"] = {"_server": "whois.nic.circle", "extend": "com"}
ZZ["cityeats"] = {"_server": "whois.nic.cityeats", "extend": "com"}
ZZ["clinique"] = {"_server": "whois.nic.clinique", "extend": "com"}
ZZ["clubmed"] = {"_server": "whois.nic.clubmed", "extend": "com"}
ZZ["cologne"] = {"_server": "whois.ryce-rsp.com", "extend": "com"}
ZZ["comcast"] = {"_server": "whois.nic.comcast", "extend": "com"}
ZZ["commbank"] = {"_server": "whois.nic.commbank", "extend": "com"}
ZZ["compare"] = {"_server": "whois.nic.compare", "extend": "com"}
ZZ["comsec"] = {"_server": "whois.nic.comsec", "extend": "com"}
ZZ["cooking"] = {"_server": "whois.nic.cooking", "extend": "com"}
ZZ["cookingchannel"] = {"_server": "whois.nic.cookingchannel", "extend": "com"}
ZZ["corsica"] = {"_server": "whois.nic.corsica", "extend": "com"}
ZZ["country"] = {"_server": "whois.nic.country", "extend": "com"}
ZZ["cpa"] = {"_server": "whois.nic.cpa", "extend": "com"}
ZZ["cruise"] = {"_server": "whois.nic.cruise", "extend": "com"}
ZZ["cuisinella"] = {"_server": "whois.nic.cuisinella", "extend": "com"}
ZZ["cymru"] = {"_server": "whois.nic.cymru", "extend": "com"}
ZZ["data"] = {"_server": "whois.nic.data", "extend": "com"}
ZZ["day"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["dds"] = {"_server": "whois.nic.dds", "extend": "com"}
ZZ["deal"] = {"_server": "whois.nic.deal", "extend": "com"}
ZZ["deloitte"] = {"_server": "whois.nic.deloitte", "extend": "com"}
ZZ["delta"] = {"_server": "whois.nic.delta", "extend": "com"}
ZZ["dish"] = {"_server": "whois.nic.dish", "extend": "com"}
ZZ["diy"] = {"_server": "whois.nic.diy", "extend": "com"}
ZZ["dm"] = {"_server": "whois.dmdomains.dm", "extend": "com"}
ZZ["dnp"] = {"_server": "whois.nic.dnp", "extend": "com"}
ZZ["dot"] = {"_server": "whois.nic.dot", "extend": "com"}
ZZ["dtv"] = {"_server": "whois.nic.dtv", "extend": "com"}
ZZ["dubai"] = {"_server": "whois.nic.dubai", "extend": "com"}
ZZ["dunlop"] = {"_server": "whois.nic.dunlop", "extend": "com"}
ZZ["durban"] = {"_server": "whois.nic.durban", "extend": "com"}
ZZ["dvag"] = {"_server": "whois.nic.dvag", "extend": "com"}
ZZ["dvr"] = {"_server": "whois.nic.dvr", "extend": "com"}
ZZ["earth"] = {"_server": "whois.nic.earth", "extend": "com"}
ZZ["eco"] = {"_server": "whois.nic.eco", "extend": "com"}
ZZ["epson"] = {"_server": "whois.nic.epson", "extend": "com"}
ZZ["ericsson"] = {"_server": "whois.nic.ericsson", "extend": "com"}
ZZ["erni"] = {"_server": "whois.nic.erni", "extend": "com"}
ZZ["eurovision"] = {"_server": "whois.nic.eurovision", "extend": "com"}
ZZ["fairwinds"] = {"_server": "whois.nic.fairwinds", "extend": "com"}
ZZ["fast"] = {"_server": "whois.nic.fast", "extend": "com"}
ZZ["fedex"] = {"_server": "whois.nic.fedex", "extend": "com"}
ZZ["ferrari"] = {"_server": "whois.nic.ferrari", "extend": "com"}
ZZ["fidelity"] = {"_server": "whois.nic.fidelity", "extend": "com"}
ZZ["film"] = {"_server": "whois.nic.film", "extend": "com"}
ZZ["fire"] = {"_server": "whois.nic.fire", "extend": "com"}
ZZ["firestone"] = {"_server": "whois.nic.firestone", "extend": "com"}
ZZ["firmdale"] = {"_server": "whois.nic.firmdale", "extend": "com"}
ZZ["fishing"] = {"_server": "whois.nic.fishing", "extend": "com"}
ZZ["foodnetwork"] = {"_server": "whois.nic.foodnetwork", "extend": "com"}
ZZ["forex"] = {"_server": "whois.nic.forex", "extend": "com"}
ZZ["fox"] = {"_server": "whois.nic.fox", "extend": "com"}
ZZ["free"] = {"_server": "whois.nic.free", "extend": "com"}
ZZ["fresenius"] = {"_server": "whois.nic.fresenius", "extend": "com"}
ZZ["frogans"] = {"_server": "whois.nic.frogans", "extend": "com"}
ZZ["frontdoor"] = {"_server": "whois.nic.frontdoor", "extend": "com"}
ZZ["gal"] = {"_server": "whois.nic.gal", "extend": "com"}
ZZ["gallo"] = {"_server": "whois.nic.gallo", "extend": "com"}
ZZ["gallup"] = {"_server": "whois.nic.gallup", "extend": "com"}
ZZ["gdn"] = {"_server": "whois.nic.gdn", "extend": "com"}
ZZ["gea"] = {"_server": "whois.nic.gea", "extend": "com"}
ZZ["genting"] = {"_server": "whois.nic.genting", "extend": "com"}
ZZ["george"] = {"_server": "whois.nic.george", "extend": "com"}
ZZ["ggee"] = {"_server": "whois.nic.ggee", "extend": "com"}
ZZ["giving"] = {"_server": "whois.nic.giving", "extend": "com"}
ZZ["gl"] = {"_server": "whois.nic.gl", "extend": "com"}
ZZ["gmo"] = {"_server": "whois.nic.gmo", "extend": "com"}
ZZ["gmx"] = {"_server": "whois.nic.gmx", "extend": "com"}
ZZ["godaddy"] = {"_server": "whois.nic.godaddy", "extend": "com"}
ZZ["goldpoint"] = {"_server": "whois.nic.goldpoint", "extend": "com"}
ZZ["goodyear"] = {"_server": "whois.nic.goodyear", "extend": "com"}
ZZ["google"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["gop"] = {"_server": "whois.nic.gop", "extend": "com"}
ZZ["got"] = {"_server": "whois.nic.got", "extend": "com"}
ZZ["gs"] = {"_server": "whois.nic.gs", "extend": "com"}
ZZ["gucci"] = {"_server": "whois.nic.gucci", "extend": "com"}
ZZ["hamburg"] = {"_server": "whois.nic.hamburg", "extend": "com"}
ZZ["hdfc"] = {"_server": "whois.nic.hdfc", "extend": "com"}
ZZ["hdfcbank"] = {"_server": "whois.nic.hdfcbank", "extend": "com"}
ZZ["helsinki"] = {"_server": "whois.nic.helsinki", "extend": "com"}
ZZ["hgtv"] = {"_server": "whois.nic.hgtv", "extend": "com"}
ZZ["hiv"] = {"_server": "whois.nic.hiv", "extend": "com"}
ZZ["hkt"] = {"_server": "whois.nic.hkt", "extend": "com"}
ZZ["homedepot"] = {"_server": "whois.nic.homedepot", "extend": "com"}
ZZ["honda"] = {"_server": "whois.nic.honda", "extend": "com"}
ZZ["horse"] = {"_server": "whois.nic.horse", "extend": "com"}
ZZ["hot"] = {"_server": "whois.nic.hot", "extend": "com"}
ZZ["how"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["ht"] = {"_server": "whois.nic.ht", "extend": "com"}
ZZ["hughes"] = {"_server": "whois.nic.hughes", "extend": "com"}
ZZ["hyundai"] = {"_server": "whois.nic.hyundai", "extend": "com"}
ZZ["ibm"] = {"_server": "whois.nic.ibm", "extend": "com"}
ZZ["icbc"] = {"_server": "whois.nic.icbc", "extend": "com"}
ZZ["ice"] = {"_server": "whois.nic.ice", "extend": "com"}
ZZ["ifm"] = {"_server": "whois.nic.ifm", "extend": "com"}
ZZ["ikano"] = {"_server": "whois.nic.ikano", "extend": "com"}
ZZ["imdb"] = {"_server": "whois.nic.imdb", "extend": "com"}
ZZ["insurance"] = {"_server": "whois.nic.insurance", "extend": "com"}
ZZ["ist"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["istanbul"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["jaguar"] = {"_server": "whois.nic.jaguar", "extend": "com"}
ZZ["java"] = {"_server": "whois.nic.java", "extend": "com"}
ZZ["jio"] = {"_server": "whois.nic.jio", "extend": "com"}
ZZ["jobs"] = {"_server": "whois.nic.jobs", "extend": "com"}
ZZ["joburg"] = {"_server": "whois.nic.joburg", "extend": "com"}
ZZ["jot"] = {"_server": "whois.nic.jot", "extend": "com"}
ZZ["joy"] = {"_server": "whois.nic.joy", "extend": "com"}
ZZ["juniper"] = {"_server": "whois.nic.juniper", "extend": "com"}
ZZ["kddi"] = {"_server": "whois.nic.kddi", "extend": "com"}
ZZ["kerryhotels"] = {"_server": "whois.nic.kerryhotels", "extend": "com"}
ZZ["kerrylogistics"] = {"_server": "whois.nic.kerrylogistics", "extend": "com"}
ZZ["kerryproperties"] = {"_server": "whois.nic.kerryproperties", "extend": "com"}
ZZ["kfh"] = {"_server": "whois.nic.kfh", "extend": "com"}
ZZ["kia"] = {"_server": "whois.nic.kia", "extend": "com"}
ZZ["kids"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["kim"] = {"_server": "whois.nic.kim", "extend": "com"}
ZZ["kindle"] = {"_server": "whois.nic.kindle", "extend": "com"}
ZZ["koeln"] = {"_server": "whois.ryce-rsp.com", "extend": "com"}
ZZ["komatsu"] = {"_server": "whois.nic.komatsu", "extend": "com"}
ZZ["kosher"] = {"_server": "whois.nic.kosher", "extend": "com"}
ZZ["krd"] = {"_server": "whois.nic.krd", "extend": "com"}
ZZ["kuokgroup"] = {"_server": "whois.nic.kuokgroup", "extend": "com"}
ZZ["ky"] = {"_server": "whois.kyregistry.ky", "extend": "com"}
ZZ["kyoto"] = {"_server": "whois.nic.kyoto", "extend": "com"}
ZZ["lacaixa"] = {"_server": "whois.nic.lacaixa", "extend": "com"}
ZZ["lamer"] = {"_server": "whois.nic.lamer", "extend": "com"}
ZZ["lancaster"] = {"_server": "whois.nic.lancaster", "extend": "com"}
ZZ["landrover"] = {"_server": "whois.nic.landrover", "extend": "com"}
ZZ["latino"] = {"_server": "whois.nic.latino", "extend": "com"}
ZZ["latrobe"] = {"_server": "whois.nic.latrobe", "extend": "com"}
ZZ["law"] = {"_server": "whois.nic.law", "extend": "com"}
ZZ["lb"] = {"_server": "whois.lbdr.org.lb", "extend": "com"}
ZZ["lds"] = {"_server": "whois.nic.lds", "extend": "com"}
ZZ["leclerc"] = {"_server": "whois.nic.leclerc", "extend": "com"}
ZZ["lefrak"] = {"_server": "whois.nic.lefrak", "extend": "com"}
ZZ["lego"] = {"_server": "whois.nic.lego", "extend": "com"}
ZZ["lexus"] = {"_server": "whois.nic.lexus", "extend": "com"}
ZZ["lgbt"] = {"_server": "whois.nic.lgbt", "extend": "com"}
ZZ["lidl"] = {"_server": "whois.nic.lidl", "extend": "com"}
ZZ["lifestyle"] = {"_server": "whois.nic.lifestyle", "extend": "com"}
ZZ["like"] = {"_server": "whois.nic.like", "extend": "com"}
ZZ["linde"] = {"_server": "whois.nic.linde", "extend": "com"}
ZZ["lipsy"] = {"_server": "whois.nic.lipsy", "extend": "com"}
ZZ["llc"] = {"_server": "whois.nic.llc", "extend": "com"}
ZZ["llp"] = {"_server": "whois.nic.llp", "extend": "com"}
ZZ["locker"] = {"_server": "whois.nic.locker", "extend": "com"}
ZZ["locus"] = {"_server": "whois.nic.locus", "extend": "com"}
ZZ["lotte"] = {"_server": "whois.nic.lotte", "extend": "com"}
ZZ["lotto"] = {"_server": "whois.nic.lotto", "extend": "com"}
ZZ["lpl"] = {"_server": "whois.nic.lpl", "extend": "com"}
ZZ["ltda"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["lundbeck"] = {"_server": "whois.nic.lundbeck", "extend": "com"}
ZZ["luxe"] = {"_server": "whois.nic.luxe", "extend": "com"}
ZZ["macys"] = {"_server": "whois.nic.macys", "extend": "com"}
ZZ["madrid"] = {"_server": "whois.nic.madrid", "extend": "com"}
ZZ["man"] = {"_server": "whois.nic.man", "extend": "com"}
ZZ["mango"] = {"_server": "whois.nic.mango", "extend": "com"}
ZZ["markets"] = {"_server": "whois.nic.markets", "extend": "com"}
ZZ["maserati"] = {"_server": "whois.nic.maserati", "extend": "com"}
ZZ["mckinsey"] = {"_server": "whois.nic.mckinsey", "extend": "com"}
ZZ["med"] = {"_server": "whois.nic.med", "extend": "com"}
ZZ["melbourne"] = {"_server": "whois.nic.melbourne", "extend": "com"}
ZZ["men"] = {"_server": "whois.nic.men", "extend": "com"}
ZZ["menu"] = {"_server": "whois.nic.menu", "extend": "com"}
ZZ["miami"] = {"_server": "whois.nic.miami", "extend": "com"}
ZZ["mini"] = {"_server": "whois.nic.mini", "extend": "com"}
ZZ["mls"] = {"_server": "whois.nic.mls", "extend": "com"}
ZZ["mma"] = {"_server": "whois.nic.mma", "extend": "com"}
ZZ["mobile"] = {"_server": "whois.nic.mobile", "extend": "com"}
ZZ["moi"] = {"_server": "whois.nic.moi", "extend": "com"}
ZZ["mom"] = {"_server": "whois.nic.mom", "extend": "com"}
ZZ["monash"] = {"_server": "whois.nic.monash", "extend": "com"}
ZZ["mormon"] = {"_server": "whois.nic.mormon", "extend": "com"}
ZZ["moscow"] = {"_server": "whois.nic.moscow", "extend": "com"}
ZZ["mr"] = {"_server": "whois.nic.mr", "extend": "com"}
ZZ["ms"] = {"_server": "whois.nic.ms", "extend": "com"}
ZZ["mtn"] = {"_server": "whois.nic.mtn", "extend": "com"}
ZZ["mtr"] = {"_server": "whois.nic.mtr", "extend": "com"}
ZZ["museum"] = {"_server": "whois.nic.museum", "extend": "com"}
ZZ["music"] = {"_server": "whois.nic.music", "extend": "com"}
ZZ["mz"] = {"_server": "whois.nic.mz", "extend": "com"}
ZZ["na"] = {"_server": "whois.na-nic.com.na", "extend": "com"}
ZZ["nab"] = {"_server": "whois.nic.nab", "extend": "com"}
ZZ["nagoya"] = {"_server": "whois.nic.nagoya", "extend": "com"}
ZZ["nec"] = {"_server": "whois.nic.nec", "extend": "com"}
ZZ["netbank"] = {"_server": "whois.nic.netbank", "extend": "com"}
ZZ["new"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["next"] = {"_server": "whois.nic.next", "extend": "com"}
ZZ["nextdirect"] = {"_server": "whois.nic.nextdirect", "extend": "com"}
ZZ["nf"] = {"_server": "whois.nic.nf", "extend": "com"}
ZZ["ngo"] = {"_server": "whois.nic.ngo", "extend": "com"}
ZZ["nhk"] = {"_server": "whois.nic.nhk", "extend": "com"}
ZZ["nico"] = {"_server": "whois.nic.nico", "extend": "com"}
ZZ["nikon"] = {"_server": "whois.nic.nikon", "extend": "com"}
ZZ["nissay"] = {"_server": "whois.nic.nissay", "extend": "com"}
ZZ["norton"] = {"_server": "whois.nic.norton", "extend": "com"}
ZZ["now"] = {"_server": "whois.nic.now", "extend": "com"}
ZZ["nowruz"] = {"_server": "whois.nic.nowruz", "extend": "com"}
ZZ["nowtv"] = {"_server": "whois.nic.nowtv", "extend": "com"}
ZZ["obi"] = {"_server": "whois.nic.obi", "extend": "com"}
ZZ["olayan"] = {"_server": "whois.nic.olayan", "extend": "com"}
ZZ["olayangroup"] = {"_server": "whois.nic.olayangroup", "extend": "com"}
ZZ["ollo"] = {"_server": "whois.nic.ollo", "extend": "com"}
ZZ["om"] = {"_server": "whois.registry.om", "extend": "com"}
ZZ["omega"] = {"_server": "whois.nic.omega", "extend": "com"}
ZZ["oracle"] = {"_server": "whois.nic.oracle", "extend": "com"}
ZZ["orange"] = {"_server": "whois.nic.orange", "extend": "com"}
ZZ["organic"] = {"_server": "whois.nic.organic", "extend": "com"}
ZZ["origins"] = {"_server": "whois.nic.origins", "extend": "com"}
ZZ["osaka"] = {"_server": "whois.nic.osaka", "extend": "com"}
ZZ["otsuka"] = {"_server": "whois.nic.otsuka", "extend": "com"}
ZZ["ott"] = {"_server": "whois.nic.ott", "extend": "com"}
ZZ["paris"] = {"_server": "whois.nic.paris", "extend": "com"}
ZZ["pars"] = {"_server": "whois.nic.pars", "extend": "com"}
ZZ["pay"] = {"_server": "whois.nic.pay", "extend": "com"}
ZZ["pccw"] = {"_server": "whois.nic.pccw", "extend": "com"}
ZZ["philips"] = {"_server": "whois.nic.philips", "extend": "com"}
ZZ["phone"] = {"_server": "whois.nic.phone", "extend": "com"}
ZZ["physio"] = {"_server": "whois.nic.physio", "extend": "com"}
ZZ["pid"] = {"_server": "whois.nic.pid", "extend": "com"}
ZZ["pin"] = {"_server": "whois.nic.pin", "extend": "com"}
ZZ["pink"] = {"_server": "whois.nic.pink", "extend": "com"}
ZZ["pioneer"] = {"_server": "whois.nic.pioneer", "extend": "com"}
ZZ["playstation"] = {"_server": "whois.nic.playstation", "extend": "com"}
ZZ["pnc"] = {"_server": "whois.nic.pnc", "extend": "com"}
ZZ["pohl"] = {"_server": "whois.nic.pohl", "extend": "com"}
ZZ["poker"] = {"_server": "whois.nic.poker", "extend": "com"}
ZZ["politie"] = {"_server": "whois.nic.politie", "extend": "com"}
ZZ["porn"] = {"_server": "whois.nic.porn", "extend": "com"}
ZZ["pr"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["prime"] = {"_server": "whois.nic.prime", "extend": "com"}
ZZ["qa"] = {"_server": "whois.registry.qa", "extend": "com"}
ZZ["quebec"] = {"_server": "whois.nic.quebec", "extend": "com"}
ZZ["read"] = {"_server": "whois.nic.read", "extend": "com"}
ZZ["realty"] = {"_server": "whois.nic.realty", "extend": "com"}
ZZ["redstone"] = {"_server": "whois.nic.redstone", "extend": "com"}
ZZ["reliance"] = {"_server": "whois.nic.reliance", "extend": "com"}
ZZ["rexroth"] = {"_server": "whois.nic.rexroth", "extend": "com"}
ZZ["rich"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["richardli"] = {"_server": "whois.nic.richardli", "extend": "com"}
ZZ["ricoh"] = {"_server": "whois.nic.ricoh", "extend": "com"}
ZZ["ril"] = {"_server": "whois.nic.ril", "extend": "com"}
ZZ["rodeo"] = {"_server": "whois.nic.rodeo", "extend": "com"}
ZZ["room"] = {"_server": "whois.nic.room", "extend": "com"}
ZZ["rsvp"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["rugby"] = {"_server": "whois.nic.rugby", "extend": "com"}
ZZ["ruhr"] = {"_server": "whois.nic.ruhr", "extend": "com"}
ZZ["rwe"] = {"_server": "whois.nic.rwe", "extend": "com"}
ZZ["safe"] = {"_server": "whois.nic.safe", "extend": "com"}
ZZ["safety"] = {"_server": "whois.nic.safety", "extend": "com"}
ZZ["samsclub"] = {"_server": "whois.nic.samsclub", "extend": "com"}
ZZ["samsung"] = {"_server": "whois.nic.samsung", "extend": "com"}
ZZ["sandvik"] = {"_server": "whois.nic.sandvik", "extend": "com"}
ZZ["sandvikcoromant"] = {"_server": "whois.nic.sandvikcoromant", "extend": "com"}
ZZ["sanofi"] = {"_server": "whois.nic.sanofi", "extend": "com"}
ZZ["sap"] = {"_server": "whois.nic.sap", "extend": "com"}
ZZ["save"] = {"_server": "whois.nic.save", "extend": "com"}
ZZ["saxo"] = {"_server": "whois.nic.saxo", "extend": "com"}
ZZ["sbi"] = {"_server": "whois.nic.sbi", "extend": "com"}
ZZ["sc"] = {"_server": "whois2.afilias-grs.net", "extend": "com"}
ZZ["sca"] = {"_server": "whois.nic.sca", "extend": "com"}
ZZ["scb"] = {"_server": "whois.nic.scb", "extend": "com"}
ZZ["schmidt"] = {"_server": "whois.nic.schmidt", "extend": "com"}
ZZ["scholarships"] = {"_server": "whois.nic.scholarships", "extend": "com"}
ZZ["schwarz"] = {"_server": "whois.nic.schwarz", "extend": "com"}
ZZ["scot"] = {"_server": "whois.nic.scot", "extend": "com"}
ZZ["seat"] = {"_server": "whois.nic.seat", "extend": "com"}
ZZ["secure"] = {"_server": "whois.nic.secure", "extend": "com"}
ZZ["seek"] = {"_server": "whois.nic.seek", "extend": "com"}
ZZ["select"] = {"_server": "whois.nic.select", "extend": "com"}
ZZ["seven"] = {"_server": "whois.nic.seven", "extend": "com"}
ZZ["sex"] = {"_server": "whois.nic.sex", "extend": "com"}
ZZ["sfr"] = {"_server": "whois.nic.sfr", "extend": "com"}
ZZ["shangrila"] = {"_server": "whois.nic.shangrila", "extend": "com"}
ZZ["shell"] = {"_server": "whois.nic.shell", "extend": "com"}
ZZ["shia"] = {"_server": "whois.nic.shia", "extend": "com"}
ZZ["shiksha"] = {"_server": "whois.nic.shiksha", "extend": "com"}
ZZ["silk"] = {"_server": "whois.nic.silk", "extend": "com"}
ZZ["sina"] = {"_server": "whois.nic.sina", "extend": "com"}
ZZ["ski"] = {"_server": "whois.nic.ski", "extend": "com"}
ZZ["sky"] = {"_server": "whois.nic.sky", "extend": "com"}
ZZ["sling"] = {"_server": "whois.nic.sling", "extend": "com"}
ZZ["smart"] = {"_server": "whois.nic.smart", "extend": "com"}
ZZ["smile"] = {"_server": "whois.nic.smile", "extend": "com"}
ZZ["sncf"] = {"_server": "whois.nic.sncf", "extend": "com"}
ZZ["sony"] = {"_server": "whois.nic.sony", "extend": "com"}
ZZ["soy"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["spa"] = {"_server": "whois.afilias-srs.net", "extend": "com"}
ZZ["sport"] = {"_server": "whois.nic.sport", "extend": "com"}
ZZ["spot"] = {"_server": "whois.nic.spot", "extend": "com"}
ZZ["ss"] = {"_server": "whois.nic.ss", "extend": "com"}
ZZ["star"] = {"_server": "whois.nic.star", "extend": "com"}
ZZ["statebank"] = {"_server": "whois.nic.statebank", "extend": "com"}
ZZ["stc"] = {"_server": "whois.nic.stc", "extend": "com"}
ZZ["stcgroup"] = {"_server": "whois.nic.stcgroup", "extend": "com"}
ZZ["stream"] = {"_server": "whois.nic.stream", "extend": "com"}
ZZ["sucks"] = {"_server": "whois.nic.sucks", "extend": "com"}
ZZ["surf"] = {"_server": "whois.nic.surf", "extend": "com"}
ZZ["suzuki"] = {"_server": "whois.nic.suzuki", "extend": "com"}
ZZ["swatch"] = {"_server": "whois.nic.swatch", "extend": "com"}
ZZ["swiss"] = {"_server": "whois.nic.swiss", "extend": "com"}
ZZ["sydney"] = {"_server": "whois.nic.sydney", "extend": "com"}
ZZ["tab"] = {"_server": "whois.nic.tab", "extend": "com"}
ZZ["taipei"] = {"_server": "whois.nic.taipei", "extend": "com"}
ZZ["talk"] = {"_server": "whois.nic.talk", "extend": "com"}
ZZ["taobao"] = {"_server": "whois.nic.taobao", "extend": "com"}
ZZ["tatamotors"] = {"_server": "whois.nic.tatamotors", "extend": "com"}
ZZ["tatar"] = {"_server": "whois.nic.tatar", "extend": "com"}
ZZ["tci"] = {"_server": "whois.nic.tci", "extend": "com"}
ZZ["tdk"] = {"_server": "whois.nic.tdk", "extend": "com"}
ZZ["teva"] = {"_server": "whois.nic.teva", "extend": "com"}
ZZ["thd"] = {"_server": "whois.nic.thd", "extend": "com"}
ZZ["tiaa"] = {"_server": "whois.nic.tiaa", "extend": "com"}
ZZ["tiffany"] = {"_server": "whois.nic.tiffany", "extend": "com"}
ZZ["tirol"] = {"_server": "whois.nic.tirol", "extend": "com"}
ZZ["tmall"] = {"_server": "whois.nic.tmall", "extend": "com"}
ZZ["toray"] = {"_server": "whois.nic.toray", "extend": "com"}
ZZ["toshiba"] = {"_server": "whois.nic.toshiba", "extend": "com"}
ZZ["total"] = {"_server": "whois.nic.total", "extend": "com"}
ZZ["toyota"] = {"_server": "whois.nic.toyota", "extend": "com"}
ZZ["trading"] = {"_server": "whois.nic.trading", "extend": "com"}
ZZ["travelchannel"] = {"_server": "whois.nic.travelchannel", "extend": "com"}
ZZ["trust"] = {"_server": "whois.nic.trust", "extend": "com"}
ZZ["tui"] = {"_server": "whois.nic.tui", "extend": "com"}
ZZ["tunes"] = {"_server": "whois.nic.tunes", "extend": "com"}
ZZ["tushu"] = {"_server": "whois.nic.tushu", "extend": "com"}
ZZ["tvs"] = {"_server": "whois.nic.tvs", "extend": "com"}
ZZ["ubank"] = {"_server": "whois.nic.ubank", "extend": "com"}
ZZ["ubs"] = {"_server": "whois.nic.ubs", "extend": "com"}
ZZ["unicom"] = {"_server": "whois.nic.unicom", "extend": "com"}
ZZ["ups"] = {"_server": "whois.nic.ups", "extend": "com"}
ZZ["vana"] = {"_server": "whois.nic.vana", "extend": "com"}
ZZ["vanguard"] = {"_server": "whois.nic.vanguard", "extend": "com"}
ZZ["vegas"] = {"_server": "whois.nic.vegas", "extend": "com"}
ZZ["verisign"] = {"_server": "whois.nic.verisign", "extend": "com"}
ZZ["versicherung"] = {"_server": "whois.nic.versicherung", "extend": "com"}
ZZ["vg"] = {"_server": "whois.nic.vg", "extend": "com"}
ZZ["virgin"] = {"_server": "whois.nic.virgin", "extend": "com"}
ZZ["visa"] = {"_server": "whois.nic.visa", "extend": "com"}
ZZ["viva"] = {"_server": "whois.nic.viva", "extend": "com"}
ZZ["vlaanderen"] = {"_server": "whois.nic.vlaanderen", "extend": "com"}
ZZ["vodka"] = {"_server": "whois.nic.vodka", "extend": "com"}
ZZ["volvo"] = {"_server": "whois.nic.volvo", "extend": "com"}
ZZ["vote"] = {"_server": "whois.nic.vote", "extend": "com"}
ZZ["voting"] = {"_server": "whois.nic.voting", "extend": "com"}
ZZ["voto"] = {"_server": "whois.nic.voto", "extend": "com"}
ZZ["wales"] = {"_server": "whois.nic.wales", "extend": "com"}
ZZ["walmart"] = {"_server": "whois.nic.walmart", "extend": "com"}
ZZ["walter"] = {"_server": "whois.nic.walter", "extend": "com"}
ZZ["wanggou"] = {"_server": "whois.nic.wanggou", "extend": "com"}
ZZ["watches"] = {"_server": "whois.nic.watches", "extend": "com"}
ZZ["weber"] = {"_server": "whois.nic.weber", "extend": "com"}
ZZ["wed"] = {"_server": "whois.nic.wed", "extend": "com"}
ZZ["wedding"] = {"_server": "whois.nic.wedding", "extend": "com"}
ZZ["weibo"] = {"_server": "whois.nic.weibo", "extend": "com"}
ZZ["whoswho"] = {"_server": "whois.nic.whoswho", "extend": "com"}
ZZ["wien"] = {"_server": "whois.nic.wien", "extend": "com"}
ZZ["wme"] = {"_server": "whois.nic.wme", "extend": "com"}
ZZ["wolterskluwer"] = {"_server": "whois.nic.wolterskluwer", "extend": "com"}
ZZ["woodside"] = {"_server": "whois.nic.woodside", "extend": "com"}
ZZ["wow"] = {"_server": "whois.nic.wow", "extend": "com"}
ZZ["wtc"] = {"_server": "whois.nic.wtc", "extend": "com"}
ZZ["xerox"] = {"_server": "whois.nic.xerox", "extend": "com"}
ZZ["xfinity"] = {"_server": "whois.nic.xfinity", "extend": "com"}
ZZ["xn--11b4c3d"] = {"_server": "whois.nic.xn--11b4c3d", "extend": "com"}
ZZ["xn--1qqw23a"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["xn--3pxu8k"] = {"_server": "whois.nic.xn--3pxu8k", "extend": "com"}
ZZ["xn--42c2d9a"] = {"_server": "whois.nic.xn--42c2d9a", "extend": "com"}
ZZ["xn--4gbrim"] = {"_server": "whois.nic.xn--4gbrim", "extend": "com"}
ZZ["xn--55qx5d"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["xn--5su34j936bgsg"] = {"_server": "whois.nic.xn--5su34j936bgsg", "extend": "com"}
ZZ["xn--5tzm5g"] = {"_server": "whois.nic.xn--5tzm5g", "extend": "com"}
ZZ["xn--6frz82g"] = {"_server": "whois.nic.xn--6frz82g", "extend": "com"}
ZZ["xn--6qq986b3xl"] = {"_server": "whois.gtld.knet.cn", "extend": "com"}
ZZ["xn--80adxhks"] = {"_server": "whois.nic.xn--80adxhks", "extend": "com"}
ZZ["xn--80aqecdr1a"] = {"_server": "whois.nic.xn--80aqecdr1a", "extend": "com"}
ZZ["xn--80asehdb"] = {"_server": "whois.nic.xn--80asehdb", "extend": "com"}
ZZ["xn--80aswg"] = {"_server": "whois.nic.xn--80aswg", "extend": "com"}
ZZ["xn--8y0a063a"] = {"_server": "whois.nic.xn--8y0a063a", "extend": "com"}
ZZ["xn--9dbq2a"] = {"_server": "whois.nic.xn--9dbq2a", "extend": "com"}
ZZ["xn--9krt00a"] = {"_server": "whois.nic.xn--9krt00a", "extend": "com"}
ZZ["xn--c1avg"] = {"_server": "whois.nic.xn--c1avg", "extend": "com"}
ZZ["xn--c2br7g"] = {"_server": "whois.nic.xn--c2br7g", "extend": "com"}
ZZ["xn--cckwcxetd"] = {"_server": "whois.nic.xn--cckwcxetd", "extend": "com"}
ZZ["xn--czrs0t"] = {"_server": "whois.nic.xn--czrs0t", "extend": "com"}
ZZ["xn--efvy88h"] = {"_server": "whois.nic.xn--efvy88h", "extend": "com"}
ZZ["xn--fhbei"] = {"_server": "whois.nic.xn--fhbei", "extend": "com"}
ZZ["xn--fiqs8s"] = {"_server": "cwhois.cnnic.cn", "extend": "com"}
ZZ["xn--fiqz9s"] = {"_server": "cwhois.cnnic.cn", "extend": "com"}
ZZ["xn--fjq720a"] = {"_server": "whois.nic.xn--fjq720a", "extend": "com"}
ZZ["xn--fzys8d69uvgm"] = {"_server": "whois.nic.xn--fzys8d69uvgm", "extend": "com"}
ZZ["xn--i1b6b1a6a2e"] = {"_server": "whois.nic.xn--i1b6b1a6a2e", "extend": "com"}
ZZ["xn--io0a7i"] = {"_server": "whois.ngtld.cn", "extend": "com"}
ZZ["xn--j1aef"] = {"_server": "whois.nic.xn--j1aef", "extend": "com"}
ZZ["xn--jlq480n2rg"] = {"_server": "whois.nic.xn--jlq480n2rg", "extend": "com"}
ZZ["xn--kcrx77d1x4a"] = {"_server": "whois.nic.xn--kcrx77d1x4a", "extend": "com"}
ZZ["xn--kput3i"] = {"_server": "whois.nic.xn--kput3i", "extend": "com"}
ZZ["xn--mgba7c0bbn0a"] = {"_server": "whois.nic.xn--mgba7c0bbn0a", "extend": "com"}
ZZ["xn--mgbab2bd"] = {"_server": "whois.nic.xn--mgbab2bd", "extend": "com"}
ZZ["xn--mgbca7dzdo"] = {"_server": "whois.nic.xn--mgbca7dzdo", "extend": "com"}
ZZ["xn--mgbi4ecexp"] = {"_server": "whois.nic.xn--mgbi4ecexp", "extend": "com"}
ZZ["xn--mgbt3dhd"] = {"_server": "whois.nic.xn--mgbt3dhd", "extend": "com"}
ZZ["xn--mk1bu44c"] = {"_server": "whois.nic.xn--mk1bu44c", "extend": "com"}
ZZ["xn--mxtq1m"] = {"_server": "whois.nic.xn--mxtq1m", "extend": "com"}
ZZ["xn--ngbc5azd"] = {"_server": "whois.nic.xn--ngbc5azd", "extend": "com"}
ZZ["xn--ngbe9e0a"] = {"_server": "whois.nic.xn--ngbe9e0a", "extend": "com"}
ZZ["xn--ngbrx"] = {"_server": "whois.nic.xn--ngbrx", "extend": "com"}
ZZ["xn--nqv7f"] = {"_server": "whois.nic.xn--nqv7f", "extend": "com"}
ZZ["xn--nqv7fs00ema"] = {"_server": "whois.nic.xn--nqv7fs00ema", "extend": "com"}
ZZ["xn--pssy2u"] = {"_server": "whois.nic.xn--pssy2u", "extend": "com"}
ZZ["xn--q9jyb4c"] = {"_server": "whois.nic.google", "extend": "com"}
ZZ["xn--ses554g"] = {"_server": "whois.nic.xn--ses554g", "extend": "com"}
ZZ["xn--t60b56a"] = {"_server": "whois.nic.xn--t60b56a", "extend": "com"}
ZZ["xn--tckwe"] = {"_server": "whois.nic.xn--tckwe", "extend": "com"}
ZZ["xn--tiq49xqyj"] = {"_server": "whois.nic.xn--tiq49xqyj", "extend": "com"}
ZZ["xn--unup4y"] = {"_server": "whois.nic.xn--unup4y", "extend": "com"}
ZZ["xn--vermgensberater-ctb"] = {"_server": "whois.nic.xn--vermgensberater-ctb", "extend": "com"}
ZZ["xn--vermgensberatung-pwb"] = {"_server": "whois.nic.xn--vermgensberatung-pwb", "extend": "com"}
ZZ["xn--vhquv"] = {"_server": "whois.nic.xn--vhquv", "extend": "com"}
ZZ["xn--w4r85el8fhu5dnra"] = {"_server": "whois.nic.xn--w4r85el8fhu5dnra", "extend": "com"}
ZZ["xn--w4rs40l"] = {"_server": "whois.nic.xn--w4rs40l", "extend": "com"}
ZZ["xxx"] = {"_server": "whois.nic.xxx", "extend": "com"}
ZZ["yamaxun"] = {"_server": "whois.nic.yamaxun", "extend": "com"}
ZZ["yoga"] = {"_server": "whois.nic.yoga", "extend": "com"}
ZZ["yokohama"] = {"_server": "whois.nic.yokohama", "extend": "com"}
ZZ["you"] = {"_server": "whois.nic.you", "extend": "com"}
ZZ["zappos"] = {"_server": "whois.nic.zappos", "extend": "com"}

ZZ["amfam"] = {"_server": "whois.nic.amfam", "extend": "com"}
ZZ["lplfinancial"] = {"_server": "whois.nic.lplfinancial", "extend": "com"}  # auto-detected via IANA tld
ZZ["okinawa"] = {"_server": "whois.nic.okinawa", "extend": "com"}  # auto-detected via IANA tld
ZZ["ryukyu"] = {"_server": "whois.nic.ryukyu", "extend": "com"}  # auto-detected via IANA tld
ZZ["softbank"] = {"_server": "whois.nic.softbank", "extend": "com"}  # auto-detected via IANA tld

ZZ["gov"] = {"extend": "com"}  # only 2 or 3 fields are actually returned

ZZ["tm"] = {  # Turkmenistan
    "extend": "com",
    "domain_name": r"Domain\s*:\s*(.+)",
    "expiration_date": r"Expiry\s*:\s*(\d+-\d+-\d+)",
    "name_servers": r"NS\s+\d+\s+:\s*(\S+)",
    "status": r"Status\s*:\s*(.+)",
}

ZZ["com.tm"] = {"extend": "tm"}
