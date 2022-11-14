#! /bin/bash

TMPDIR="./tmp" # the default work directory is a local tmp (exclude by .gitignore )

FORCE=0 # force whois loogup by not using cached data
VERBOSE=0 # along the way inform us on progress and results

prepTempDir()
{
    # make the work dir if it does nt exist
    mkdir -p "$TMPDIR" || {
        echo "FATAL: cannot make test dir: $TMPDIR" >&2
        exit 101
    }
}

getAllTldSupported()
{
    # get all currently supported tld's
    ./test2.py -S
}

testNameserverExistsInInputAndOutput()
{
    local tld="$1"
    local d="$TMPDIR/$tld"
    local dns="$d/__dns-ns"

    [ -s "$dns" ] || return # dont bother at all if we have no dns file

    rm -f "$d/error.ns"

    cat "$dns" |
    awk '{ print $NF }' |
    while read ns
    do
        [ -s "$d/input" ] || return # dont bother if we have no input file

        grep -q -i "$ns" "$d/input" && {
            # only test in the output if it is present in the input
            grep -q -i "$ns" "$d/output" || {
                echo "ERROR: output;  missing nameserver '$ns' for tld: $tld" |
                tee -a "$d/error.ns"
            }
        }
    done
}

cleanupTldTestDirectory()
{
    local tld="$1"
    local domain="$2"
    local d="$TMPDIR/$tld"
    local zz="$domain.$tld"

    rm -f "$d/input" "$d/output" "$d/__domain__$zz" "$d/__dns-soa" "$d/__dns-ns"
}

getTestDataInputForTldAndDomain()
{
    local tld="$1"
    local domain="$2"
    local d="$TMPDIR/$tld"
    local zz="$domain.$tld"

    # make the testing input data
    # dont overwire the input file unless FORCE is requested

    [ ! -s "$d/input" -o "$FORCE" = "1" ] && {
        # for whois force english, force no cache
        # LANG=EN whois --force-lookup "meta.$tld" >"$d/input" || {
        whois --force-lookup "meta.$tld" >"$d/input" || {
            # whois has a problem
            local ret=$?
            echo "ERROR: whois returns $ret for domain: $zz" >&2
            cat "$d/input" >&2
            cleanupTldTestDirectory "$tld" "$domain"
            return 1
        }
    }

    # parse the input and annotate it and split the body in sections
    ./test2.py -C "$d/input" > "$d/input.out"
}

getTestDataOutputForTldAndDomain()
{
    local tld="$1"
    local domain="$2"
    local d="$TMPDIR/$tld"

    # make the testing output data
    # dont overwrite the output file unless FORCE is requested
    [ ! -s "$d/output" -o "$FORCE" = "1" ] && {
        ./test2.py -d "$domain.$tld" >"$d/output"
    }
}

getDnsSoaRecordAndLeaveEvidenceTldDomain()
{
    local tld="$1"
    local domain="$2"
    local d="$TMPDIR/$tld"
    local zz="$domain.$tld"

    [ -f "$d/_NO_SOA_$zz" ] && return 2

    # get the soa record , if it exists proceed otherwise ignore this domain
    # along the way we store the raw soa record also
    host -t soa "$zz" |
    tee "$d/__dns-soa" |
    grep -q " has SOA record " || {
        # no soa record so that domain does not exist, cleanup the test dir
        cleanupTldTestDirectory "$tld" "$domain"
        echo "WARN: no SOA for domain: $zz" >&2
        >"$d/_NO_SOA_$zz"
        return 1
    }
}

makeDirectoryForTld()
{
    local tld="$1"
    local domain="$2"
    local d="$TMPDIR/$tld"

    mkdir -p "$d" || {
        echo "FATAL: cannot make tld directory: '$d'" >&2
        exit 101
    }
}

makeTestDataOriginalOneTldDomain()
{
    # see if we have a proper soa record for the domain before attempting to run whois
    # collect the raw whois data in input, the test2 data in output
    # and get the dns nameservers for later comparison,
    # for many tld patterns we have no nameserver info although they are in the input,
    # we may need to improve the parsing of the whois nameservers
    # or skip them alltogether and use dns diectly for nameservers

    local tld="$1"
    local domain="$2"
    local d="$TMPDIR/$tld"
    local zz="$domain.$tld"

    getDnsSoaRecordAndLeaveEvidenceTldDomain "$tld" "$domain" || return 1

    # what domain did we test
    touch "$d/__domain__$zz"

    # store the nameservers from dns
    host -t ns "$zz" > "$d/__dns-ns"

    getTestDataInputForTldAndDomain || return 1

    getTestDataOutputForTldAndDomain "$tld" "$domain"
    return 0
}

domainsToTry()
{
    cat <<! |
meta
google
!
    awk  '
    /^[ \t]*$/ { next }
    /^[ \t]*;/ { next }
    /^[ \t]*#/ { next }
    { print $1 }
    '
}

makeTestDataTldFromDomains()
{
    local tld="$1"

    domainsToTry |
    while read domain
    do
        [ "$VERBOSE" = "1" ] && echo "try: $domain.$tld"
        makeTestDataOriginalOneTldDomain "$tld" "$domain"
        [ -s "$TMPDIR/$tld/input" ] && {
            [ "$VERBOSE" = "1" ] && ls -l "$TMPDIR/$tld/"
            testNameserverExistsInInputAndOutput "$tld" && break
        }
    done
}

makeRulesFromTldIfExist()
{
    local tld="$1"
    local tld2=$(echo $tld | tr "." "_" ) # here we need to replace all . into _

    ./test2.py -R -d "$tld2" > "$TMPDIR/$tld/__rules__"
    [ -s "$TMPDIR/$tld/__rules__" ]
}

makeTestDataOriginalOneTld()
{
    local tld="$1"

    [ "$VERBOSE" = "1" ] && echo "try: $tld"

    makeDirectoryForTld "$tld" "$domain" || exit 101
    makeRulesFromTldIfExist "$tld"
    makeTestDataTldFromDomains "$tld"
}

makeTestDataOriginalAllTldSupported()
{
    getAllTldSupported |
    sort |
    while read tld
    do
        makeTestDataOriginalOneTld "$tld"
    done
}

main()
{
    prepTempDir

    [ "$#" = "0" ] && {
        makeTestDataOriginalAllTldSupported
        return
    }

    for tld in $*
    do
        makeTestDataOriginalOneTld "$tld"
    done
}

main $* 2>&1 |
tee out
