#! /bin/bash

TMPDIR="./tmp"
FORCE=0
VERBOSE=1

prepTempDir()
{
    mkdir -p "$TMPDIR" || {
        echo "FATAL: cannot make test dir: $TMPDIR" >&2
        exit 101
    }
}

getAllTldSupported()
{
    ./test2.py -S
}

makeTestDataOriginalOne()
{
    local tld="$1"
    local domain="$2"

    local d="$TMPDIR/$tld"
    mkdir -p "$d" || {
        echo "FATAL: cannot make tld directory: '$d'" >&2
        exit 101
    }

    local zz="$domain.$tld"

    host -t soa "$zz" |
    tee "$d/__dns-soa" |
    grep " has SOA record " || {
        # no soa record so that domain does not exist, cleanup the test dir
        rm -f "$d/input" "$d/output" "$d/__domain__$zz" "$d/__dns-soa" "$d/dns-ns"
        echo "INFO: no domain for $zz" >&2
        return 1
    }

    host -t ns "$zz" > "$d/__dns-ns"

    # what domain did we test
    touch "$d/__domain__$zz"

    # force english, force no cache
    [ ! -s "$d/input" -o "$FORCE" = "1" ] && {
        LANG=EN whois --force-lookup "meta.$tld" >"$d/input" || {
            # whois has a problem
            rm -f "$d/input" "$d/output" "$d/__domain__$zz" "$d/__dns-soa" "$d/dns-ns"
            return 1
        }
    }

    [ ! -s "$d/output" -o "$FORCE" = "1" ] && {
        ./test2.py -d "meta.$tld" >"$d/output"
    }

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

makeTestDataOriginalAll()
{
    getAllTldSupported |
    while read tld
    do
        echo "try: $tld"

        domainsToTry |
        while read domain
        do
            makeTestDataOriginalOne "$tld" "$domain"
            [ -f "$TMPDIR/$tld/input" ] && {
                [ "$VERBOSE" ] && {
                    ls -l "$TMPDIR/$tld/"
                }
                break
            }
        done
    done
}

main()
{
    prepTempDir
    makeTestDataOriginalAll
}

main
