"""
	Python module/library for retrieving WHOIS information of domains.

	By DDarko.org  ddarko@ddarko.org  http://ddarko.org/
	License MIT  http://www.opensource.org/licenses/mit-license.php

	Usage example
	>>> import whois
	>>> domain = whois.query('google.com')

	>>> print(domain.__dict__)
	{'expiration_date': datetime.datetime(2020, 9, 14, 0, 0), 'last_updated': datetime.datetime(2011, 7, 20, 0, 0), 'registrar': 'MARKMONITOR INC.', 'name': 'google.com', 'creation_date': datetime.datetime(1997, 9, 15, 0, 0)}

	>>> print(domain.name)
	google.com

	>>> print(domain.expiration_date)
	2020-09-14 00:00:00

"""
from ._1_query import _do_whois_query
from ._2_parse import _do_parse
from ._3_adjust import Domain



def query(domain):
	assert isinstance(domain, str), Exception('`domain` - must be <str>')
	domain = domain.lower().strip()
	d = domain.split('.')
	if d[0] == 'www': d = d[1:]
	while 1:
		pd = _do_parse(_do_whois_query(d), d[-1])
		if not pd['domain_name'][0] and len(d) > 2: d = d[1:]
		else: break

	return Domain(pd) if pd['domain_name'][0] else None


