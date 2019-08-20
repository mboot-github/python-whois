import whois
from time import sleep

domains = '''
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
    google.biz
    google.info
    google.name
    google.it
    google.cz
    google.fr
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
'''

failure = list()

# domains = ''

invalidTld = '''
    bit.ly
'''

failedParsing = '''
'''

unknownDateFormat = '''
    gopro.com
'''

for d in domains.split('\n'):
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
            Error : {},
            On Domain: {}
            """.format(str(e),d)

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
            """.format(str(e),d)
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
            """.format(str(e),d)
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
            """.format(str(e),d)
            print('Caught UnknownDateFormat Exception')
            print(e)


report_str = """
Failure during test : {}
Domains : {}
""".format(len(failure),failure)
message = '\033[91m' + report_str + '\x1b[0m'
print(message)