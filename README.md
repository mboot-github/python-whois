# whois
A Python package for retrieving WHOIS information of domains.
This package will not support querying ip CIDR ranges or AS information

## Features
 * Python wrapper for the "whois" cli command of your operating system.
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

## Dependencies
  * please install also the command line "whois" of your distribution
  * this library parses the output of the "whois" cli command of your operating system

## Help Wanted
Your contributions are welcome, look for the Help wanted tag https://github.com/DannyCork/python-whois/labels/help%20wanted

## Usage example

Install the cli `whois` of your operating system if it is not present already

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

2023-01-18: sorrowless
 * add an opportunity to specify maximum cache age

2023-01-25: maarten_boot
 * convert the tld file to a Dict, we now no longer need a mappper for python keywords or second level domains.
 * utf8 level domains also need no mapper anymore an can be added as is with a translation to xn--<something>
 * added xn-- tlds for all known utf-8 domains we currently have
 * we can now add new domains on the fly or change them:  whois.mergeExternalDictWithRegex(aDictToOverride) see example testExtend.py

2023-01-27: maarten_boot
 * add autodetect via iana tld file (this has only tld's)
 * add a central collection of all compiled regexes and reuse them: REG_COLLECTION_BY_KEY in _0_init_tld.py
 * refresh testdata now that tld has dot instead of _ if more then one level
 * add additional strings meaning domain does not exist

2023-02-02: maarten_boot
 * whois.QuotaStringsAdd(str) to add additional strings for over quota detection. whois.QuotaStrings() lists the current configured strings
 * whois.NoneStringsAdd(str) to add additional string for NoSuchDomainExists detection (whois.query() retuning None). whois.NoneStrings() lsts the current configured strings
 * suppress messages to stderr if not verbose=True

## Support
 * Python 3.x is supported.
 * Python 2.x IS NOT supported.
