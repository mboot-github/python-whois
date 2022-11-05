#! /usr/bin/bash

# signal whois module that we are testing, this reads data from testdata/<domain>/in
export TEST_WHOIS_PYTHON="1"

TestDataDir="./testdata"

get_testdomains()
{
    ls "$TestDataDir" |
    grep -v ".sh"
}

testOneDomain()
{
    domain="$1"
    [ ! -d "$TestDataDir/$domain" ] && return

    echo "testing: $domain"
    ./test2.py -d "$domain" >"$TestDataDir/$domain/test.out"

    diff "$TestDataDir/$domain/out" "$TestDataDir/$domain/test.out"
}

main()
{
    get_testdomains |
    while read line
    do
        testOneDomain $(basename $line)
    done
}

main
