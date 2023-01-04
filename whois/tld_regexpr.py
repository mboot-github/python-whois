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
com = {
    "extend": None,
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s?(.+)",
    "registrant": r"Registrant\s*Organi(?:s|z)ation:\s?(.+)",
    "registrant_country": r"Registrant Country:\s?(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "name_servers": r"Name Server:\s*(.+)\s*",
    "status": r"Status:\s?(.+)",
    # the trailing domain must have minimal 2 parts firstname.lastname@fld.tld
    # it may actually have more then 4 levels
    # to match the dot in firstname.lastname we must use \.
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

# United Kingdom - academic sub-domain
ac_uk = {
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

co_uk = {
    "extend": "uk",
    "domain_name": r"Domain name:\s+(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "name_servers": r"Name servers:\s+(.+)\s+(.+)",
    "status": r"Registration status:\s*(.+)",
    "creation_date": r"Registered on:(.+)",
    "expiration_date": r"Expiry date:(.+)",
    "updated_date": r"Last updated:(.+)",
    "owner": r"Domain Owner:\s+(.+)",
    "registrant": r"Registered Contact:\s+(.+)",
}

# United Arab Emirates
# ae = {    "extend": "ar"}
# redefined below

# Anguilla
ai = {
    "extend": "com",
    "_server": "whois.nic.ai",
}

# Armenia
am = {
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
amsterdam = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Domain Status:\s?(.+)",
}

app = {
    "extend": "com",
    "_server": "whois.nic.google",
}

# Argentina
ar = {
    "extend": "com",
    "domain_name": r"domain\s*:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "creation_date": r"registered:\s?(.+)",
    "expiration_date": r"expire:\s?(.+)",
    "updated_date": r"changed\s*:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)\s*",
}

asia = {
    "extend": "com",
}

# Austria
at = {
    "extend": "com",
    "_server": "whois.nic.at",
    "domain_name": r"domain:\s?(.+)",
    "updated_date": r"changed:\s?(.+)",
    "name_servers": r"nserver:\s*(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant": r"registrant:\s?(.+)",
}

# Australia
au = {
    "extend": "com",
    "registrar": r"Registrar Name:\s?(.+)",
    "updated_date": r"Last Modified:([^\n]*)",  # fix empty LastModified
}

ax = {
    "extend": "com",
    "domain_name": r"domain\.+:\s*(\S+)",
    "registrar": r"registrar\.+:\s*(.+)",
    "creation_date": r"created\.+:\s*(\S+)",
    "expiration_date": r"expires\.+:\s*(\S+)",
    "updated_date": r"modified\.+:\s?(\S+)",
    "name_servers": r"nserver\.+:\s*(\S+)",
    "status": r"status\.+:\s*(\S+)",
    "registrant": r"Holder\s+name\.+:\s*(.+)\r?\n",  # not always present see meta.ax and google.ax
    "registrant_country": r"country\.+:\s*(.+)\r?\n",  # not always present see meta.ax and google.ax
}

aw = {
    "extend": "nl",
    "name_servers": r"Domain nameservers:\s+(\S+)[ \t]*\r?\n(?:\s+(\S+))?",
}

# Banking TLD - ICANN
bank = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
}

be = {
    "extend": "pl",
    "domain_name": r"\nDomain:\s*(.+)",
    "registrar": r"Company Name:\n?(.+)",
    "creation_date": r"Registered:\s*(.+)\n",
    "status": r"Status:\s?(.+)",
}

biz = {
    "extend": "com",
    "registrar": r"Registrar:\s?(.+)",
    "registrant": r"Registrant Organization:\s?(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": None,
}

br = {
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

by = {
    "extend": "com",
    "domain_name": r"Domain Name:\s*(.+)",
    "registrar": r"\nRegistrar:\s*(.+)",
    "registrant": r"\nOrg:\s*(.+)",
    "registrant_country": r"\nCountry:\s*(.+)",
    "creation_date": r"\nCreation Date:\s*(.+)",
    "expiration_date": r"\nExpiration Date:\s*(.+)",
    "updated_date": r"\nUpdated Date:\s*(.+)",
    "name_servers": r"\nName Server:\s*(.+)",
}

# Brittany (French Territory)
# Some personal data could be obfuscated at request from the registrant
bzh = {
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

ca = {
    "extend": "com",
}

cat = {
    "extend": "com",
    "_server": "whois.nic.cat",
}

cc = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

cl = {
    "extend": "com",
    "registrar": "nic.cl",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "name_servers": r"Name Server:\s*(.+)\s*",
}

click = {
    "extend": "com",
}

cloud = {
    "extend": "com",
}

club = {
    "extend": "com",
}

cn = {
    "extend": "com",
    "registrar": r"Sponsoring Registrar:\s?(.+)",
    "registrant": r"Registrant:\s?(.+)",
    "creation_date": r"Registration Time:\s?(.+)",
    "expiration_date": r"Expiration Time:\s?(.+)",
}

co = {
    "extend": "biz",
    "status": r"Status:\s?(.+)",
}

com_au = {
    "extend": "au",
}

com_tr = {
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

edu_tr = {
    "extend": "com_tr",
}

org_tr = {
    "extend": "com_tr",
}

net_tr = {
    "extend": "com_tr",
}

co_il = {
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

co_jp = {
    "extend": "jp",
    "domain_name": r"\[ドメイン名\]\s?(.+)",
    "creation_date": r"\[登録年月\]\s?(.+)",
    "expiration_date": r"\[状態\].+\((.+)\)",
    "updated_date": r"\[最終更新\]\s?(.+)",
}

courses = {
    "extend": "com",
}

cr = {
    "extend": "cz",
}

cz = {
    "extend": "com",
    "domain_name": r"domain:\s?(.+)",
    "registrar": r"registrar:\s?(.+)",
    "registrant": r"registrant:\s?(.+)",
    "registrant_country": None,
    "creation_date": r"registered:\s?(.+)",
    "expiration_date": r"expire:\s?(.+)",
    "updated_date": r"changed:\s?(.+)",
    "name_servers": r"nserver:\s*(.+) ",
    "status": r"status:\s*(.+)",
}

# The .de NIC whois servers no longer provide any PII data for domains in the TLD.
# To obtains "personal" data, one must use the web interface: http://www.denic.de/en/domains/whois-service/web-whois.html
de = {
    "extend": "com",
    "domain_name": r"\ndomain:\s*(.+)",
    "updated_date": r"\nChanged:\s?(.+)",
    "name_servers": r"Nserver:\s*(.+)",
}

# Developer
dev = {
    "extend": "com",
}

# Denmark
dk = {
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

download = {
    "extend": "amsterdam",
    "name_servers": r"Name Server:[ \t]+(\S+)",  # fix needed after strip(\r) in _2_parse.py in version 0.19
    "status": r"Domain Status:\s*([a-zA-z]+)",
}

edu = {
    "extend": "com",
    "registrant": r"Registrant:\s*(.+)",
    "creation_date": r"Domain record activated:\s?(.+)",
    "updated_date": r"Domain record last updated:\s?(.+)",
    "expiration_date": r"Domain expires:\s?(.+)",
    "name_servers": r"Name Servers:\s?\t(.+)\n\t(.+)\n",
}

# estonian
ee = {
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

eu = {
    "extend": "com",
    "registrar": r"Name:\s?(.+)",
    "domain_name": r"\nDomain:\s*(.+)",
    "name_servers": r"Name servers:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?",
}

fi = {
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

fit = {
    "extend": "com",
}

fm = {
    "extend": "com",
}

fo = {
    "extend": "com",
    "registrant": None,
}

fr = {
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

game = {
    "extend": "amsterdam",
}

global_ = {
    "extend": "amsterdam",
    "name_servers": r"Name Server: (.+)",
}

# Honduras
hn = {
    "extend": "com",
}

# Hong Kong
hk = {
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

id_ = {
    "extend": "com",
    "registrar": r"Sponsoring Registrar Organization:\s?(.+)",
    "creation_date": r"Created On:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "updated_date": r"Last Updated On:\s?(.+)$",
}

# Ireland
ie = {
    "extend": "com",
}

im = {
    "domain_name": r"Domain Name:\s+(.+)",
    "status": None,
    "registrar": None,
    "registrant_country": None,
    "creation_date": "",
    "expiration_date": r"Expiry Date:\s?(.+)",
    "updated_date": "",
    "name_servers": r"Name Server:(.+)",
}

in_ = {
    "extend": "com",
}

info = {
    "extend": "com",
}

ink = {
    "extend": "amsterdam",
}

io = {
    "extend": "com",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
}

ir = {
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

is_ = {
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

it = {
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
jp = {
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
co_jp = {
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
ne_jp = {"extend": "co_jp"}

or_jp = {"extend": "co_jp"}

go_jp = {"extend": "co_jp"}

ac_jp = {"extend": "co_jp"}

ad_jp = {"extend": "co_jp"}

ed_jp = {"extend": "co_jp"}

gr_jp = {"extend": "co_jp"}

lg_jp = {"extend": "co_jp"}

geo_jp = {"extend": "co_jp"}

kiwi = {
    "extend": "com",
}

kg = {
    "domain_name": r"Domain\s+(\S+)",
    "registrar": r"Billing\sContact:\n.*\n\s+Name:\s(.+)\n",
    "registrant_country": None,
    "expiration_date": r"Record expires on:\s+(.+)",
    "creation_date": r"Record created:\s+(.+)",
    "updated_date": r"Record last updated on:\s+(.+)",
    # name servers have trailing whitespace
    "name_servers": r"Name servers in the listed order:\n\n(?:(\S+)[ \t]*\n)(?:(\S+)[ \t]*\n)?",
    "status": r"Domain\s+\S+\s+\((\S+)\)",
}

# Saint Kitts and Nevis
kn = {
    "extend": "com",
}

kr = {
    "extend": "com",
    "domain_name": r"Domain Name\s*:\s?(.+)",
    "registrar": r"Authorized Agency\s*:\s*(.+)",
    "registrant": r"Registrant\s*:\s*(.+)",
    "creation_date": r"Registered Date\s*:\s?(.+)",
    "expiration_date": r"Expiration Date\s*:\s?(.+)",
    "updated_date": r"Last Updated Date\s*:\s?(.+)",
    "status": r"status\s*:\s?(.+)",
}

kz = {
    "extend": None,
    "domain_name": r"Domain name\.+:\s(.+)",
    "registrar": r"Current Registar:\s(.+)",
    "registrant_country": r"Country\.+:\s?(.+)",
    "expiration_date": None,
    "creation_date": r"Domain created:\s(.+)",
    "updated_date": r"Last modified :\s(.+)",
    "name_servers": r"server.*:\s(.+)",
    "status": r"Domain status :\s?(.+)",
}

link = {
    "extend": "amsterdam",
}

lt = {
    "extend": "com",
    "domain_name": r"Domain:\s?(.+)",
    "creation_date": r"Registered:\s?(.+)",
    "expiration_date": r"Expires:\s?(.+)",
    "name_servers": r"Nameserver:\s*(.+)\s*",
    "status": r"\nStatus:\s?(.+)",
}

lv = {
    "extend": "ru",
    "creation_date": r"Registered:\s*(.+)\n",
    "updated_date": r"Changed:\s*(.+)\n",
    "status": r"Status:\s?(.+)",
}

me = {
    # lines have \r
    "extend": "biz",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiry Date:\s?(.+)",
    "updated_date": None,  # some entries have no date string but not always
    "name_servers": r"Name Server:\s*(\S+)\r?\n",
    "status": r"Domain Status:\s?(.+)",
}

ml = {
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

mobi = {
    "extend": "com",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
    "updated_date": r"\nUpdated Date:\s?(.+)",
}

mx = {
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

name = {
    "extend": "com",
    "status": r"Domain Status:\s?(.+)",
}

# New-Caledonia (French Territory)
nc = {
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

net = {
    "extend": "com",
}

nl = {
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
no = {
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

nu = {
    "extend": "se",
}

nyc = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

nz = {
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

org = {
    "extend": "com",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
    "updated_date": r"\nLast Updated On:\s?(.+)",
    "name_servers": r"Name Server:\s?(.+)\s*",
}

ovh = {
    "extend": "com",
}

pe = {
    "extend": "com",
    "registrant": r"Registrant Name:\s?(.+)",
    "admin": r"Admin Name:\s?(.+)",
}

pharmacy = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"status:\s?(.+)",
}

pl = {
    # pl has lines ending in multiple line feeds \r and trailing whitespace
    "extend": "uk",
    "registrar": r"\nREGISTRAR:\s*(.+)\n",
    "creation_date": r"\ncreated:\s*(.+)\n",
    "updated_date": r"\nlast modified:\s*(.+)\n",
    "expiration_date": r"\noption expiration date:\s*(.+)\n",
    "name_servers": r"\nnameservers:(?:\s*(\S+)[ \t\r]*\n)(?:\s*(\S+)[ \t\r]*\n)?(?:\s*(\S+)[ \t\r]*\n)?",
    "status": r"\nStatus:\n\s*(.+)",
}

pro = {
    "extend": "com",
}

pt = {
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

pw = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

radio = {
    "extend": "com",
    "_server": "whois.nic.radio",
}

red = {
    "extend": "com",
}

ru = {
    "extend": "com",
    "domain_name": r"\ndomain:\s*(.+)",
    "creation_date": r"\ncreated:\s*(.+)",
    "expiration_date": r"\npaid-till:\s*(.+)",
    "name_servers": r"\nnserver:\s*(.+)",
    "status": r"\nstate:\s*(.+)",
}

# Rossíyskaya Federátsiya) is the Cyrillic country code top-level domain for the Russian Federation,
# In the Domain Name System it has the ASCII DNS name xn--p1ai.

ru_rf = {
    "extend": "ru",
}

sa = {
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

sh = {
    "extend": "com",
    "registrant": r"\nRegistrant Organization:\s?(.+)",
    "expiration_date": r"\nRegistry Expiry Date:\s*(.+)",
    "status": r"\nDomain Status:\s?(.+)",
}

shop = {
    "extend": "com",
}

se = {
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
com_sg = {
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
    "name_servers": r"Name Servers:(?:\s+(\S+))(?:\s+(\S+))?(?:\s+([\.\w]+)\s+)?",
    # this seems ok for 2 and 3 ns and does not catch the dnssec: line
    "status": r"Domain Status:\s*(.*)\r?\n",
    # "emails": r"(\S+@\S+)",
    "emails": r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}",
}

# Slovakia
sk = {
    "extend": "com",
    "domain_name": r"Domain:\s?(.+)",
    "creation_date": r"Created:\s?(.+)",
    "expiration_date": r"Valid Until:\s?(.+)",
    "updated_date": r"Updated:\s?(.+)",
    "name_servers": r"Nameserver:\s*(\S+)",  # fix needed after strip(\r) in _2_parse.py in version 0.19
    "registrant": r"Contact:\s?(.+)",
    "registrant_country": r"Country Code:\s?(.+)\nRegistrar:",
}

study = {
    "extend": "com",
}

tel = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"\nRegistry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

# Thailand - Commercial sub-domain
co_th = {
    "_server": "whois.thnic.co.th",
    "extend": "com",
    "registrant": r"Domain Holder Organization:\s?(.+)",
    "registrant_country": r"Domain Holder Country:\s?(.+)",
    "creation_date": r"Created date:\s?(.+)",
    "expiration_date": r"Exp date:\s?(.+)",
    "updated_date": r"Updated date:\s?(.+)",
}

go_th = {
    "extend": "co_th",
}

in_th = {
    "extend": "co_th",
}

ac_th = {
    "extend": "co_th",
}

tn = {
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

tokyo = {
    "extend": "com",
    "_server": "whois.nic.tokyo",
}

top = {
    "extend": "com",
}

trade = {
    "extend": "amsterdam",
}

tv = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

tz = {
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

ua = {
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

edu_ua = {
    "extend": "ua",
    "creation_date": r"\ncreated:\s+0-UANIC\s+(.+)",
}
com_ua = {
    "extend": "ua",
}
net_ua = {
    "extend": "ua",
}

lviv_ua = {
    "extend": "com",
}

uk = {
    "extend": "com",
    "registrant": r"Registrant:\n\s*(.+)",
    "creation_date": r"Registered on:\s*(.+)",
    "expiration_date": r"Expiry date:\s*(.+)",
    "updated_date": r"Last updated:\s*(.+)",
    "name_servers": r"Name Servers:\s*(\S+)\r?\n(?:\s+(\S+)\r?\n)?(?:\s+(\S+)\r?\n)?(?:\s+(\S+)\r?\n)?",
    "status": r"Registration status:\n\s*(.+)",
}

us = {
    "extend": "name",
}

uz = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Expiration Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

vip = {
    "_server": "whois.nic.vip",
    "extend": "com",
    "updated_date": None,
}

wiki = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

win = {
    "extend": "com",
}

work = {
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
}

xin = {
    "extend": "com",
    "_server": "whois.nic.xin",
}

za = {
    "extend": "com",
}

web_za = {"extend": "za", "_server": "web-whois.registry.net.za"}
org_za = {"extend": "za", "_server": "org-whois.registry.net.za"}
net_za = {"extend": "za", "_server": "net-whois.registry.net.za"}
co_za = {"extend": "za", "_server": "coza-whois.registry.net.za"}

gy = {
    "extend": "com",
}

# Multiple initialization
ca = rw = mu = bank

# Registry operator: donuts.domains
# WHOIS server: whois.donuts.co
_donuts = {
    "extend": "com",
    "_server": "whois.donuts.co",
    "registrant": r"Registrant Organization:\s?(.+)",
    "status": r"Domain Status:\s?(.+)",
}

academy = {"extend": "_donuts"}
accountants = {"extend": "_donuts"}
actor = {"extend": "_donuts"}
agency = {"extend": "_donuts"}
airforce = {"extend": "_donuts"}
apartments = {"extend": "_donuts"}
army = {"extend": "_donuts"}
associates = {"extend": "_donuts"}
attorney = {"extend": "_donuts"}
auction = {"extend": "_donuts"}
band = {"extend": "_donuts"}
bargains = {"extend": "_donuts"}
bike = {"extend": "_donuts"}
bingo = {"extend": "_donuts"}
boutique = {"extend": "_donuts"}
builders = {"extend": "_donuts"}
business = {"extend": "_donuts"}
cab = {"extend": "_donuts"}
cafe = {"extend": "_donuts"}
camera = {"extend": "_donuts"}
camp = {"extend": "_donuts"}
capital = {"extend": "_donuts"}
cards = {"extend": "_donuts"}
careers = {"extend": "_donuts"}
care = {"extend": "_donuts"}
cash = {"extend": "_donuts"}
casino = {"extend": "_donuts"}
catering = {"extend": "_donuts"}
center = {"extend": "_donuts"}
charity = {"extend": "_donuts"}
chat = {"extend": "_donuts"}
cheap = {"extend": "_donuts"}
church = {"extend": "_donuts"}
city = {"extend": "_donuts"}
claims = {"extend": "_donuts"}
cleaning = {"extend": "_donuts"}
clinic = {"extend": "_donuts"}
clothing = {"extend": "_donuts"}
coach = {"extend": "_donuts"}
codes = {"extend": "_donuts"}
coffee = {"extend": "_donuts"}
community = {"extend": "_donuts"}
company = {"extend": "_donuts"}
computer = {"extend": "_donuts"}
condos = {"extend": "_donuts"}
construction = {"extend": "_donuts"}
consulting = {"extend": "_donuts"}
contact = {"extend": "_donuts"}
contractors = {"extend": "_donuts"}
cool = {"extend": "_donuts"}
coupons = {"extend": "_donuts"}
creditcard = {"extend": "_donuts"}
credit = {"extend": "_donuts"}
cruises = {"extend": "_donuts"}
dance = {"extend": "_donuts"}
dating = {"extend": "_donuts"}
deals = {"extend": "_donuts"}
degree = {"extend": "_donuts"}
delivery = {"extend": "_donuts"}
democrat = {"extend": "_donuts"}
dental = {"extend": "_donuts"}
dentist = {"extend": "_donuts"}
diamonds = {"extend": "_donuts"}
digital = {"extend": "_donuts"}
direct = {"extend": "_donuts"}
directory = {"extend": "_donuts"}
discount = {"extend": "_donuts"}
doctor = {"extend": "_donuts"}
dog = {"extend": "_donuts"}
domains = {"extend": "_donuts"}
education = {"extend": "_donuts"}
email = {"extend": "_donuts"}
energy = {"extend": "_donuts"}
engineer = {"extend": "_donuts"}
engineering = {"extend": "_donuts"}
enterprises = {"extend": "_donuts"}
equipment = {"extend": "_donuts"}
estate = {"extend": "_donuts"}
events = {"extend": "_donuts"}
exchange = {"extend": "_donuts"}
expert = {"extend": "_donuts"}
exposed = {"extend": "_donuts"}
express = {"extend": "_donuts"}
fail = {"extend": "_donuts"}
family = {"extend": "_donuts"}
fan = {"extend": "_donuts"}
farm = {"extend": "_donuts"}
finance = {"extend": "_donuts"}
financial = {"extend": "_donuts"}
fish = {"extend": "_donuts"}
fitness = {"extend": "_donuts"}
flights = {"extend": "_donuts"}
florist = {"extend": "_donuts"}
football = {"extend": "_donuts"}
forsale = {"extend": "_donuts"}
foundation = {"extend": "_donuts"}
fund = {"extend": "_donuts"}
furniture = {"extend": "_donuts"}
futbol = {"extend": "_donuts"}
fyi = {"extend": "_donuts"}
gallery = {"extend": "_donuts"}
games = {"extend": "_donuts"}
gifts = {"extend": "_donuts"}
gives = {"extend": "_donuts"}
glass = {"extend": "_donuts"}
gmbh = {"extend": "_donuts"}
gold = {"extend": "_donuts"}
golf = {"extend": "_donuts"}
graphics = {"extend": "_donuts"}
gratis = {"extend": "_donuts"}
gripe = {"extend": "_donuts"}
group = {"extend": "_donuts"}
guide = {"extend": "_donuts"}
guru = {"extend": "_donuts"}
haus = {"extend": "_donuts"}
healthcare = {"extend": "_donuts"}
hockey = {"extend": "_donuts"}
holdings = {"extend": "_donuts"}
holiday = {"extend": "_donuts"}
hospital = {"extend": "_donuts"}
house = {"extend": "_donuts"}
immobilien = {"extend": "_donuts"}
immo = {"extend": "_donuts"}
industries = {"extend": "_donuts"}
institute = {"extend": "_donuts"}
insure = {"extend": "_donuts"}
international = {"extend": "_donuts"}
investments = {"extend": "_donuts"}
irish = {"extend": "_donuts"}
jetzt = {"extend": "_donuts"}
jewelry = {"extend": "_donuts"}
kaufen = {"extend": "_donuts"}
kitchen = {"extend": "_donuts"}
land = {"extend": "_donuts"}
lawyer = {"extend": "_donuts"}
lease = {"extend": "_donuts"}
legal = {"extend": "_donuts"}
life = {"extend": "_donuts"}
lighting = {"extend": "_donuts"}
limited = {"extend": "_donuts"}
limo = {"extend": "_donuts"}
live = {"extend": "_donuts"}
loans = {"extend": "_donuts"}
ltd = {"extend": "_donuts"}
maison = {"extend": "_donuts"}
management = {"extend": "_donuts"}
market = {"extend": "_donuts"}
marketing = {"extend": "_donuts"}
mba = {"extend": "_donuts"}
media = {"extend": "_donuts"}
memorial = {"extend": "_donuts"}
moda = {"extend": "_donuts"}
money = {"extend": "_donuts"}
mortgage = {"extend": "_donuts"}
movie = {"extend": "_donuts"}
navy = {"extend": "_donuts"}
network = {"extend": "_donuts"}
news = {"extend": "_donuts"}
ninja = {"extend": "_donuts"}
partners = {"extend": "_donuts"}
parts = {"extend": "_donuts"}
pet = {"extend": "_donuts"}
photography = {"extend": "_donuts"}
photos = {"extend": "_donuts"}
pictures = {"extend": "_donuts"}
pizza = {"extend": "_donuts"}
place = {"extend": "_donuts"}
plumbing = {"extend": "_donuts"}
plus = {"extend": "_donuts"}
productions = {"extend": "_donuts"}
properties = {"extend": "_donuts"}
pub = {"extend": "_donuts"}
recipes = {"extend": "_donuts"}
rehab = {"extend": "_donuts"}
reise = {"extend": "_donuts"}
reisen = {"extend": "_donuts"}
rentals = {"extend": "_donuts"}
repair = {"extend": "_donuts"}
report = {"extend": "_donuts"}
republican = {"extend": "_donuts"}
restaurant = {"extend": "_donuts"}
reviews = {"extend": "_donuts"}
rip = {"extend": "_donuts"}
rocks = {"extend": "_donuts"}
run = {"extend": "_donuts"}
sale = {"extend": "_donuts"}
salon = {"extend": "_donuts"}
sarl = {"extend": "_donuts"}
school = {"extend": "_donuts"}
schule = {"extend": "_donuts"}
services = {"extend": "_donuts"}
shoes = {"extend": "_donuts"}
shopping = {"extend": "_donuts"}
show = {"extend": "_donuts"}
singles = {"extend": "_donuts"}
soccer = {"extend": "_donuts"}
social = {"extend": "_donuts"}
software = {"extend": "_donuts"}
solar = {"extend": "_donuts"}
solutions = {"extend": "_donuts"}
studio = {"extend": "_donuts"}
style = {"extend": "_donuts"}
supplies = {"extend": "_donuts"}
supply = {"extend": "_donuts"}
support = {"extend": "_donuts"}
surgery = {"extend": "_donuts"}
systems = {"extend": "_donuts"}
tax = {"extend": "_donuts"}
taxi = {"extend": "_donuts"}
team = {"extend": "_donuts"}
technology = {"extend": "_donuts"}
tennis = {"extend": "_donuts"}
theater = {"extend": "_donuts"}
tienda = {"extend": "_donuts"}
tips = {"extend": "_donuts"}
tires = {"extend": "_donuts"}
today = {"extend": "_donuts"}
tools = {"extend": "_donuts"}
tours = {"extend": "_donuts"}
town = {"extend": "_donuts"}
toys = {"extend": "_donuts"}
training = {"extend": "_donuts"}
travel = {"extend": "_donuts"}
university = {"extend": "_donuts"}
vacations = {"extend": "_donuts"}
ventures = {"extend": "_donuts"}
vet = {"extend": "_donuts"}
viajes = {"extend": "_donuts"}
video = {"extend": "_donuts"}
villas = {"extend": "_donuts"}
vin = {"extend": "_donuts"}
vision = {"extend": "_donuts"}
voyage = {"extend": "_donuts"}
watch = {"extend": "_donuts"}
wine = {"extend": "_donuts"}
works = {"extend": "_donuts"}
world = {"extend": "_donuts"}
wtf = {"extend": "_donuts"}
zone = {"extend": "_donuts"}

# Registry operator: CentralNic
# WHOIS server: whois.centralnic.com
_centralnic = {
    "extend": "com",
    "_server": "whois.centralnic.com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Domain Status:\s?(.+)",
}

art = {"extend": "_centralnic"}
auto = {"extend": "_centralnic"}
autos = {"extend": "_centralnic"}
baby = {"extend": "_centralnic"}
bar = {"extend": "_centralnic"}
beauty = {"extend": "_centralnic"}
best = {"extend": "_centralnic"}
blog = {"extend": "_centralnic"}
boats = {"extend": "_centralnic"}
bond = {"extend": "_centralnic"}
build = {"extend": "_centralnic"}
cam = {"extend": "_centralnic"}
car = {"extend": "_centralnic"}
cars = {"extend": "_centralnic"}
ceo = {"extend": "_centralnic"}
cfd = {"extend": "_centralnic"}
college = {"extend": "_centralnic"}
coop = {"extend": "_centralnic"}
cyou = {"extend": "_centralnic"}
dealer = {"extend": "_centralnic"}
desi = {"extend": "_centralnic"}
fans = {"extend": "_centralnic"}
feedback = {"extend": "_centralnic"}
forum = {"extend": "_centralnic"}
frl = {"extend": "_centralnic"}
fun = {"extend": "_centralnic"}
gent = {"extend": "_centralnic"}
hair = {"extend": "_centralnic"}
homes = {"extend": "_centralnic"}
host = {"extend": "_centralnic"}
icu = {"extend": "_centralnic"}
inc = {"extend": "_centralnic"}
kred = {"extend": "_centralnic"}
london = {"extend": "_centralnic"}
luxury = {"extend": "_centralnic"}
makeup = {"extend": "_centralnic"}
monster = {"extend": "_centralnic"}
motorcycles = {"extend": "_centralnic"}
online = {"extend": "_centralnic"}
ooo = {"extend": "_centralnic"}
press = {"extend": "_centralnic"}
protection = {"extend": "_centralnic"}
qpon = {"extend": "_centralnic"}
quest = {"extend": "_centralnic"}
reit = {"extend": "_centralnic"}
rent = {"extend": "_centralnic"}
rest = {"extend": "_centralnic"}
saarland = {"extend": "_centralnic"}
sbs = {"extend": "_centralnic"}
security = {"extend": "_centralnic"}
site = {"extend": "_centralnic"}
skin = {"extend": "_centralnic"}
space = {"extend": "_centralnic"}
storage = {"extend": "_centralnic"}
store = {"extend": "_centralnic"}
tech = {"extend": "_centralnic"}
theatre = {"extend": "_centralnic"}
tickets = {"extend": "_centralnic"}
uno = {"extend": "_centralnic"}
website = {"extend": "_centralnic"}
xyz = {"extend": "_centralnic"}
yachts = {"extend": "_centralnic"}
zuerich = {"extend": "_centralnic"}

# mboot added start
# note i extract the whois server for each toplevel domain using: https://github.com/jophy/iana_tld_list
# of which i am a contributer

ac = {
    "extend": None,
    "domain_name": r"Domain Name:\s+(.+)",
    "registrar": r"Registrar:\s+(.+)",
    "status": r"Domain Status:\s(.+)",
    "name_servers": r"Name Server:\s+(.+)",
    "registrant_country": r"Registrant Country:\s*(.*)\r?\n",
    "updated_date": r"Updated Date:\s+(.+)",
    "creation_date": r"Creation Date:\s+(.+)",
    "expiration_date": r"Registry Expiry Date:\s+(.+)",
}

ae = {
    "extend": "ar",
    "domain_name": r"Domain Name:\s+(.+)",
    "registrar": r"Registrar Name:\s+(.+)",
    "status": r"Status:\s(.+)",
    "name_servers": r"Name Server:\s+(.+)",
    "registrant_country": None,
    "creation_date": None,
    "expiration_date": None,
    "updated_date": None,
}

aero = {
    "extend": "ac",
    "_server": "whois.aero",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}


af = {
    "extend": "ac",
}

ag = {
    "extend": "ac",
}

bet = {
    "extend": "ac",
    "_server": "whois.nic.bet",
}

bg = {
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

bid = {
    "extend": "ac",
    "_server": "whois.nic.bid",
}

# Benin
# WHOIS server: whois.nic.bj
# by: https://github.com/LickosA

bj = {
    "_server": "whois.nic.bj",
    "extend": "com",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Registrar:\s*(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "updated_date": r"Updated Date:\s?(.+)",
    "status": r"Status:\s?(.+)",
}

buzz = {
    "extend": "amsterdam",
}

casa = {
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

cd = {
    "extend": "ac",
    "_server": "whois.nic.cd",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

cf = {
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

design = {
    "extend": "ac",
}

eus = {
    "extend": "ac",
}

ge = {
    "_server": "whois.nic.ge",
    "extend": "ac",
    "updated_date": None,
}

gq = {
    "extend": "ml",
    "_server": "whois.domino.gq",
}

la = {
    "extend": "com",
}

lol = {
    "extend": "amsterdam",
}

love = {
    "extend": "ac",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

ly = {
    "extend": "ac",
    "_server": "whois.nic.ly",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

com_ly = {
    "extend": "ly",
}

ma = {
    "extend": "ac",
    "_server": "whois.registre.ma",
    "registrar": r"Sponsoring Registrar:\s*(.+)",
}

mg = {
    "extend": "ac",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

moe = {
    "extend": "ac",
    "registrant_country": r"Registrant\s+Country:\s+(.+)",
}

ng = {
    "_server": "whois.nic.net.ng",
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

ong = {
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

pics = {
    "extend": "ac",
}

re = {
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

ro = {
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

rs = {
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
sg = {
    "_server": "whois.sgnic.sg",
    "registrar": r"Registrar:\s+(.+)",
    "domain_name": r"\s+Domain name:\s+(.+)",
    "creation_date": r"\s+Creation Date:\s+(.+)",
    "expiration_date": r"\s+Expiration Date:\s+(.+)",
    "updated_date": r"\s+Modified Date:\s+(.+)",
    "status": r"\s+Domain Status:\s(.+)",
    "registrant_country": None,
    "name_servers": r"Name Servers:\s+(\S+)[ \t]*\r?\n\s+(\S+)[ \t]*\r?\n\s+(\S+)",
}

srl = {
    "_server": "whois.afilias-srs.net",
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

su = {
    "extend": "ru",
}

td = {
    "_server": "whois.nic.td",
    "extend": "ac",
    "registrant_country": r"Registrant Country:\s+(.+)",
}

tw = {
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

com_tw = {
    "extend": "tw",
}

ug = {
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

co_ug = {
    "extend": "ug",
}

ca_ug = {
    "extend": "ug",
}

ws = {
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

re = {
    "domain_name": r"domain:\s+(.+)",
    "status": r"status:\s+(.+)",
    "registrar": r"registrar:\s+(.+)",
    "name_servers": r"nserver:\s+(.+)",
    "creation_date": r"created:\s+(.+)",
    "expiration_date": r"Expiry Date:\s+(.+)",
    "updated_date": r"last-update:\s+(.+)",
    "registrant_country": None,
}

bo = {
    "domain_name": r"\s*NOMBRE DE DOMINIO:\s+(.+)",
    "registrant_country": r"País:\s+(.+)",
    "creation_date": r"Fecha de activación:\s+(.+)",
    "expiration_date": r"Fecha de corte:\s+(.+)",
    "extend": None,
    "registrar": None,
    "status": None,
    "name_servers": None,
    "updated_date": None,
}

com_bo = {"extend": "bo"}

hr = {
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
_gtldKnet = {
    "extend": "com",
    "_server": "whois.gtld.knet.cn",
    "admin": r"Admin\s*Name:\s+(.+)",
}

wang = {"extend": "_gtldKnet"}
八卦 = {"extend": "_gtldKnet"}
商城 = {"extend": "_gtldKnet"}
网店 = {"extend": "_gtldKnet"}

accountant = {"extend": "com", "_server": "whois.nic.accountant"}
cricket = {"extend": "com", "_server": "whois.nic.cricket"}
date = {"extend": "com", "_server": "whois.nic.date"}
faith = {"extend": "com", "_server": "whois.nic.faith"}
hiphop = {"extend": "com", "_server": "whois.nic.hiphop"}
loan = {"extend": "com", "_server": "whois.nic.loan"}
party = {"extend": "com", "_server": "whois.nic.party"}
racing = {"extend": "com", "_server": "whois.nic.racing"}
ren = {"extend": "com", "_server": "whois.nic.ren"}
review = {"extend": "com", "_server": "whois.nic.review"}
science = {"extend": "com", "_server": "whois.nic.science"}
webcam = {"extend": "com", "_server": "whois.nic.webcam"}
fashion = {"extend": "com", "_server": "whois.nic.fashion"}

# Registry operator: UNR Corp.
# WHOIS server: whois.uniregistry.net
_uniregistry = {
    "extend": "com",
    "_server": "whois.uniregistry.net",
}

help = {"extend": "_uniregistry"}
photo = {"extend": "_uniregistry"}
sexy = {"extend": "_uniregistry"}
gift = {"extend": "_uniregistry"}
tattoo = {"extend": "_uniregistry"}
property = {"extend": "_uniregistry"}
juegos = {"extend": "_uniregistry"}
hosting = {"extend": "_uniregistry"}
guitars = {"extend": "_uniregistry"}
flowers = {"extend": "_uniregistry"}
diet = {"extend": "_uniregistry"}
christmas = {"extend": "_uniregistry"}
blackfriday = {"extend": "_uniregistry"}
audio = {"extend": "_uniregistry"}

# Registry operator: TLD REGISTRY LIMITED.
# WHOIS server: whois.teleinfo.cn
_teleinfo = {
    "extend": "com",
    "_server": "whois.teleinfo.cn",
}

中文网 = {"extend": "_teleinfo"}
在线 = {"extend": "_teleinfo"}

# RESTRICTED: now known as PrivateRegistry
# restricted domains never answer or never show information sufficient for parsing
# some only show if the domain is free, most allow using a website but some have no web
# but you may have to prove you are not a robot and limits apply also on the website
# some actually dont have a working whois server
# details can be found at:
# (https://www.iana.org/domains/root/db/<tld>.html)

_privateReg = {
    "_privateRegistry": True,
}

al = {"extend": "_privateReg"}
az = {"extend": "_privateReg"}
ba = {"extend": "_privateReg"}
ch = {"extend": "_privateReg"}
cv = {"extend": "_privateReg"}  # Cape Verde
cw = {"extend": "_privateReg"}
es = {"extend": "_privateReg"}
ga = {"extend": "_privateReg"}
gr = {"extend": "_privateReg"}
hu = {"extend": "_privateReg"}
li = {"extend": "_privateReg"}
mp = {"extend": "_privateReg"}
my = {"extend": "_privateReg"}
pk = {"extend": "_privateReg"}
py = {"extend": "_privateReg"}  # Paraguay:https://www.iana.org/domains/root/db/py.html
com_py = {"extend": "_privateReg"}
sr = {"extend": "_privateReg"}
ke = {"extend": "_privateReg"}  # Kenia
co_ke = {"extend": "_privateReg"}

# https://www.iana.org/domains/root/db/td.html
# td = {"extend": "_privateReg"} # Chad (French: Tchad) made available for use in 1997.

tk = {"extend": "_privateReg"}
to = {"extend": "_privateReg"}  #
uy = {"extend": "_privateReg"}  # Uruguay
va = {"extend": "_privateReg"}  # This TLD has no whois server.
vu = {"extend": "_privateReg"}  # all dates 1970 , no furter relevant info
vn = {"extend": "_privateReg"}
#
zw = {"extend": "_privateReg"}  # Zimbabwe ; # This TLD has no whois server
com_zw = {"extend": "zw"}
org_zw = {"extend": "zw"}

# Nepal
np = {
    "extend": "_privateReg"
}  # This TLD has no whois server, but you can access the whois database at https://www.mos.com.np/
com_np = {"extend": "np"}

# Ecuador
ec = {"extend": "_privateReg"}
com_ec = {"extend": "ec"}
gob_ec = {"extend": "ec"}

# https://umbrella.cisco.com/blog/on-the-trail-of-malicious-dynamic-dns-domains
hopto_org = {"extend": "_privateReg"}  # dynamic dns without any whois
duckdns_org = {"extend": "_privateReg"}  # dynamic dns without any whois
# changeip_com = {"extend": "_privateReg"}  # dynamic dns without any whois
# dnsdynamic_org = {"extend": "_privateReg"}  # dynamic dns without any whois
noip_com = {"extend": "_privateReg"}  # dynamic dns without any whois
noip_org = {"extend": "_privateReg"}  # dynamic dns without any whois
# freedns_afraid_org = {"extend": "_privateReg"}  # dynamic dns without any whois
# dyndns_com = {"extend": "_privateReg"}  # dynamic dns without any whois
# sitelutions_com = {"extend": "_privateReg"}  # dynamic dns without any whois
# 3322_org = {"extend": "_privateReg"}  # dynamic dns without any whois

# https://en.wikipedia.org/wiki/.onion, a "official" fake domain
onion = {"extend": "_privateReg"}

# backend registry for domain names ending in GG, JE, and AS.
# lines may have \r actually before \n , updated all 3 domains return all nameservers
gg = {
    "domain_name": r"Domain:\s*\n\s+(.+)",
    "status": r"Domain Status:\s*\n\s+(.+)",
    "registrar": r"Registrar:\s*\n\s+(.+)",
    "name_servers": r"Name servers:\s*\r?\n(?:\s+(\S+)\r?\n)(?:\s+(\S+)\r?\n)?(?:\s+(\S+)\r?\n)?",
    "creation_date": r"Relevant dates:\s*\n\s+Registered on(.+)",
    "expiration_date": None,
    "updated_date": None,
    "registrant_country": None,
}

as_ = {"extend": "gg"}
je = {"extend": "gg"}

sn = {
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

si = {
    "domain_name": r"domain:\s+(.+)",
    "status": r"status:\s+(.+)",
    "registrar": r"registrar:\s+(.+)",
    "name_servers": r"nameserver:\s*(.+)",
    "creation_date": r"created:\s+(.+)",
    "expiration_date": r"expire:\s+(.+)",
    "updated_date": None,
    "registrant_country": None,
}

do = {"extend": "_privateReg"}
com_do = {"extend": "_privateReg"}
cx = {"extend": "com"}
dz = {"extend": "_privateReg"}
gd = {"extend": "com"}
mn = {"extend": "com"}
tl = {"extend": "com"}
gay = {"extend": "com", "_server": "whois.nic.gay"}
tt = {"extend": "_privateReg"}
mo = {
    "extend": "com",
    "creation_date": r"created on\s+(.+)",
    "expiration_date": r"expires on\s+(.+)",
    "name_servers": r"Domain name servers:\s*\-+(?:\s*(\S+)\n)(?:\s*(\S+)\n)?(?:\s*(\S+)\n)?(?:\s*(\S+)\n)?",
}
com_mo = {"extend": "mo"}
st = {
    # .ST domains can now be registered with many different competing registrars. and hence different formats
    # >>> line appears quite early, valid info after would have been suppressed with the ^>>> cleanup rule: switched off
    "extend": "com",
    "registrant_country": r"registrant-country:\s+(\S+)",
    "registrant": r"registrant-organi(?:s|z)ation:\s*(.+)\r?\n",
}

so = {"extend": "com"}
nrw = {"extend": "com"}
lat = {"extend": "com"}
realestate = {"_server": "whois.nic.realestate", "extend": "com"}
ph = {"extend": "_privateReg"}
com_ph = {"extend": "ph"}
org_ph = {"extend": "ph"}
net_ph = {"extend": "ph"}
zm = {"extend": "com"}
sy = {"extend": "_privateReg", "_server": "whois.tld.sy"}
tr = {"extend": "_privateReg"}
onl = {"extend": "com"}
blue = {"extend": "com"}
garden = {"extend": "com", "_server": "whois.nic.garden"}
promo = {"extend": "com", "_server": "whois.nic.promo"}

pyc_ = {"extend": "com"}

mn = {"extend": "com", "_server": "whois.nic.mn"}

africa = {"extend": "com", "_server": "whois.nic.africa"}

green = {"extend": "com"}

mk = {
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

observer = {"extend": "com", "_server": "whois.nic.observer"}
one = {"extend": "com", "_server": "whois.nic.one"}
page = {"extend": "com", "_server": "whois.nic.google"}

bf = {
    "extend": "com",
    "_server": "whois.nic.bf",
    "registrant": r"Registrant Name:\s?(.+)",
}
bz = {"extend": "_privateReg"}

si = {
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

sx = {"extend": "com", "_server": "whois.sx"}

tc = {
    "extend": "com",
    "_server": "whois.nic.tc",
    "domain_name": r"Domain Name:\s?(.+)",
    "registrar": r"Sponsoring Registrar:\s?(.+)",
    "creation_date": r"Creation Date:\s?(.+)",
    "expiration_date": r"Registry Expiry Date:\s?(.+)",
    "name_servers": r"Name Server:\s*(.+)\s*",
    "status": r"Domain Status:\s?(.+)",
}

wf = {
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

lk = {"extend": "_privateReg"}  # Sri Lanka, whois.nic.lk exists but does not answer
eg = {"extend": "_privateReg"}  # Egipt
com_eg = {"extend": "_privateReg"}  # Egipt

mo = {
    "extend": "com",
    "_server": "whois.monic.mo",
    "name_servers": r"Domain name servers:\s+-+\s+(\S+)\n(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?",
    "creation_date": r"Record created on (.+)",
    "expiration_date": r"Record expires on (.+)",
}

ph = {"extend": "_privateReg"}
