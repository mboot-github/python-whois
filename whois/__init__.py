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
from ._1_query import do_query
from ._2_parse import do_parse
from ._3_adjust import Domain


CACHE_FILE = None
SLOW_DOWN = 0


def query(domain, force=0, cache_file=None, slow_down=0):
	"""
		force=1				<bool>		Don't use cache.
		cache_file=<path>	<str>		Use file to store cache not only memory.
		slow_down=0			<int>		Time [s] I will wait after you query the WHOIS database. This is useful when there is a limit to the number of requests at a time.
	"""
	assert isinstance(domain, str), Exception('`domain` - must be <str>')
	cache_file = cache_file or CACHE_FILE
	slow_down = slow_down or SLOW_DOWN
	domain = domain.lower().strip()
	d = domain.split('.')
	if d[0] == 'www': d = d[1:]

	while 1:
		pd = do_parse(do_query(d, force, cache_file, slow_down), d[-1])
		if not pd['domain_name'][0] and len(d) > 2: d = d[1:]
		else: break

	return Domain(pd) if pd['domain_name'][0] else None


