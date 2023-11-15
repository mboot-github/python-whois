# Features
 * Python wrapper for the "whois" cli command of your operating system.
 * Simple interface to access parsed WHOIS data for a given domain.
 * Able to extract data for all the popular TLDs (com, org, net, biz, info, pl, jp, uk, nz,  ...).
 * Query a WHOIS server directly instead of going through an intermediate web service like many others do.
 * Works with Python >= 3.9
 * All dates as datetime objects.
 * Possibility to cache results.
 * Verbose output on stderr during debugging to see how the internal functions are doing their work
 * raise a exception on Quota ecceeded type responses
 * raise a exception on PrivateRegistry tld's where we know the tld and know we don't know anything
 * allow for optional cleaning the response before extracting information
 * optionally allow IDN's to be translated to Punycode
 * optional specify the whois command on query(...,cmd="whois") as in: https://github.com/gen1us2k/python-whois/
 * the module is now 'mypy --strict' clean
 * the module now also exports a cli command domainwhois
 * both the module and the cli now support showing the version with lib:whois.getVersion() or cli:whoisdomain -V
 * the whoisdomain can now output json data (one per domain: e.g 'whoisdomain -d google.com -j' )
 * withRedacted: bool = False has been added to query(), if set to True any redacted fields will now be shown also (also supported in the cli whoisdomain as --withRedacted)
 * a analizer directory is presend in the github repo that will be used to look for new IANA tls's currently unsupported but maching known whois servers
