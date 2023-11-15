# whoisdomain

  * A Python package for retrieving WHOIS information of DOMAIN'S ONLY.
  * Python 2.x IS NOT supported.
  * Currently no additional python packages need to be installed.

---

## Notes

  * This package will not support querying ip CIDR ranges or AS information
  * This was a copy of the original DanyCork 'whois'.
      * Significantly refactored in 2023.
      * The output is still compatible with DanyCork 'whois'

## Versioning

  * I will start versioning at 1.x.x
     * the second item will be YYYYMMDD,
     * the third item will start from 1 and be only used if more than one update will have to be done in one day.

Versions `1.x.x` will keep the output compatible with Danny Cork until 2024-02-03 (February 2024)

## Releases

  * Releases are avalable at: [Pypi](https://pypi.org/project/whoisdomain/)

Pypi releases can be installed with:

  * `pip install whoisdomain`

## Features
  * See: [Features](docs/Features.md)

## Dependencies
  * please install also the command line "whois" of your distribution as this library parses the output of the "whois" cli command of your operating system

### Notes for Mac users
  * it has been observed that the default cli whois on Mac is showing each forward step in its output, this makes parsing the result very unreliable.
  * using a brew install whois will give in general better results.

## Docker release
  * See [Docker](docs/Docker.md)

## Usage example
  * See [Usage](docs/Usage.md)

## whoisdomain
  * the cli `whoisdomain` is  documented in [whoisdomain-cli](docs/whoisdomain-cli.md)

## ccTLD & TLD support

Most `tld's` are now autodetected via IANA root db, see the Analizer directory
and `make suggest`.

  * see the file: [tld_regexpr](./whoisdomain/tldDb/tld_regexpr.py)
  * for python use:  `whoisdomain.validTlds()`
  * for cli use `whoisdomain -S`

---

## Support
 * Python 3.x is supported for x >= 9
 * Python 2.x IS NOT supported.

## Author's
  * See: [Authors](docs/Authors.md)

---

## Updates
  * see [Updates](docs/Updates.md) for a full history of changes.
  * Only the latest update is mentioned here

### 1.20230906.1
  * introduce parsing based on functions
  * allow contextual search in splitted data and plain data
  * allow contextual search based on earlier result
  * fix a few tld to return the proper registrant string (not nic handle)

### 1.20230913.1
  * if you have installed `tld` (pip install tld) you can enable withPublicSuffix=True to process untill you reach the pseudo tld.
  * the public_suffix info is added if available (and if requested)
  * example case is: ./test2.py -d www.dublin.airport.aero --withPublicSuffix

### 1.20230913.3
  * fix re.NOFLAGS, it is not compatible with 3.9, it appears in 3.11

## 1.20230917.1
  * prepare work on pylint
  * switch to logging: all verbose is currently log.debug(); to show set LOGLEVEL=DEBUG before calling, see Makefile: make test
  * experimental: add extractServers: bool default False; when true we will try to extract the "redirect info chain" on rcf1036/whois and jwhois for linux/darwin
  * add missing option to query(), test in production environment done

## 1.20231102.1
  * fix from kazet for .pl tld.

## 1.20231115.1
 New tld's and removal of a few tlds no longer supported at iana

 * abb, bw, bn, crown, crs, fj (does not work), gp (does not work), weir, realtor, post, mw, pf (a strange one), iq (gives timout), mm, int, hm (does not work)

---

## in progress

