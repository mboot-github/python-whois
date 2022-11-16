#!/usr/bin/python3
import whois
import os
import re
import getopt
import sys
from typing import Optional, List, Dict

Verbose = False
PrintGetRawWhoisResult = False
Ruleset = False

Failures = {}
IgnoreReturncode = False


class ResponseCleaner:
    data: Optional[str] = None
    rDict: Dict = {}

    def __init__(self, pathToTestFile: str):
        self.data = self.readInputFile(pathToTestFile)

    def readInputFile(self, pathToTestFile: str):
        if not os.path.exists(pathToTestFile):
            return None

        with open(pathToTestFile, mode="rb") as f:  # switch to binary mode as that is what Popen uses
            # make sure the data is treated exactly the same as the output of Popen
            return f.read().decode(errors="ignore")

    def cleanSection(self, section: List) -> List:
        # cleanup any beginning and ending empty lines from the section

        if len(section) == 0:
            return section

        rr = r"^\s*$"
        n = 0  # remove empty lines from the start of section
        while re.match(rr, section[n]):
            section.pop(n)
            # n stays 0

        n = len(section) - 1  # remove empty lines from the end of the section
        while re.match(rr, section[n]):
            section.pop(n)
            n = len(section) - 1  # remove empty lines from the end of section

        return section

    def splitBodyInSections(self, body: List) -> List:
        # split the body on empty line, cleanup all sections, remove empty sections
        # return list of body's

        sections = []
        n = 0
        sections.append([])
        for line in body:
            if re.match(r"^\s*$", line):
                n += 1
                sections.append([])
                continue
            sections[n].append(line)

        m = 0
        while m < len(sections):
            sections[m] = self.cleanSection(sections[m])
            m += 1

        # now remove ampty sections and return
        sections2 = []
        m = 0
        while m < len(sections):
            if len(sections[m]) > 0:
                sections2.append("\n".join(sections[m]))
            m += 1

        return sections2

    def cleanupWhoisResponse(
        self,
        verbose: bool = False,
        with_cleanup_results: bool = False,
    ):
        result = whois._2_parse.cleanupWhoisResponse(
            self.data,
            verbose=False,
            with_cleanup_results=False,
        )

        self.rDict = {
            "BodyHasSections": False,  # if this is true the body is not a list of lines but a list of sections with lines
            "Preamble": [],  # the lines telling what whois servers wwere contacted
            "Percent": [],  # lines staring with %% , often not present but may contain hints
            "Body": [],  # the body of the whois, may be in sections separated by empty lines
            "Postamble": [],  # copyright and other not relevant info for actual parsing whois
        }
        body = []

        rr = []
        z = result.split("\n")
        preambleSeen = False
        postambleSeen = False
        percentSeen = False
        for line in z:
            if preambleSeen is False:
                if line.startswith("["):
                    self.rDict["Preamble"].append(line)
                    line = "PRE;" + line
                    continue
                else:
                    preambleSeen = True

            if preambleSeen is True and percentSeen is False:
                if line.startswith("%"):
                    self.rDict["Percent"].append(line)
                    line = "PERCENT;" + line
                    continue
                else:
                    percentSeen = True

            if postambleSeen is False:
                if line.startswith("--") or line.startswith(">>> ") or line.startswith("Copyright notice"):
                    postambleSeen = True

            if postambleSeen is True:
                self.rDict["Postamble"].append(line)
                line = "POST;" + line
                continue

            body.append(line)

            if "\t" in line:
                line = "TAB;" + line  # mark lines having tabs

            if line.endswith("\r"):
                line = "CR;" + line  # mark lines having CR (\r)

            rr.append(line)

        body = self.cleanSection(body)
        self.rDict["Body"] = self.splitBodyInSections(body)
        return "\n".join(rr), self.rDict

    def printMe(self):
        zz = ["Preamble", "Percent", "Postamble"]
        for k in zz:
            n = 0
            for lines in self.rDict[k]:
                tab = " [TAB] " if "\t" in lines else ""  # tabs are present in this section
                cr = " [CR] " if "\r" in lines else ""  # \r is present in this section
                print(k, cr, tab, lines)

        k = "Body"
        if len(self.rDict[k]):
            n = 0
            for lines in self.rDict[k]:
                tab = " [TAB] " if "\t" in lines else "-------"  # tabs are present in this section
                cr = " [CR] " if "\r" in lines else "------"  # \r is present in this section
                print(f"# ------------- {k} Section: {n} {cr}{tab}---------")
                n += 1
                print(lines)


def prepItem(d):
    print("")
    print(f"test domain: <<<<<<<<<< {d} >>>>>>>>>>>>>>>>>>>>")


def xType(x):
    s = f"{type(x)}"
    return s.split("'")[1]


def testItem(d: str, printgetRawWhoisResult: bool = False):
    global PrintGetRawWhoisResult

    w = whois.query(
        d,
        ignore_returncode=IgnoreReturncode,
        verbose=Verbose,
        internationalized=True,
        include_raw_whois_text=PrintGetRawWhoisResult,
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


def ShowRuleset(tld):
    rr = whois.TLD_RE
    if tld in rr:
        for key in sorted(rr[tld].keys()):
            rule = f"{rr[tld][key]}"
            if "re.compile" in rule:
                rule = rule.split("re.compile(")[1]
                rule = rule.split(", re.IGNORECASE)")[0]
            print(key, rule, "IGNORECASE")


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

    [ -p | --print ]
    also print text containing the raw output of whois

    [ -R | --Ruleset ]
    dump the ruleset for the tld and exit

    [ -S | --SupportedTld ]
    print all supported top level domains we know and exit

    [ -C <file> | --Cleanup <file> ]
    read the input file specified and run the same cleanup as in whois.query , then exit

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
    global PrintGetRawWhoisResult
    global Ruleset
    try:
        opts, args = getopt.getopt(
            argv,
            "RSpvIhaf:d:D:r:H:C:",
            [
                "Ruleset",
                "SupportedTld",
                "print",
                "verbose",
                "IgnoreReturncode",
                "all",
                "file=",
                "Directory=",
                "domain=",
                "reg=",
                "having=",
                "Cleanup=",
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
        if opt in ("-S", "SupportedTld"):
            for tld in sorted(whois.validTlds()):
                print(tld)
            sys.exit(0)

        if opt == "-h":
            usage()
            sys.exit(0)

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

        if opt in ("-p", "--print"):
            PrintGetRawWhoisResult = True

        if opt in ("-R", "--Ruleset"):
            Ruleset = True

        if opt in ("-D", "--Directory"):
            directory = arg
            isDir = os.path.isdir(directory)
            if isDir is False:
                print(f"{directory} cannot be found or is not a directory", file=sys.stderr)
                sys.exit(101)

        if opt in ("-C", "--Cleanup"):
            inFile = arg
            isFile = os.path.isfile(arg)
            if isFile is False:
                print(f"{inFile} cannot be found or is not a file", file=sys.stderr)
                sys.exit(101)

            rc = ResponseCleaner(inFile)
            d1, rDict = rc.cleanupWhoisResponse()
            rc.printMe()
            sys.exit(0)

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

    if Ruleset is True and len(domains):
        for domain in domains:
            ShowRuleset(domain)
        sys.exit(0)

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
