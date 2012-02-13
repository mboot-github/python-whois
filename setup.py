from distutils.core import setup

setup(
	name='whois',
	version='0.3',
	description='Python module/library for retrieving WHOIS information of domains.',
	long_description = open('README').read(),
	author='DDarko.org',
	author_email='ddarko@ddarko.org',
	license='MIT',
	url='http://code.google.com/p/python-whois/',
	platforms = ['any'],
	packages=['whois'],
	keywords=['Python','WHOIS','TLD','domain','expiration','registrar'],
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Intended Audience :: Developers',
		'Environment :: Console',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.0',
		'Programming Language :: Python :: 3.1',
		'Programming Language :: Python :: 3.2',
		'Topic :: Internet',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)

'''
test_suite='testsuite',
entry_points="""
[console_scripts]
cmd = package:main
""",
'''