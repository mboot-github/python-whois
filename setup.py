from distutils.core import setup

setup(
	name='whois',
	version='0.2',
	description='Python module/library for retrieving WHOIS information of domains.',
	long_description = """\
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
""",
	author='DDarko.org',
	author_email='ddarko@ddarko.org',
	license='MIT',
	url='http://code.google.com/p/python-whois/',
	platforms = ['any'],
	packages=['whois'],
	keywords=['Python','WHOIS','TLD','domain','expiration','registrar'],
	classifiers = """\
Classifier: License :: OSI Approved :: MIT License
Classifier: Programming Language :: Python :: 2.5
Classifier: Programming Language :: Python :: 2.6
Classifier: Programming Language :: Python :: 2.7
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.0
Classifier: Programming Language :: Python :: 3.1
Classifier: Programming Language :: Python :: 3.2
Classifier: Topic :: Software Development :: Libraries :: Python Modules""".split('\n'),
)
