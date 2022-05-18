# whois
A Python package for retrieving WHOIS information of domains.

## Features
 * Python wrapper for Linux "whois" command.
 * Simple interface to access parsed WHOIS data for a given domain.
 * Able to extract data for all the popular TLDs (com, org, net, biz, info, pl, jp, uk, nz,  ...).
 * Query a WHOIS server directly instead of going through an intermediate web service like many others do.
 * Works with Python 3.x.
 * All dates as datetime objects.
 * Possibility to cache results.

## Help Wanted
Your contributions are welcome, look for the Help wanted tag https://github.com/DannyCork/python-whois/labels/help%20wanted

## Usage example

Install `whois` package from your distribution (e.g apt install whois)

```
$pip install whois

>>> import whois
>>> domain = whois.query('google.com')

>>> print(domain.__dict__)
{
	'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
	'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
	'registrar': 'MARKMONITOR INC.',
	'name': 'google.com',
	'creation_date': datetime.datetime(1997, 9, 15, 0, 0)
}

>>> print(domain.name)
google.com

>>> print(domain.expiration_date)
2020-09-14 00:00:00
```

## ccTLD & TLD support
```
.ac.uk
.am
.amsterdam
.app
.ar
.asia
.at
.au
.aw
.bank
.be
.best
.biz
.bond
.br
.by
.bzh
.ca
.cat
.cc
.cl
.click
.cloud
.club
.cn
.co
.co.il
.co.jp
.com
.com.au
.com.tr
.courses
.cr
.cz
.de
.dev
.download
.edu
.education
.eu
.fi
.fit
.fm
.fr
.frl
.game
.global
.hk
.icu
.id
.ie
.im
.in
.info
.ink
.io
.ir
.is
.it
.jp
.kiwi
.kr
.kz
.link
.lt
.lv
.me
.ml
.mobi
.mu
.mx
.name
.nc
.net
.ninja
.nl
.nu
.nyc
.nz
.online
.org
.ovh
.pe
.pharmacy
.pl
.press
.pt
.pub
.pw
.red
.rest
.ru
.ru.rf
.rw
.sale
.se
.security
.sh
.shop
.sk
.site
.space
.store
.study
.tech
.tel
.theatre
.tickets
.top
.trade
.tv
.tz
.ua
.uk
.us
.uz
.video
.vip
.website
.wiki
.win
.work
.xin
.xyz
.za
```

## Issues
Raise an issue https://github.com/DannyCork/python-whois/issues/new


## Support
Python 3.x is supported.

Python 2.x IS NOT supported.
