#!/usr/bin/python3
import whois

Verbose = True

NEW_TESTS = """
    nic.ua
    zieit.edu.ua # has issues with date/time strings
    custler.com # may have issues with gethostaddr
    example.com
    abroco.me
    nic.me
    fraukesart.de # status: free
    google.ch
    google.gr
    google.hu
    google.li
    google.tk
    google.vn
"""

InvalidTld = """
    bit.ly
    google.com.vn
"""

FailedParsing = """
    vols.cat
    sylblog.xin
    google.dev
    google.com.au
    ghc.fit
    davidetson.ovh
    bretagne.bzh
    amazon.courses
    afilias.com.au
    www.google.com
    www.fsdfsdfsdfsd.google.com
"""

UnknownDateFormat = """
"""

# these are all supposed to result in data or None but no errors
DOMAINS = """
    google.bj
    dot.ml
    example.com
    mphimmoitv.com
    phimchill.tv
    netsec.ninja
    test.education
    doramy.club
    google.cl
    google.in
    google.com.ar
    google.com.co
    google.pl
    google.com.br
    digg.com
    imdb.com
    microsoft.com
    office.com
    python.org
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
    google.cat
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
    jisc.ac.uk
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
    google.sk
    youtube.com
    youtu.be
    belgium.com
    america.com
    elcomercio.pe
    terra.com.pe
    amazon.study
    google.aw
    karibu.tz
    congres.nc
    colooder.app
    bellerose.asia
    minigames.best
    timphillipsgarage.bond
    edc.click
    hisd.cloud
    medicaldata.icu
    agtaster.kiwi
    curly.red
    clubclio.shop
    agodasylumsy.top
    rans88.vip
    kubet77.win
    luminor.ee
    icee.sa
    vidange.tn
    nic.cam
    nic.gent
    nic.desi
    nic.london
    nic.tech
    nic.coop
    nic.host
    nic.online
    nic.press
    nic.site
    nic.space
    nic.store
    nic.website
    nic.frl
    nic.ooo
    nic.dealer
    nic.inc
    nic.zuerich
    nic.blog
    nic.luxury
    nic.reit
    nic.bar
    nic.rest
    nic.ceo
    nic.kred
    nic.build
    nic.fun
    nic.uno
    nic.bond
    nic.cfd
    nic.cyou
    nic.icu
    nic.sbs
    nic.best
    nic.feedback
    nic.forum
    nic.art
    nic.auto
    nic.autos
    nic.baby
    nic.beauty
    nic.boats
    nic.car
    nic.cars
    nic.college
    nic.hair
    nic.homes
    nic.makeup
    nic.monster
    nic.motorcycles
    nic.protection
    nic.quest
    nic.rent
    nic.security
    nic.skin
    nic.storage
    nic.theatre
    nic.tickets
    nic.xyz
    nic.yachts
    nic.fans
    nic.qpon
    nic.saarland
    gopro.com
    nic.bj
"""

failure = {}


def prepItem(d):
    print("-" * 80)
    print(d)


def testItem(d):
    w = whois.query(
        d,
        ignore_returncode=True,
        verbose=Verbose,
    )
    if w:
        wd = w.__dict__
        for k, v in wd.items():
            print('%20s\t"%s"' % (k, v))
    else:
        print("None")


def errorItem(d, e, what="Generic"):
    print(f"Caught {what} Exception")
    failure[d] = {"exception": what, "result": e}
    message = f"""
    Error : {e},
    On Domain: {d}
    """
    print(message)


def testDomains(aList):
    for d in sorted(aList):

        # skip empty lines
        if not d:
            continue

        # skip comments
        if d.startswith("#"):
            continue

        # skip comments behind the domain
        d = d.split("#")[0]
        d = d.strip()

        prepItem(d)
        try:
            testItem(d)
        except whois.UnknownTld as e:
            errorItem(d, e, what="UnknownTld")
        except whois.FailedParsingWhoisOutput as e:
            errorItem(d, e, what="FailedParsingWhoisOutput")
        except whois.UnknownDateFormat as e:
            errorItem(d, e, what="UnknownDateFormat")
        except whois.WhoisCommandFailed as e:
            errorItem(d, e, what="WhoisCommandFailed")
        except whois.WhoisQuotaExceeded as e:
            errorItem(d, e, what="WhoisQuotaExceeded")
        except whois.WhoisPrivateRegistry as e:
            errorItem(d, e, what="WhoisPrivateRegistry")
        except Exception as e:
            errorItem(d, e, what="Generic")


def main():

    testOnlyProblems = True

    if testOnlyProblems is False:
        print("Tld's currently supported")
        zz = whois.validTlds()
        for tld in zz:
            print(tld)

    print("\n========================================\n")
    print("Testing domains")
    testDomains(NEW_TESTS.split("\n"))

    if testOnlyProblems is False:
        print("\n========================================\n")
        testDomains(DOMAINS.split("\n"))

    print("\n========================================\n")
    testDomains(InvalidTld.split("\n"))

    print("\n========================================\n")
    testDomains(FailedParsing.split("\n"))

    print("\n========================================\n")
    testDomains(UnknownDateFormat.split("\n"))

    print(f"Failure during test : {len(failure)}")
    for i in sorted(failure.keys()):
        print(i, failure[i])


main()
