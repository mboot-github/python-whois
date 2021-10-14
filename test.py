#!/usr/bin/python3
import whois

DOMAINS = '''
    dot.ml
    netsec.ninja
    test.education
    doramy.club
    google.cl
    google.in
    google.com.ar
    google.com.co
    google.pl
    google.com.br
    www.google.com
    www.fsdfsdfsdfsd.google.com
    digg.com
    imdb.com
    microsoft.com
    www.google.org
    ddarko.org
    google.net
    www.asp.net
    www.ddarko.pl
    google.co.uk
    google.jp
    www.google.co.jp
    google.io
    google.co
    google.de
    yandex.ru
    google.us
    google.eu
    google.me
    google.be
    google.lt
    google.biz
    google.info
    google.name
    google.it
    google.cz
    google.fr
    google.nl
    dfsdfsfsdf
    test.ez.lv
    google.store
    kono.store
    wonder.store
    viacom.tech
    google.tech
    google.space
    loop.space
    bloom.space
    invr.space
    buzzi.space
    theobservatory.space
    google.security
    pep.security
    token.security
    juniper.security
    ci.security
    in.security
    autobuyer.site
    emeralds.site
    darkops.site
    google.site
    manniswindows.site
    google.website
    discjockey.website
    anthropology.website
    livechat.website
    google.tickets
    google.theatre
    google.xyz
    google.tel
    google.tv
    google.cc
    google.nyc
    google.pw
    google.online
    google.wiki
    google.press
    google.se
    google.nu
    google.fi
    google.is
    afilias.com.au
    jisc.ac.uk
    google.com.au
    register.bank
    yandex.ua
    google.ca
    google.mu
    google.rw
    tut.by
    guinness.ie
    google.com.tr
    google.sale
    google.link
    google.game
    google.trade
    google.ink
    google.pub
    google.im
    google.am
    google.fm
    google.hk
    google.cr
    google.global
    google.co.il
    google.pt
    elcomercio.pe
    terra.com.pe
    amazon.study
    amazon.courses
    google.aw
    esa.int
    google.ai
    nic.fund
    bit.ly
    google.hr
    google.ng
    nic.events
    nic.gov
    nic.nrw
    nic.aero
    nic.report
    google.ch
    nic.google
    nic.gle
    nic.energy
    google.sk
    google.no
    google.tl
    nic.community
    google.bg
'''

failure = list()

# domains = ''

invalidTld = '''
    google.sr
'''

failedParsing = '''
'''

unknownDateFormat = '''
    gopro.com
'''

for d in DOMAINS.split('\n'):
    if d:
        print('-'*80)
        print(d)
        try:
            w = whois.query(d, ignore_returncode=1)
            if w:
                wd = w.__dict__
                for k, v in wd.items():
                    print('%20s\t"%s"' % (k, v))
        except Exception as e:
            failure.append(d)
            message = """
            Exception Class: {},
            Error : {},
            On Domain: {}
            """.format(type(e).__name__, str(e), d)
            print(message)

for d in invalidTld.split('\n'):
    if d:
        print('-'*80)
        print(d)
        try:
            w = whois.query(d, ignore_returncode=1)
        except whois.UnknownTld as e:
            failure.append(d)
            message = """
            Error : {},
            On Domain: {}
            """.format(str(e), d)
            print('Caught UnknownTld Exception')
            print(e)

for d in failedParsing.split('\n'):
    if d:
        print('-'*80)
        print(d)
        try:
            w = whois.query(d, ignore_returncode=1)
        except whois.FailedParsingWhoisOutput as e:
            failure.append(d)
            message = """
            Error : {},
            On Domain: {}
            """.format(str(e), d)
            print('Caught FailedParsingWhoisOutput Exception')
            print(e)

for d in unknownDateFormat.split('\n'):
    if d:
        print('-'*80)
        print(d)
        try:
            w = whois.query(d, ignore_returncode=1)
        except whois.UnknownDateFormat as e:
            failure.append(d)
            message = """
            Error : {},
            On Domain: {}
            """.format(str(e), d)
            print('Caught UnknownDateFormat Exception')
            print(e)


report_str = """
Failure during test : {}
Domains : {}
""".format(len(failure), failure)
message = '\033[91m' + report_str + '\x1b[0m'
print(message)
