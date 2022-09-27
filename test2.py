#!/usr/bin/python3
import whois
import os
import re
import getopt
import sys

Verbose = True
failure = {}


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
    if what not in failure:
        failure[what] = {}
    failure[what][d] = e

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


def getTestFilesAll(tDir):
    result = {}

    for item in os.listdir(tDir):
        fPath = f"{tDir}/{item}"

        if not os.path.isfile(fPath):  # only files
            continue

        if not item.endswith(".txt"):  # ending in .txt
            continue

        bName = item[:-4]
        result[bName] = []
        xx = result[bName]

        with open(fPath) as f:
            for index, line in enumerate(f):
                line = line.strip()
                if len(line) == 0 or line.startswith("#"):
                    continue

                aa = re.split(r"\s+", line)
                if aa[0] not in xx:
                    xx.append(aa[0])

    return result


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
    print("test.py -i <inputfile> -o <outputfile>")

    """ TODO
    --all
        tld supported [default]

    --all --reg <re>
        from all tld a regex match sub selection

    --all -- having <name>
        from all but only the ones haveing a certain field

    -- domain , -d
        only one domain

    -- file, -f
        only one file

    -- directory, -D
        only one dir

    """


def main(argv):
    tDir = "tests"
    testAllTld = True
    testAllFiles = False

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit()

        if opt in ("-i", "--ifile"):
            inputfile = arg

        if opt in ("-o", "--ofile"):
            outputfile = arg

    if testAllTld:
        allMetaTld = makeMateAllCurrentTld()
        testDomains(allMetaTld)

    if testAllFiles:
        result = getTestFilesAll(tDir)
        for testFile in result:
            testDomains(result[testFile])

    print("\n# ========================")
    for i in sorted(failure.keys()):
        for j in sorted(failure[i].keys()):
            print(i, j, failure[i][j])


if __name__ == "__main__":
    main(sys.argv[1:])
