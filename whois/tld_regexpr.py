# Commercial TLD - Original Big 7
com = {
    'extend': None,

    'domain_name':		r'Domain Name:\s?(.+)',

    'registrar':		r'Registrar:\s?(.+)',
    'registrant':		r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':		r'Creation Date:\s?(.+)',
    'expiration_date':		r'Registry Expiry Date:\s?(.+)',
    'updated_date':		r'Updated Date:\s?(.+)',

    'name_servers':		r'Name Server:\s*(.+)\s*',
    'status':			r'Status:\s?(.+)',
    'emails':			r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


# United Kingdom - academic sub-domain
ac_uk = {
    'extend': 'uk',

    'domain_name':              r'Domain:\n\s?(.+)',

    'owner':                    r'Domain Owner:\n\s?(.+)',
    'registrar':                r'Registered By:\n\s?(.+)',
    'registrant':               r'Registered Contact:\n\s*(.+)',
    'expiration_date':          r'Renewal date:\n\s*(.+)',

    'updated_date':             r'Entry updated:\n\s*(.+)',
    'creation_date':            r'Entry created:\n\s?(.+)',
    'name_servers':             r'Servers:\s*(.+)\t\n\s*(.+)\t\n',

}


# United Arab Emirates
ae = {
    'extend': 'ar',
}


# Anguilla
ai = {
    'extend': 'com',
}


# Armenia
am = {
    'extend':                   None,

    'domain_name':              r'Domain name:\s+(.+)',
    'status':                   r'Status:\s(.+)',

    'registrar':                r'Registrar:\s+(.+)',
    'registrant':               r'Registrant:\s+(.+)',
    'registrant_country':       r'Registrant:\n.+\n.+\n.+\n\s+(.+)',

    'creation_date':            r'Registered:\s+(.+)',
    'expiration_date':          r'Expires:\s+(.+)',
    'updated_date':             r'Last modified:\s+(.+)',

    'name_servers':             r'DNS servers.*:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?',
}


# Amsterdam
amsterdam = {
    'extend':   'store',
}

app = {
    'extend': 'com',
}

# Argentina
ar = {
    'extend': 'com',

    'domain_name':              r'domain\s*:\s?(.+)',

    'registrar':                r'registrar:\s?(.+)',

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed\s*:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)\s*',
}

asia = {
    'extend': 'com',
}


# Austria
at = {
    'extend': 'com',

    'domain_name':              r'domain:\s?(.+)',

    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',

    'registrar':		r'registrar:\s?(.+)',
    'registrant':		r'registrant:\s?(.+)',
}


# Australia
au = {
    'extend': 'com',

    'registrar':                r'Registrar Name:\s?(.+)',

    'updated_date':             r'Last Modified:\s?(.+)'
}

aw = {
    'extend': 'nl',
}

# Banking TLD - ICANN
bank = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
}


be = {
    'extend': 'pl',

    'domain_name':              r'\nDomain:\s*(.+)',

    'registrar':                r'Company Name:\n?(.+)',

    'creation_date':            r'Registered:\s*(.+)\n',

    'status':                   r'Status:\s?(.+)',
}

best = {
    'extend': 'com',
}

biz = {
    'extend': 'com',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   None,
}

bond = {
    'extend': 'com',
}

br = {
    'extend': 'com',

    'domain_name':              r'domain:\s?(.+)',

    'registrar':                'nic.br',
    'registrant':               None,
    'owner':                    r'owner:\s?(.+)',

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

by = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s*(.+)',
    'registrar':                r'\nRegistrar:\s*(.+)',
    'registrant':               r'\nOrg:\s*(.+)',
    'registrant_country':       r'\nCountry:\s*(.+)',

    'creation_date':            r'\nCreation Date:\s*(.+)',
    'expiration_date':          r'\nExpiration Date:\s*(.+)',
    'updated_date':             r'\nUpdated Date:\s*(.+)',

    'name_servers':             r'\nName Server:\s*(.+)',
}

# Brittany (French Territory)
# Some personal data could be obfuscated at request from the registrant
bzh = {
    'extend': 'fr',

    'domain_name':          r'Domain Name:\s*(.+)',
    'registrar':            r'Registrar:\s*(.+)',
    'registrant':           r'Registrant Organization:\s*(.+)',
    'registrant_country':   r'Registrant Country:\s*(.*)',

    'creation_date':        r'Creation Date:\s*(.*)',
    'expiration_date':      r'Registry Expiry Date:\s*(.*)',
    'updated_date':         r'Updated Date:\s*(.*)',

    'name_servers':         r'Name Server:\s*(.*)',
    'status':               r'Domain Status:\s*(.*)',
}

ca = {
    'extend': 'com',
}

cat = {
    'extend': 'com',
}

cc = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

cl = {
    'extend': 'com',

    'registrar':                'nic.cl',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)\s*',
}

click = {
    'extend': 'com',
}

cloud = {
    'extend': 'com',
}

club = {
    'extend': 'com',
}

cn = {
    'extend': 'com',

    'registrar':                r'Sponsoring Registrar:\s?(.+)',
    'registrant':               r'Registrant:\s?(.+)',

    'creation_date':            r'Registration Time:\s?(.+)',
    'expiration_date':          r'Expiration Time:\s?(.+)',
}

co = {
    'extend':                   'biz',

    'status':                   r'Status:\s?(.+)',
}

com_au = {
    'extend': 'au',
}

com_tr = {
    'extend': 'com',

    'domain_name':          r'\*\* Domain Name:\s?(.+)',

    'registrar':            r'Organization Name\s+:\s?(.+)',
    'registrant':           r'\*\* Registrant:\s+?(.+)',
    'registrant_country':   None,

    'creation_date':        r'Created on..............:\s?(.+).',
    'expiration_date':      r'Expires on..............:\s?(.+).',
    'updated_date':         '',

    'name_servers':         r'\*\* Domain Servers:\n(?:(\S+)\n)(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)\n?',
    'status':               None,
}

co_il = {
    'extend': 'com',

    'domain_name':              r'domain:\s*(.+)',
    'registrar':                r'registrar name:\s*(.+)',
    'registrant':               None,
    'registrant_country':       None,

    'creation_date':            None,
    'expiration_date':          r'validity:\s*(.+)',
    'updated_date':             None,

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s*(.+)',
}

co_jp = {
    'extend': 'jp',

    'domain_name':              r'\[ドメイン名\]\s?(.+)',

    'creation_date':            r'\[登録年月\]\s?(.+)',
    'expiration_date':          r'\[状態\].+\((.+)\)',
    'updated_date':             r'\[最終更新\]\s?(.+)',
}

courses = {
    'extend': 'com'
}

cr = {
    'extend': 'cz',
}

cz = {
    'extend': 'com',

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s?(.+)',
    'registrant':               r'registrant:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+) ',
    'status':                   r'status:\s*(.+)',
}


# The .de NIC whois servers no longer provide any PII data for domains in the TLD.
# To obtains "personal" data, one must use the web interface: http://www.denic.de/en/domains/whois-service/web-whois.html
de = {
    'extend': 'com',

    'domain_name':              r'\ndomain:\s*(.+)',

    'updated_date':             r'\nChanged:\s?(.+)',

    'name_servers':             r'Nserver:\s*(.+)',
}

# Developer
dev = {
    'extend': 'com',
}

# Denmark
dk = {
    'extend': None,

    'domain_name':		r'Domain:\s?(.+)',

    'registrar':                None,
    'registrant':		r'Registrant\s*Handle:\s*\w*\s*Name:\s?(.+)',
    'registrant_country':       r'Country:\s?(.+)',

    'creation_date':		r'Registered:\s?(.+)',
    'expiration_date':		r'Expires:\s?(.+)',
    'updated_date':		None,

    'name_servers':		r'Hostname:\s*(.+)\s*',
    'status':			r'Status:\s?(.+)',
    'emails':			None,
}



download = {
    'extend': 'store',

    'name_servers':             r'Name Server:\s*(.+)\r',
    'status':                   r'Domain Status:\s*([a-zA-z]+)',
}


edu = {
    'extend': 'com',

    'registrant':               r'Registrant:\s*(.+)',

    'creation_date':            r'Domain record activated:\s?(.+)',
    'updated_date':             r'Domain record last updated:\s?(.+)',
    'expiration_date':          r'Domain expires:\s?(.+)',

    'name_servers':             r'Name Servers:\s?\t(.+)\n\t(.+)\n',
}


eu = {
    'extend': 'com',

    'registrar':                r'Name:\s?(.+)',

    'domain_name':              r'\nDomain:\s*(.+)',

    'name_servers':             r'Name servers:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?',
}


fi = {
    'extend': None,

    'domain_name':              r'domain\.+:\s?(.+)',

    'registrar':                r'registrar\.+:\s?(.+)',

    'registrant_country':       None,

    'creation_date':            r'created\.+:\s?(.+)',
    'expiration_date':          r'expires\.+:\s?(.+)',
    'updated_date':             r'modified\.+:\s?(.+)',

    'name_servers':             r'nserver\.+:\s*(.+)',
    'status':                   r'status\.+:\s?(.+)',
}

fit = {
    'extend': 'com',
}

fm = {
    'extend': 'com',
}


fr = {
    'extend': 'com',

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s*(.+)',
    'registrant':               r'contact:\s?(.+)',

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'Expiry Date:\s?(.+)',
    'updated_date':             r'last-update:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

frl = {
    'extend':   'store',
}

game = {
    'extend': 'store',
}

global_ = {
    'extend': 'store',

    'name_servers': r'Name Server: (.+)',
}


# Honduras
hn = {
    'extend': 'com',
}


# Hong Kong
hk = {
    'extend': 'com',

    'domain_name':				r'Domain Name:\s+(.+)',

    'registrar':				r'Registrar Name:\s?(.+)',
    'registrant':				r'Company English Name.*:\s?(.+)',
    'registrant_country':       None,

    'creation_date':			r'Domain Name Commencement Date:\s?(.+)',
    'expiration_date':			r'Expiry Date:\s?(.+)',
    'updated_date':				None,

    'name_servers':				r'Name Servers Information:\n\n(?:(\S+)\n)(?:(\S+)\n)(?:(\S+)\n)?(?:(\S+)\n)?\n?',
    'status':					None,
}

id_ = {
    'extend': 'com',

    'registrar':                r'Sponsoring Registrar Organization:\s?(.+)',

    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)$',
}

icu = {
    'extend': 'com',
}

# Ireland
ie = {
    'extend': 'com',
}

im = {
    'domain_name':              r'Domain Name:\s+(.+)',
    'status':                   None,

    'registrar':                None,
    'registrant_country':       None,

    'creation_date':            '',
    'expiration_date':          r'Expiry Date:\s?(.+)',
    'updated_date':             '',

    'name_servers':             r'Name Server:(.+)',
}

in_ = {
    'extend': 'com',
}

info = {
    'extend': 'com',
}

ink = {
    'extend': 'store',
}

io = {
    'extend': 'com',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
}


ir = {
    'extend': None,

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                'nic.ir',

    'registrant_country':       None,

    'creation_date':            None,
    'status':                   None,

    'expiration_date':          r'expire-date:\s?(.+)',
    'updated_date':             r'last-updated:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)\s*',
}


is_ = {
    'domain_name':              r'domain:\s?(.+)',

    'registrar':                None,
    'registrant':               r'registrant:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             None,

    'name_servers':             r'nserver:\s?(.+)',
    'status':                   None,
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


it = {
    'extend': 'com',

    'domain_name':              r'Domain:\s?(.+)',
    'registrar':                r'Registrar\s*Organization:\s*(.+)',
    'registrant':               r'Registrant\s*Organization:\s*(.+)',

    'creation_date':            r'Created:\s?(.+)',
    'expiration_date':          r'Expire Date:\s?(.+)',
    'updated_date':             r'Last Update:\s?(.+)',

    'name_servers':             r'Nameservers\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

# The Japanese whois servers always return English unless a Japanese locale is specified in the user's LANG environmental variable.
# See: https://www.computerhope.com/unix/uwhois.htm
# Additionally, whois qeuries can explicitly request english:
# 	To suppress Japanese output, add'/e' at the end of command, e.g. 'whois -h whois.jprs.jp xxx/e'.
#
jp = {
    'domain_name':              r'\[Domain Name\]\s?(.+)',

#    'registrar':                None,
    'registrar':                r'\[ (.+) database provides information on network administration. Its use is    \]',
    'registrant':               r'\[Registrant\]\s?(.+)',
    'registrant_country':       None,

#    'creation_date':            r'\[登録年月日\]\s?(.+)',
#    'expiration_date':          r'\[有効期限\]\s?(.+)',
#    'updated_date':             r'\[最終更新\]\s?(.+)',
    'creation_date':            r'\[Created on\]\s?(.+)',
    'expiration_date':          r'\[Expires on\]\s?(.+)',
    'updated_date':             r'\[Last Updated\]\s?(.+)',

    'name_servers':             r'\[Name Server\]\s*(.+)',
#    'status':                   r'\[状態\]\s?(.+)',
    'status':                   r'\[Status\]\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

# The Japanese whois servers always return English unless a Japanese locale is specified in the user's LANG environmental variable.
# See: https://www.computerhope.com/unix/uwhois.htm
# Additionally, whois qeuries can explicitly request english:
# 	To suppress Japanese output, add'/e' at the end of command, e.g. 'whois -h whois.jprs.jp xxx/e'.
#
co_jp = {
    'extend': 'jp',

#    'domain_name':              r'\[ドメイン名\]\s?(.+)',
    'domain_name':              r'\[Domain Name\]\s?(.+)',

#    'creation_date':            r'\[登録年月\]\s?(.+)',
#    'expiration_date':          r'\[状態\].+\((.+)\)',
#    'updated_date':             r'\[最終更新\]\s?(.+)',
    'creation_date':            r'\[Registered Date\]\s?(.+)',
    'expiration_date':          None,
    'updated_date':             r'\[Last Update\]\s?(.+)',

    'status':                   r'\[State\]\s?(.+)',
}

# All Japanese Sub-TLDs. See: https://jprs.co.jp/en/jpdomain.html
ne_jp = {
    'extend': 'co_jp'
}

or_jp = {
    'extend': 'co_jp'
}

go_jp = {
    'extend': 'co_jp'
}

ac_jp = {
    'extend': 'co_jp'
}

ad_jp = {
    'extend': 'co_jp'
}

ed_jp = {
    'extend': 'co_jp'
}

gr_jp = {
    'extend': 'co_jp'
}

lg_jp = {
    'extend': 'co_jp'
}

geo_jp = {
    'extend': 'co_jp'
}

kiwi = {
    'extend': 'com',
}

kr = {
    'extend': 'com',

    'domain_name':              r'Domain Name\s*:\s?(.+)',

    'registrar':                r'Authorized Agency\s*:\s*(.+)',
    'registrant':               r'Registrant\s*:\s*(.+)',

    'creation_date':            r'Registered Date\s*:\s?(.+)',
    'expiration_date':          r'Expiration Date\s*:\s?(.+)',
    'updated_date':             r'Last Updated Date\s*:\s?(.+)',

    'status':                   r'status\s*:\s?(.+)',
}


kz = {
    'extend': None,

    'domain_name':              r'Domain name\.+:\s(.+)',

    'registrar':                r'Current Registar:\s(.+)',
    'registrant_country':       r'Country\.+:\s?(.+)',

    'expiration_date':          None,
    'creation_date':            r'Domain created:\s(.+)',
    'updated_date':             r'Last modified :\s(.+)',

    'name_servers':             r'server.*:\s(.+)',
    'status':                   r'Domain status :\s?(.+)',
}

link = {
    'extend': 'store',
}

lt = {
    'extend': 'com',

    'domain_name':              r'Domain:\s?(.+)',

    'creation_date':            r'Registered:\s?(.+)',
    'expiration_date':          r'Expires:\s?(.+)',

    'name_servers':             r'Nameserver:\s*(.+)\s*',
    'status':                   r'\nStatus:\s?(.+)',
}

lv = {
    'extend': 'ru',

    'creation_date':            r'Registered:\s*(.+)\n',
    'updated_date':             r'Changed:\s*(.+)\n',

    'status':                   r'Status:\s?(.+)',
}

me = {
    'extend': 'biz',

    'creation_date':            r'Domain Create Date:\s?(.+)',
    'expiration_date':          r'Domain Expiration Date:\s?(.+)',
    'updated_date':             r'Domain Last Updated Date:\s?(.+)',

    'name_servers':             r'Nameservers:\s?(.+)',
    'status':                   r'Domain Status:\s?(.+)',
}

ml = {
    'extend': 'com',

    'domain_name':              r'Domain name:\s*([^(i|\n)]+)',

    'registrar':                r'(?<=Owner contact:\s)[\s\S]*?Organization:(.*)',
    'registrant_country':       r'(?<=Owner contact:\s)[\s\S]*?Country:(.*)',
    'registrant':               r'(?<=Owner contact:\s)[\s\S]*?Name:(.*)',

    'creation_date':            r'Domain registered: *(.+)',
    'expiration_date':          r'Record will expire on: *(.+)',

    'name_servers':             r'Domain Nameservers:\s*(.+)\n\s*(.+)\n',

    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

mobi = {
    'extend': 'com',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}


mx = {
    'domain_name':              r'Domain Name:\s?(.+)',

    'registrant':               r'Registrant:\n\s*(.+)',
    'registrar':                r'Registrar:\s?(.+)',

    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)',

    'name_servers':             r'\sDNS:\s*(.+)',
}


name = {
    'extend':                   'com',

    'status':                   r'Domain Status:\s?(.+)',
}


# New-Caledonia (French Territory)
nc = {
    'extend': 'fr',

    'domain_name':          r'Domain\s*:\s(.+)',
    'registrar':            r'Registrar\s*:\s(.+)',
    'registrant':           r'Registrant name\s*:\s(.+)',
    'registrant_country':   None,

    'creation_date':        r'Created on\s*:\s(.*)',
    'expiration_date':      r'Expires on\s*:\s(.*)',
    'updated_date':         r'Last updated on\s*:\s(.*)',

    'name_servers':         r'Domain server [0-9]{1,}\s*:\s(.*)',
    'status':               None,
}

net = {
    'extend': 'com',
}


nl = {
    'extend': 'com',

    'expiration_date':          None,
    'registrant_country':       None,

    'domain_name':              r'Domain name:\s?(.+)',
    'name_servers':             (
        r'''(?x:
            Domain\ nameservers:[ \t]*\n
            (?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n       # ns1.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [AAAA?]
            # Don't check for final LF; there might be even more records..
        )'''),
    'reseller':                 r'Reseller:\s?(.+)',
    'abuse_contact':            r'Abuse Contact:\s?(.+)',
}

# Norway
no = {
    'extend': None,

    'domain_name':		r'Domain Name\.+:\s?(.+)',

    'registrar':		r'Registrar Handle\.+:\s?(.+)',
    'registrant':		None,
    'registrant_country':       None,

    'creation_date':		r'Created:\s?(.+)',
    'expiration_date':		None,
    'updated_date':		r'Last Updated:\s?(.+)',

    'name_servers':		r'Name Server Handle\.+:\s*(.+)\s*',
    'status':			None,
    'emails':			None,
}


nu = {
    'extend': 'se',
}


nyc = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}


nz = {
    'extend': None,

    'domain_name':              r'domain_name:\s?(.+)',
    'registrar':                r'registrar_name:\s?(.+)',
    'registrant':               r'registrant_contact_name:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'domain_dateregistered:\s?(.+)',
    'expiration_date':          r'domain_datebilleduntil:\s?(.+)',
    'updated_date':             r'domain_datelastmodified:\s?(.+)',

    'name_servers':             r'ns_name_[0-9]{2}:\s?(.+)',
    'status':                   r'query_status:\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


online = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}



org = {
    'extend': 'com',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nLast Updated On:\s?(.+)',

    'name_servers':             r'Name Server:\s?(.+)\s*',
}

ovh = {
    'extend': 'com',
}

pe = {
    'extend': 'com',

    'registrant':				r'Registrant Name:\s?(.+)',

    'admin':                    r'Admin Name:\s?(.+)',
}

pharmacy = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'status:\s?(.+)',
}

pl = {
    'extend': 'uk',

    'registrar':                r'\nREGISTRAR:\s*(.+)\n',

    'creation_date':            r'\ncreated:\s*(.+)\n',
    'updated_date':             r'\nlast modified:\s*(.+)\n',
    'expiration_date':          r'\noption expiration date:\s*(.+)\n',

    'name_servers':             r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status':                   r'\nStatus:\n\s*(.+)',
}


press = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

pro = {
    'extend': 'com',
}

pt = {
    'extend': 'com',

    'domain_name':              r'Domain:\s?(.+)',

    'registrar':                None,

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             None,

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s?(.+)',
}


pw = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

red = {
    'extend': 'com',
}

rest = {
    'extend':                   'store',

    'status':                   r'Domain Status:\s*(.+)',
}

ru = {
    'extend': 'com',

    'domain_name':              r'\ndomain:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',
}

ru_rf = {
    'extend': 'com',

    'domain_name':              r'\ndomain:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',
}


security = {
    'extend': 'store',
}

sh = {
    'extend': 'com',

    'registrant':              r'\nRegistrant Organization:\s?(.+)',

    'expiration_date':         r'\nRegistry Expiry Date:\s*(.+)',

    'status':                  r'\nDomain Status:\s?(.+)',
}

shop = {
    'extend': 'com',
}

site = {
    'extend': 'store',
}

se = {
    'extend': None,

    'domain_name':              r'domain:\s?(.+)',

    'registrar':                r'registrar:\s?(.+)',

    'registrant_country':       None,

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'modified:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}


# Singapore - Commercial sub-domain
com_sg = {
    'extend': None,

    'domain_name':		r'Domain Name:\s?(.+)',

    'registrar':		r'Registrar:\s?(.+)',
    'registrant':		r'Registrant:\n\n\s?Name:\s?(.+)',
    'registrant_country':       None,

    'creation_date':		r'Creation Date:\s?(.+)',
    'expiration_date':		r'Expiration Date:\s?(.+)',
    'updated_date':		r'Modified Date:\s?(.+)',

    'name_servers':		r'Name Servers:\s*(.+)\s*',
    'status':			None,

    'emails':			r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


# Slovakia
sk = {
    'extend': 'com',

    'domain_name':				r'Domain:\s?(.+)',

    'creation_date':			r'Created:\s?(.+)',
    'expiration_date':			r'Valid Until:\s?(.+)',
    'updated_date':				r'Updated:\s?(.+)',

    'name_servers':				r'Nameserver:\s*(.+)\r',
    'registrant':				r'Contact:\s?(.+)',
    'registrant_country':       r'Country Code:\s?(.+)\nRegistrar:'
}


space = {
    'extend': 'store',
}

store = {
    'extend': 'com',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

study = {
    'extend': 'com'
}

tech = {
    'extend': 'store',
}


tel = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}


# Thailand - Commercial sub-domain
co_th = {
    'extend': 'com',

    'registrant':		r'Domain Holder Organization:\s?(.+)',
    'registrant_country':       r'Domain Holder Country:\s?(.+)',

    'creation_date':		r'Created date:\s?(.+)',
    'expiration_date':		r'Exp date:\s?(.+)',
    'updated_date':		r'Updated date:\s?(.+)',
}


theatre = {
    'extend': 'store',
}

tickets = {
    'extend': 'store',
}

top = {
    'extend': 'com',
}

trade = {
    'extend': 'store',
}

tv = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

tz = {
    'domain_name':              r'\ndomain:\s*(.+)', 
    'registrar':                r'\nregistrar:\s?(.+)',
    'registrant':               r'\nregistrant:\s*(.+)',
    'registrant_country':       None,
    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'\nchanged:\s*(.+)',
    'status':                   None,
    'name_servers':             r'\nnserver:\s*(.+)',
}

ua = {
    'extend': 'com',

    'domain_name':              r'\ndomain:\s*(.+)',

    'registrar':                r'\nregistrar:\s*(.+)',
    'registrant_country':       r'\ncountry:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\nexpires:\s*(.+)',
    'updated_date':             r'\nmodified:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstatus:\s*(.+)',
}

uk = {
    'extend': 'com',

    'registrant':               r'Registrant:\n\s*(.+)',

    'creation_date':            r'Registered on:\s*(.+)',
    'expiration_date':          r'Expiry date:\s*(.+)',
    'updated_date':             r'Last updated:\s*(.+)',

    'name_servers':             r'Name Servers:\s*(.+)\s*',
    'status':                   r'Registration status:\n\s*(.+)',
}

us = {
    'extend': 'name',
}

uz = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

vip = {
    'extend': 'com',
}

website = {
    'extend': 'store',
}

wiki = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

win = {
    'extend': 'com',
}

work = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
}

xin = {
    'extend': 'com',
}

xyz = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

za = {
    'extend': 'com',
}

ax = {
    'extend': 'com',
    'domain_name':              r'domain...............:\s?(.+)',

    'registrar':                r'registrar............:\s?(.+)',

    'creation_date':            r'created..............:\s?(.+)',
    'expiration_date':          r'expires..............:\s?(.+)',
    'updated_date':             r'Information Updated:\s?(.+)',
}

gy = {
     'extend': 'com',
}

# Multiple initialization
ca = rw = mu = bank


# Registry operator: donuts.domains
# WHOIS server: whois.donuts.co
_donuts = {
    'extend': 'com',

    'registrant':               r'Registrant Organization:\s?(.+)',

    'status':                   r'Domain Status:\s?(.+)',
}

academy = {'extend': '_donuts'}
accountants = {'extend': '_donuts'}
actor = {'extend': '_donuts'}
agency = {'extend': '_donuts'}
airforce = {'extend': '_donuts'}
apartments = {'extend': '_donuts'}
army = {'extend': '_donuts'}
associates = {'extend': '_donuts'}
attorney = {'extend': '_donuts'}
auction = {'extend': '_donuts'}
band = {'extend': '_donuts'}
bargains = {'extend': '_donuts'}
bike = {'extend': '_donuts'}
bingo = {'extend': '_donuts'}
boutique = {'extend': '_donuts'}
builders = {'extend': '_donuts'}
business = {'extend': '_donuts'}
cab = {'extend': '_donuts'}
cafe = {'extend': '_donuts'}
camera = {'extend': '_donuts'}
camp = {'extend': '_donuts'}
capital = {'extend': '_donuts'}
cards = {'extend': '_donuts'}
care = {'extend': '_donuts'}
careers = {'extend': '_donuts'}
cash = {'extend': '_donuts'}
casino = {'extend': '_donuts'}
catering = {'extend': '_donuts'}
center = {'extend': '_donuts'}
charity = {'extend': '_donuts'}
chat = {'extend': '_donuts'}
cheap = {'extend': '_donuts'}
church = {'extend': '_donuts'}
city = {'extend': '_donuts'}
claims = {'extend': '_donuts'}
cleaning = {'extend': '_donuts'}
clinic = {'extend': '_donuts'}
clothing = {'extend': '_donuts'}
coach = {'extend': '_donuts'}
codes = {'extend': '_donuts'}
coffee = {'extend': '_donuts'}
community = {'extend': '_donuts'}
company = {'extend': '_donuts'}
computer = {'extend': '_donuts'}
condos = {'extend': '_donuts'}
construction = {'extend': '_donuts'}
consulting = {'extend': '_donuts'}
contact = {'extend': '_donuts'}
contractors = {'extend': '_donuts'}
cool = {'extend': '_donuts'}
coupons = {'extend': '_donuts'}
credit = {'extend': '_donuts'}
creditcard = {'extend': '_donuts'}
cruises = {'extend': '_donuts'}
dance = {'extend': '_donuts'}
dating = {'extend': '_donuts'}
deals = {'extend': '_donuts'}
degree = {'extend': '_donuts'}
delivery = {'extend': '_donuts'}
democrat = {'extend': '_donuts'}
dental = {'extend': '_donuts'}
dentist = {'extend': '_donuts'}
diamonds = {'extend': '_donuts'}
digital = {'extend': '_donuts'}
direct = {'extend': '_donuts'}
directory = {'extend': '_donuts'}
discount = {'extend': '_donuts'}
doctor = {'extend': '_donuts'}
dog = {'extend': '_donuts'}
domains = {'extend': '_donuts'}
education = {'extend': '_donuts'}
email = {'extend': '_donuts'}
energy = {'extend': '_donuts'}
engineer = {'extend': '_donuts'}
engineering = {'extend': '_donuts'}
enterprises = {'extend': '_donuts'}
equipment = {'extend': '_donuts'}
estate = {'extend': '_donuts'}
events = {'extend': '_donuts'}
exchange = {'extend': '_donuts'}
expert = {'extend': '_donuts'}
exposed = {'extend': '_donuts'}
express = {'extend': '_donuts'}
fail = {'extend': '_donuts'}
family = {'extend': '_donuts'}
fan = {'extend': '_donuts'}
farm = {'extend': '_donuts'}
finance = {'extend': '_donuts'}
financial = {'extend': '_donuts'}
fish = {'extend': '_donuts'}
fitness = {'extend': '_donuts'}
flights = {'extend': '_donuts'}
florist = {'extend': '_donuts'}
football = {'extend': '_donuts'}
forsale = {'extend': '_donuts'}
foundation = {'extend': '_donuts'}
fund = {'extend': '_donuts'}
furniture = {'extend': '_donuts'}
futbol = {'extend': '_donuts'}
fyi = {'extend': '_donuts'}
gallery = {'extend': '_donuts'}
games = {'extend': '_donuts'}
gifts = {'extend': '_donuts'}
gives = {'extend': '_donuts'}
glass = {'extend': '_donuts'}
gmbh = {'extend': '_donuts'}
gold = {'extend': '_donuts'}
golf = {'extend': '_donuts'}
graphics = {'extend': '_donuts'}
gratis = {'extend': '_donuts'}
gripe = {'extend': '_donuts'}
group = {'extend': '_donuts'}
guide = {'extend': '_donuts'}
guru = {'extend': '_donuts'}
haus = {'extend': '_donuts'}
healthcare = {'extend': '_donuts'}
hockey = {'extend': '_donuts'}
holdings = {'extend': '_donuts'}
holiday = {'extend': '_donuts'}
hospital = {'extend': '_donuts'}
house = {'extend': '_donuts'}
immo = {'extend': '_donuts'}
immobilien = {'extend': '_donuts'}
industries = {'extend': '_donuts'}
institute = {'extend': '_donuts'}
insure = {'extend': '_donuts'}
international = {'extend': '_donuts'}
investments = {'extend': '_donuts'}
irish = {'extend': '_donuts'}
jetzt = {'extend': '_donuts'}
jewelry = {'extend': '_donuts'}
kaufen = {'extend': '_donuts'}
kitchen = {'extend': '_donuts'}
land = {'extend': '_donuts'}
lawyer = {'extend': '_donuts'}
lease = {'extend': '_donuts'}
legal = {'extend': '_donuts'}
life = {'extend': '_donuts'}
lighting = {'extend': '_donuts'}
limited = {'extend': '_donuts'}
limo = {'extend': '_donuts'}
live = {'extend': '_donuts'}
loans = {'extend': '_donuts'}
ltd = {'extend': '_donuts'}
maison = {'extend': '_donuts'}
management = {'extend': '_donuts'}
market = {'extend': '_donuts'}
marketing = {'extend': '_donuts'}
mba = {'extend': '_donuts'}
media = {'extend': '_donuts'}
memorial = {'extend': '_donuts'}
moda = {'extend': '_donuts'}
money = {'extend': '_donuts'}
mortgage = {'extend': '_donuts'}
movie = {'extend': '_donuts'}
navy = {'extend': '_donuts'}
network = {'extend': '_donuts'}
news = {'extend': '_donuts'}
ninja = {'extend': '_donuts'}
partners = {'extend': '_donuts'}
parts = {'extend': '_donuts'}
photography = {'extend': '_donuts'}
photos = {'extend': '_donuts'}
pictures = {'extend': '_donuts'}
pizza = {'extend': '_donuts'}
place = {'extend': '_donuts'}
plumbing = {'extend': '_donuts'}
plus = {'extend': '_donuts'}
productions = {'extend': '_donuts'}
properties = {'extend': '_donuts'}
pub = {'extend': '_donuts'}
recipes = {'extend': '_donuts'}
rehab = {'extend': '_donuts'}
reise = {'extend': '_donuts'}
reisen = {'extend': '_donuts'}
rentals = {'extend': '_donuts'}
repair = {'extend': '_donuts'}
report = {'extend': '_donuts'}
republican = {'extend': '_donuts'}
restaurant = {'extend': '_donuts'}
reviews = {'extend': '_donuts'}
rip = {'extend': '_donuts'}
rocks = {'extend': '_donuts'}
run = {'extend': '_donuts'}
sale = {'extend': '_donuts'}
salon = {'extend': '_donuts'}
sarl = {'extend': '_donuts'}
school = {'extend': '_donuts'}
schule = {'extend': '_donuts'}
services = {'extend': '_donuts'}
shoes = {'extend': '_donuts'}
shopping = {'extend': '_donuts'}
show = {'extend': '_donuts'}
singles = {'extend': '_donuts'}
soccer = {'extend': '_donuts'}
social = {'extend': '_donuts'}
software = {'extend': '_donuts'}
solar = {'extend': '_donuts'}
solutions = {'extend': '_donuts'}
studio = {'extend': '_donuts'}
style = {'extend': '_donuts'}
supplies = {'extend': '_donuts'}
supply = {'extend': '_donuts'}
support = {'extend': '_donuts'}
surgery = {'extend': '_donuts'}
systems = {'extend': '_donuts'}
tax = {'extend': '_donuts'}
taxi = {'extend': '_donuts'}
team = {'extend': '_donuts'}
technology = {'extend': '_donuts'}
tennis = {'extend': '_donuts'}
theater = {'extend': '_donuts'}
tienda = {'extend': '_donuts'}
tips = {'extend': '_donuts'}
tires = {'extend': '_donuts'}
today = {'extend': '_donuts'}
tools = {'extend': '_donuts'}
tours = {'extend': '_donuts'}
town = {'extend': '_donuts'}
toys = {'extend': '_donuts'}
training = {'extend': '_donuts'}
travel = {'extend': '_donuts'}
university = {'extend': '_donuts'}
vacations = {'extend': '_donuts'}
ventures = {'extend': '_donuts'}
vet = {'extend': '_donuts'}
viajes = {'extend': '_donuts'}
video = {'extend': '_donuts'}
villas = {'extend': '_donuts'}
vin = {'extend': '_donuts'}
vision = {'extend': '_donuts'}
voyage = {'extend': '_donuts'}
watch = {'extend': '_donuts'}
wine = {'extend': '_donuts'}
works = {'extend': '_donuts'}
world = {'extend': '_donuts'}
wtf = {'extend': '_donuts'}
zone = {'extend': '_donuts'}
