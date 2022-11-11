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
 * Verbose output on stderr during debugging to see how the internal functions are doing their work
 * raise a exception on Quota ecceeded type responses
 * raise a exception on PrivateRegistry tld's where we know the tld and know we don't know anything
 * allow for optional cleaning the whois response before extracting information
 * optionally allow IDN's to be translated to Punycode

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
see the file: ./whois/tld_regexpr.py
or call whois.validTlds()

## Issues
Raise an issue https://github.com/DannyCork/python-whois/issues/new

## Changes:
2022-06-09: maarten_boot:
 * the returned list of name_servers is now a sorted unique list and not a set
 * the help function whois.validTlds() now outputs the true tld with dots

2022-09-27: maarten_boot
 * add test2.py to replace test.py
 * ./test2.py -h will show the possible usage
 * all tests from the original program are now files in the ./tests directory
 * test can be done on all supported tld's with -a or --all and limitest by regex with -r <pattern> or --reg=<pattern>

2022-11-04: maarten_boot
 * add support for Iana example.com, example.net

2022-11-07: maarten_boot
 * add testing against static known data in dir: ./testdata/<domain>/output
 * test.sh will test all domains in testdata without actually calling whois, the input data is instead read from testdata/<domain>/input

2022-11-11: maarten_boot
 * add support for returning the raw data from the whois command: flag include_raw_whois_text
 * add support for handling unsupported domains via whois raw text only: flag return_raw_text_for_unsupported_tld

## Support
 * Python 3.x is supported.
 * Python 2.x IS NOT supported.
