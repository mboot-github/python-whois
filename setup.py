from distutils.core import setup

setup(
    name='whois',
    version='0.9.11',
    description='Python package for retrieving WHOIS information of domains.',
    author='DannyCork',
    author_email='ddarko@ddarko.org',
    license='MIT http://www.opensource.org/licenses/mit-license.php',
    download_url='https://github.com/DannyCork/python-whois/releases/tag/0.9.11',
    url='https://github.com/DannyCork/python-whois/',
    platforms=['any'],
    packages=['whois'],
    keywords=['Python', 'whois', 'tld', 'domain', 'expiration', 'cctld', 'domainer', '.com', 'registrar'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
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
