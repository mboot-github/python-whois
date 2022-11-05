#!/usr/bin/python3
import whois
import os
import re
import getopt
import sys

Verbose = False
Failures = {}
IgnoreReturncode = False


def prepItem(d):
    print("")
    print(f"test domain: <<<<<<<<<< {d} >>>>>>>>>>>>>>>>>>>>")


def xType(x):
    s = f"{type(x)}"
    return s.split("'")[1]


def testItem(d):
    w = whois.query(
        d,
        ignore_returncode=IgnoreReturncode,
        verbose=Verbose,
        internationalized=True,
    )

    if w is None:
        print("None")
        return

    # the 3 date time items can be None if not present or a datetime string
    # dnssec is a bool
    # some strings are return as '' when empty (status)
    # statuses can be a array of one empty string if no data

    # not all values are always present it mainly depends on whet we see in the output of whois
    # if we return not None: the elements that ars always there ars domain_name , tld, dnssec

    wd = w.__dict__
    for k, v in wd.items():
        ss = "%-18s %-17s "
        if isinstance(v, str):
            print((ss + "'%s'") % (k, xType(v), v))
        else:
            print((ss + "%s") % (k, xType(v), v))


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
        # except Exception as e:
        #    errorItem(d, e, what="Generic")


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


def makeMetaAllCurrentTld(allHaving=None, allRegex=None):
    rr = []
    for tld in getAllCurrentTld():
        if allRegex:
            if re.search(allRegex, tld):
                rr.append(f"meta.{tld}")
        else:
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

    [ -I | --IgnoreReturncode ]
        # sets the IgnoreReturncode to True, this will be forwarded to whois.query

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

    # options are exclusive and without any options the test2 program does nothing

    # test one specific file with verbose and IgnoreReturncode
    example: ./test2.py -v -I -f tests/ok-domains.txt 2>2 >out

    # test one specific directory with verbose and IgnoreReturncode
    example: ./test2.py -v -I -D tests 2>2 >out

    # test two domains with verbose and IgnoreReturncode
    example: ./test2.py -v -I -d meta.org -d meta.com 2>2 >out

    # test all supported tld's with verbose and IgnoreReturncode
    example: ./test2.py -v -I -a 2>2 >out

    # test nothing
    example: ./test2.py -v -I 2>2 >out
"""
    )

    """
    TODO
    --all --reg <re>
        from all tld a regex match sub selection

    --all --having <name>
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
    global IgnoreReturncode

    try:
        opts, args = getopt.getopt(
            argv,
            "vIhaf:d:D:r:H:",
            [
                "verbose",
                "IgnoreReturncode",
                "all",
                "file=",
                "Directory=",
                "domain=",
                "reg=",
                "having=",
            ],
        )
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    testAllTld = False
    allHaving = None  # from all supported tld only process the ones having this :: TODO ::
    allRegex = None  # from all supported tld process only the ones matching this regex

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

        if opt in ("-H", "--having"):
            testAllTld = True
            allHaving = arg

        if opt in ("-r", "--reg"):
            testAllTld = True
            allRegex = arg

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
        allMetaTld = makeMetaAllCurrentTld(allHaving, allRegex)
        testDomains(allMetaTld)
        showFailures()
        return

    if len(dirs):
        fileData = {}
        print("## ===== TEST DIRECTORIES")
        for dName in dirs:
            getTestFilesAll(dName, fileData)
        for testFile in fileData:
            print(f"## ===== TEST FILE: {testFile}")
            testDomains(fileData[testFile])
        showFailures()
        return

    if len(files):
        fileData = {}
        print("## ===== TEST FILES")
        for testFile in files:
            getTestFileOne(testFile, fileData)
        for testFile in fileData:
            print(f"## ===== TEST FILE: {testFile}")
            testDomains(fileData[testFile])
        showFailures()
        return

    if len(domains):
        testDomains(domains)
        showFailures()
        return


if __name__ == "__main__":
    main(sys.argv[1:])
