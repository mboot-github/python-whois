#! /usr/bin/bash

DOMAINS=(
    example.net # has iana source
    example.com # has iana source
    example.org # has no iana source
    meta.co.uk # has multiline for all relevant fields and 4 nameservers; should be fixed output has only 2
    # xs4all.nl # has multiline nameserver and multiline registrar; outout has no nameservers should be 2
)

for str in ${DOMAINS[@]}
do
    echo "$str"

    # create one dir for each domain we will test
    mkdir -p "$str"

    # dump the raw whois data as in
    whois "$str" | tee "./$str/input"

    # dump the expected output as out
    ../test2.py -d "$str" | tee "./$str/output"
done
