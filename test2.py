#!/usr/bin/python3
import whois
import os
import re
import getopt
import sys

Verbose = False
Failures = {}


def prepItem(d):
    print("-" * 80)
    print(d)


def testItem(d):
    w = whois.query(
        d,
        ignore_returncode=True,
        verbose=Verbose,
        internationalized=True,
    )

    if w is None:
        print("None")
        return

    wd = w.__dict__
    for k, v in wd.items():
        print('%20s\t"%s"' % (k, v))


def errorItem(d, e, what="Generic"):
    if what not in Failures:
        Failures[what] = {}
    Failures[what][d] = e

    message = f"Domain: {d}; Exception: {what}; Error: {e}"
    print(message)


def testDomains(aList):
    for d in aList:

        # skip empty lines
        if not d:
            continue

        if len(d.strip()) == 0:
            continue

        # skip comments
        if d.strip().startswith("#"):
            continue

        # skip comments behind the domain
        d = d.split("#")[0]
        d = d.strip()

        prepItem(d)
        try:
            testItem(d)
        except whois.UnknownTld as e:
            errorItem(d, e, what="UnknownTld")
        except whois.FailedParsingWhoisOutput as e:
            errorItem(d, e, what="FailedParsingWhoisOutput")
        except whois.UnknownDateFormat as e:
            errorItem(d, e, what="UnknownDateFormat")
        except whois.WhoisCommandFailed as e:
            errorItem(d, e, what="WhoisCommandFailed")
        except whois.WhoisQuotaExceeded as e:
            errorItem(d, e, what="WhoisQuotaExceeded")
        except whois.WhoisPrivateRegistry as e:
            errorItem(d, e, what="WhoisPrivateRegistry")
        except Exception as e:
            errorItem(d, e, what="Generic")


def getTestFileOne(fPath, fileData):
    if not os.path.isfile(fPath):  # only files
        return

    if not fPath.endswith(".txt"):  # ending in .txt
        return

    bName = fPath[:-4]
    fileData[bName] = []
    xx = fileData[bName]

    with open(fPath) as f:
        for index, line in enumerate(f):
            line = line.strip()
            if len(line) == 0 or line.startswith("#"):
                continue

            aa = re.split(r"\s+", line)
            if aa[0] not in xx:
                xx.append(aa[0])

    return


def getTestFilesAll(tDir, fileData):
    for item in os.listdir(tDir):
        fPath = f"{tDir}/{item}"
        getTestFileOne(fPath, fileData)


def getAllCurrentTld():
    return whois.validTlds()


def makeMateAllCurrentTld():
    rr = []
    for tld in getAllCurrentTld():
        rr.append(f"meta.{tld}")
    return rr


def showAllCurrentTld():
    print("Tld's currently supported")
    for tld in getAllCurrentTld():
        print(tld)


def usage():
    print(
        """
test.py
    [ -v | --verbose ]
        # set verbose to True, this will be forwarded to whois.query

    [ -a | --all]
        # test all existing tld currently supported,

    [ -d <domain> | --domain = <domain> " ]
        # only analyze the given domains
        # the option can be repeated to specify more then one domain

    [ -f <filename> | --file = <filename> " ]
        # use the named file to test all domains (one domain per line)
        # lines starting with # or empty lines are skipped, anything after the domain is ignored
        # the option can be repeated to specify more then one file

    [ -D <directory> | --Directory = <directory> " ]
        # use the named directory, ald use all files ending in .txt as files containing domains
        # files are processed as in the -f option so comments and empty lines are skipped
        # the option can be repeated to specify more then one directory

    example: ./test2.py -f tests/ok-domains.txt -D tests -d meta.org -d meta.com -a 2>2 >out
"""
    )

    """
    TODO
    --all --reg <re>
        from all tld a regex match sub selection

    --all -- having <name>
        from all but only the ones haveing a certain field
    """


def showFailures():
    if len(Failures):
        print("\n# ========================")
        for i in sorted(Failures.keys()):
            for j in sorted(Failures[i].keys()):
                print(i, j, Failures[i][j])


def main(argv):
    global Verbose

    try:
        opts, args = getopt.getopt(
            argv,
            "vhaf:d:D:",
            [
                "verbose",
                "all",
                "file =",
                "Directory =",
                "domain =",
            ],
        )
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    testAllTld = False

    directory = None
    dirs = []

    filename = None
    files = []

    domain = None
    domains = []

    fileData = {}

    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit()

        if opt in ("-a", "--all"):
            testAllTld = True

        if opt in ("-v", "--verbose"):
            Verbose = True

        if opt in ("-D", "--Directory"):
            directory = arg
            isDir = os.path.isdir(directory)
            if isDir is False:
                print(f"{directory} cannot be found or is not a directory", file=sys.stderr)
                sys.exit(101)

            if directory not in dirs:
                dirs.append(directory)
                testAllTld = False

        if opt in ("-f", "--file"):
            filename = arg
            isFile = os.path.isfile(filename)
            if isFile is False:
                print(f"{filename} cannot be found or is not a file", file=sys.stderr)
                sys.exit(101)

            if filename not in files:
                files.append(filename)
                testAllTld = False

        if opt in ("-d", "--domain"):
            domain = arg
            if domain not in domains:
                domains.append(domain)

    if testAllTld:
        print("## ===== TEST CURRENT TLD's")
        allMetaTld = makeMateAllCurrentTld()
        testDomains(allMetaTld)
        showFailures()

    if len(dirs):
        print("## ===== TEST DIRECTORIES")
        for dName in dirs:
            getTestFilesAll(dName, fileData)
        for testFile in fileData:
            print(f"## ===== TEST FILE: {testFile}")
            testDomains(fileData[testFile])
        showFailures()

    if len(files):
        print("## ===== TEST FILES")
        for testFile in files:
            getTestFileOne(testFile, fileData)
        for testFile in fileData:
            print(f"## ===== TEST FILE: {testFile}")
            testDomains(fileData[testFile])
        showFailures()

    if len(domains):
        print("## ===== TEST DOMAINS")
        testDomains(domains)
        showFailures()


if __name__ == "__main__":
    main(sys.argv[1:])
