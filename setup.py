from distutils.core import setup

setup(
	name='whois',
	version='0.1',
	description='Python module/library for retrieving WHOIS information of domains.',
	author='DDarko.org',
	author_email='ddarko@ddarko.org',
	url='http://code.google.com/p/python-whois/',
	packages=['whois', 'whois.tld'],
	include_package_data=True,
)

#eof
