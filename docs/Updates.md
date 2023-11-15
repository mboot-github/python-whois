# Updates
## 1.20230627.2
  * add Kenia proper whois server and known second level domains
## 1.20230627.3
  * add rw tld proper whois server and second level ; restore mistakenly deleted .toml file
## 1.20230627.3
  * additional kenia second level domains
## 1.20230712.2
  * tld .edu now can have up to 10 nameservers; remove action on pull request
## 1.20230717.1
  * add tld: com.ru, msk.ru, spb.ru  (all have a test documented), also update the tld: ru, the newlines are not needed.
## 1.20230717.2
  * add option to parse partial result after timout has occurred (parse_partial_response:bool default False); this will need `stdbuf` installed otherwise it will fail
## 1.20230718.3
  * fix typo in whois server hint for tld: ru
## 1.20230720.1
  * add gov.tr; switch off status:available and status:free as None response, we should not interprete the result by default (we can add a option later)
## 1.20230720.2
  * fix server hints for derived second level "xxx.tr", add processing "_test" hints during 'test2.py -a'
  * add external caching framework that can be overridden for use of your own caching implementation
  * renaming various vars to mak them more verbose
  * preparing for capturing all parameters in one object and parring that object around instead of many arguments in methods/functions
  * switch to json so we dont need a additional dependency in ParamContext
  * finish rework args to ParameterContext, split of domain as file
## 1.20230803.1
  * frenzy refactor-release
## 1.20230804.1
  * testing
## 1.20230804.2
  * testing after remove of leading dot in rw second level domains
## 1.20230804.3
  * simplefy cache implementation after feedback from `baderdean`
  * "more lembas bread", refactor parse and query
  * remove option to typecheck CACHE_STUB, use try/catch/exit instead, does not work when timout happens, removed ;-(
  * refactor doQuery create processWhoisDomainRequest, split of lastWhois
## 1.20230806.1
  * testing done, prep new release: "more lembas bread"
  * bug found with the default timeout: if no timeout is specified the program fails: all pypi releases before 2023-07-17 yanked
## 1.20230807.1
  * fix default timeout
  * add DummyCache, DBMCache, RedisCache with simple test in testCache.py, testing custom cache options
## 1.20230811.1
  * replace type hint | with Union for py3.9 compat; switch off experimental redis tools
  * switch off 3.[6-8] minimal is 3.9 we test against
  * start working on dataContext;
  * add more \_test items; reorder parts of tld_regexpr;
  * propagate all meta domains servers as they are not inherited, testing , some domains have been retracted mboot; 2023-08-23;
  * add suggestion from baderdean to parse fr domains with more focus on ORGANISATION
  * 2023-08-24: mboot: more \_test added to tld
  * verify all \_test on whois.nic.<tld> \_test: nic.<tld> fix where needed; remove some abandoned tld's
## 1.20230824.1
  * mboot; to combine all new tests and changes, "the galloping Chutzpah release"
## 1.20230824.5
  * mboot; fix missing module in whl
  * restore python 3.6 test as i still use it on one remaining app with python 3.6 (make testP36)
  * finalize verification of all tld's in iana, add test where this can be auto generated from whois.nic.<tld> 2023-08-28; mboot
## 1.20230829.1
  * mboot; all \_test now work, using analizer tool to verify that iana tld db web site and tl-regexpr match
  * add DEBUG to all verbose strings
  * remove tldString and dList and domain , all go via dc (dataContect) now
  * run tests and add new TODO
  * moving all TLD_RE activities to tldInfo.py, and all exported helper funcs to helpers.py
  * thinking about adding more complicated nested regex extractors to target contact info
  * start with dependency inject: parser is passed as arg
  * add cli interface to dependency inject, rightsize after test
  * finish dependency inject move Domain create outside
  * prep for other types or regex; all simple regex strings in tld_regexpr.py now need R() around them
  * use currying to make all regex strings into function cal in whoisParser.py; all regexes in tld_regexpr.py are now converted on import to function calls via R()
  * update tld: sk to use contextual extract, test with google.sk
  * add findFromToAndLookForWithFindFirst contextual search based on a previous findFirst, used in "fr" tld, example google.fr, {} is used to add to fromStr

## 1.20230904.1
  * only on pypi-test

---

## 1.20230906.1
  * introduce parsing based on functions
  * allow contextual search in splitted data and plain data
  * allow contextual search based on earlier result
  * fix a few tld to return the proper registrant string (not nic handle)
  * introduce parsing based on functions, allow contextual search in splitted data and plain data, allow contextual search based on earlier result; fix a few tld to return the proper registrant string (not nic handle)

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

---

## in progress

  * prepare work on pylint
  * switch to logging: all verbose is currently log.debug(); to show set LOGLEVEL=DEBUG before calling, see Makefile: make test



