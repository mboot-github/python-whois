#! /usr/bin/bash

# signal whois module that we are testing, this reads data from testdata/<domain>/in
TestDataDir=$(realpath ./testdata)
export TEST_WHOIS_PYTHON="$TestDataDir"

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

    diff "$TestDataDir/$domain/output" "$TestDataDir/$domain/test.out" | tee "$TestDataDir/$domain/out"
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
