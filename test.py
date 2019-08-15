import whois

domains = '''
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
    google.pl
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
        w = whois.query(d, ignore_returncode=1)
        if w:
            wd = w.__dict__
            for k, v in wd.items():
                print('%20s\t"%s"' % (k, v))

for d in invalidTld.split('\n'):
    if d:
        print('-'*80)
        print(d)
        try:
            w = whois.query(d, ignore_returncode=1)
        except whois.UnknownTld as e:
            print('Caught UnknownTld Exception')
            print(e)

for d in failedParsing.split('\n'):
    if d:
        print('-'*80)
        print(d)
        try:
            w = whois.query(d, ignore_returncode=1)
        except whois.FailedParsingWhoisOutput as e:
            print('Caught FailedParsingWhoisOutput Exception')
            print(e)

for d in unknownDateFormat.split('\n'):
    if d:
        print('-'*80)
        print(d)
        try:
            w = whois.query(d, ignore_returncode=1)
        except whois.UnknownDateFormat as e:
            print('Caught UnknownDateFormat Exception')
            print(e)
