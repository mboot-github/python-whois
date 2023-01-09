#!/usr/bin/python3
import whois
import os
import re
import getopt
import sys
import subprocess
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
                if line.startswith("-- ") or line.startswith(">>> ") or line.startswith("Copyright notice"):
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
                ws = " [WHITESPACE AT END] " if re.search(r"[ \t]+\r?\n", lines) else ""
                tab = " [TAB] " if "\t" in lines else ""  # tabs are present in this section
                cr = " [CR] " if "\r" in lines else ""  # \r is present in this section
                print(f"# --- {k} Section: {n} {cr}{tab}{ws}")
                n += 1
                print(lines)


def prepItem(d):
    print("")
    print(f"test domain: <<<<<<<<<< {d} >>>>>>>>>>>>>>>>>>>>")


def xType(x):
    s = f"{type(x)}"
    return s.split("'")[1]


def doDnsDomainExists(domain):

    cmd = ["host", "-t", "ns", domain]

    # LANG=en is added to make the ".jp" output consist across all environments
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env={"LANG": "en"},
    )

    r = p.communicate()[0].decode(errors="ignore")
    what = r.split("\n")

    rr = []
    for i in what:
        if " name server " in i:
            rr.append(i.split(" ")[-1].lower())
    return rr


def testItem(d: str, printgetRawWhoisResult: bool = False):
    global PrintGetRawWhoisResult

    w = whois.query(
        d,
        ignore_returncode=IgnoreReturncode,
        verbose=Verbose,
        internationalized=True,
        include_raw_whois_text=PrintGetRawWhoisResult,
    )
    return w

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

        ns = sorted(doDnsDomainExists(d))
        if len(ns) == 0:
            continue

        # prepItem(d)
        try:
            w = testItem(d)
            if w is None:
                print("None")
                continue

            wd = w.__dict__
            for k, v in wd.items():
                if k == "name_servers":
                    if len(v) != len(ns):
                        ss = "%-18s %-17s "
                        if not isinstance(v, str):
                            print(d, (ss + "%s") % (k, xType(v), v))
                            print(ns)

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
        rr.append(f"meta.{tld}")
        rr.append(f"google.{tld}")

    return rr


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

"""
    )


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
            "pvI",
            [
                "print",
                "verbose",
                "IgnoreReturncode",
            ],
        )
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit(0)

        if opt in ("-v", "--verbose"):
            Verbose = True

        if opt in ("-p", "--print"):
            PrintGetRawWhoisResult = True

    print("## ===== TEST CURRENT TLD's")
    allMetaTld = makeMetaAllCurrentTld()
    testDomains(allMetaTld)
    showFailures()
    return


if __name__ == "__main__":
    main(sys.argv[1:])
