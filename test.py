#!/usr/bin/python3
import whois

Verbose = True

NEW_TESTS = """
    # https://www.rfc-editor.org/rfc/rfc6761.html
    # The domains "example.", "example.com.", "example.net.", "example.org.",
    # and any names falling within those domains,
    # are special in the following ways:

    # TODO future:
    # example.com #  All example names are registered in perpetuity to IANA:

    # OK NOW:
    # abroco.me
    # wp.pl

    # New TLD
    whois.aero
    nic.cd
    register.bg
    nic.ba
    whois.az
    bit.ly
    nic.re
    nic.pet
    gooogle.onion
    twnic.net.tw
    nic.td
    net.pk # no whois server
    mynic.my # No answers
    nic.moe
    nic.mg
    nic.love
    nic.es
    google.cf
    google.bo
    thnic.co.th
    google.ke
    nic.br
    nic.zw
    nic.ec
    nusurionuy5ff.at
    phila.ac.ug # has a None date
    nic.ma # error in ma: missing extend
    merlin.ua # Unknown date format: '2006-03-30 13:26:31+03:00'
    www.google.co.jp

    # test next item if first one has no whois data
    dns1.carnet.hr # get actual info from carnet.hr

    # now a secondlevel tld
    ns1.cfi.co.ug # should go to: cfi.co.ug but not to: co.ug
"""

PrivateRegistry = """
    google.al
    google.ch
    google.cw
    google.ga
    google.gr
    google.hu
    google.li
    google.mp
    google.sr
    google.tk
    google.to
    google.vn
"""

InvalidTld = """
"""

FailedParsing = """
    afilias.com.au
    amazon.courses
    bretagne.bzh
    davidetson.ovh
    ghc.fit
    google.com.au
    google.dev
    sylblog.xin
    vols.cat
    www.fsdfsdfsdfsd.google.com
    www.google.com
"""

UnknownDateFormat = """
"""

# these are all supposed to result in data or None but no errors
DOMAINS = """
    abroco.me
    agodasylumsy.top
    agtaster.kiwi
    amazon.study
    america.com
    anthropology.website
    autobuyer.site
    belgium.com
    bellerose.asia
    bloom.space
    buzzi.space
    ci.security
    clubclio.shop
    colooder.app
    congres.nc
    curly.red
    custler.com # may have issues with gethostaddr
    darkops.site
    ddarko.org
    digg.com
    discjockey.website
    doramy.club
    dot.ml
    edc.click
    elcomercio.pe
    emeralds.site
    example.com
    fraukesart.de # status: free
    google.am
    google.aw
    google.be
    google.biz
    google.bj
    google.ca
    google.cat
    google.cc
    google.cl
    google.co
    google.co.il
    google.com.ar
    google.com.br
    google.com.co
    google.com.tr
    google.co.uk
    google.cr
    google.cz
    google.de
    google.eu
    google.fi
    google.fm
    google.fr
    google.game
    google.global
    google.hk
    google.im
    google.in
    google.info
    google.ink
    google.io
    google.is
    google.it
    google.jp
    google.link
    google.lt
    google.me
    google.mu
    google.name
    google.net
    google.nl
    google.nu
    google.nyc
    google.online
    google.pl
    google.press
    google.pt
    google.pub
    google.pw
    google.rw
    google.sale
    google.se
    google.security
    google.site
    google.sk
    google.space
    google.store
    google.tech
    google.tel
    google.theatre
    google.tickets
    google.trade
    google.tv
    google.us
    google.website
    google.wiki
    google.xyz
    gopro.com
    guinness.ie
    hisd.cloud
    icee.sa
    imdb.com
    in.security
    invr.space
    jisc.ac.uk
    juniper.security
    karibu.tz
    kono.store
    kubet77.win
    livechat.website
    loop.space
    luminor.ee
    manniswindows.site
    medicaldata.icu
    microsoft.com
    minigames.best
    mphimmoitv.com
    netsec.ninja
    nic.art
    nic.auto
    nic.autos
    nic.baby
    nic.bar
    nic.beauty
    nic.best
    nic.bj
    nic.blog
    nic.boats
    nic.bond
    nic.build
    nic.cam
    nic.car
    nic.cars
    nic.ceo
    nic.cfd
    nic.college
    nic.coop
    nic.cyou
    nic.dealer
    nic.desi
    nic.fans
    nic.feedback
    nic.forum
    nic.frl
    nic.fun
    nic.gent
    nic.hair
    nic.homes
    nic.host
    nic.icu
    nic.inc
    nic.kred
    nic.london
    nic.luxury
    nic.makeup
    nic.me
    nic.monster
    nic.motorcycles
    nic.online
    nic.ooo
    nic.press
    nic.protection
    nic.qpon
    nic.quest
    nic.reit
    nic.rent
    nic.rest
    nic.saarland
    nic.sbs
    nic.security
    nic.site
    nic.skin
    nic.space
    nic.storage
    nic.store
    nic.tech
    nic.theatre
    nic.tickets
    nic.ua
    nic.uno
    nic.website
    nic.xyz
    nic.yachts
    nic.zuerich
    office.com
    pep.security
    phimchill.tv
    python.org
    rans88.vip
    register.bank
    terra.com.pe
    test.education
    test.ez.lv
    theobservatory.space
    timphillipsgarage.bond
    token.security
    tut.by
    viacom.tech
    vidange.tn
    wonder.store
    www.asp.net
    www.ddarko.pl
    www.google.co.jp
    www.google.org
    yandex.ru
    yandex.ua
    youtu.be
    youtube.com
    zieit.edu.ua # has issues with date/time strings

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
    for d in aList:

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
    # ----------------------------
    testAllTlds = True
    testOnlyProblems = True
    testOnlyNew = True

    # ----------------------------
    if testAllTlds is True:
        print("Tld's currently supported")
        zz = whois.validTlds()
        for tld in zz:
            print(tld)

    print("\n========================================\n")
    print("Testing")
    testDomains(NEW_TESTS.split("\n"))

    if testOnlyNew is False:
        if testOnlyProblems is False:
            print("\n========================================\n")
            testDomains(DOMAINS.split("\n"))

        print("\n========================================\n")
        testDomains(PrivateRegistry.split("\n"))

        print("\n========================================\n")
        testDomains(InvalidTld.split("\n"))

        print("\n========================================\n")
        testDomains(FailedParsing.split("\n"))

        print("\n========================================\n")
        testDomains(UnknownDateFormat.split("\n"))

        print(f"Failure during test : {len(failure)}")

    print("\n# ========================")
    for i in sorted(failure.keys()):
        print(i, failure[i])


main()
