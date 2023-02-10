from distutils.core import setup

setup(
    name="whois",
    version="0.9.27",
    description="Python package for retrieving WHOIS information of domains.",
    author="DannyCork",
    author_email="ddarko@ddarko.org",
    license="MIT http://www.opensource.org/licenses/mit-license.php",
    download_url="https://github.com/DannyCork/python-whois/releases/latest",
    url="https://github.com/DannyCork/python-whois/",
    platforms=["any"],
    packages=["whois"],
    keywords=[
        "Python",
        "whois",
        "tld",
        "domain",
        "expiration",
        "cctld",
        "domainer",
        ".com",
        "registrar",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)

'''
test_suite='testsuite',
entry_points="""
[console_scripts]
cmd = package:main
""",
'''
