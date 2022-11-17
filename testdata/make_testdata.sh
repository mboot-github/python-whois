#! /usr/bin/bash

DOMAINS=(
    example.net # has iana source
    example.com # has iana source
    example.org # has no iana source
    meta.co.uk # has multiline for all relevant fields and 4 nameservers; should be fixed output has only 2
    xs4all.nl # has multiline nameserver and multiline registrar; outout has no nameservers should be 2
    meta.com.sg # has mail
    meta.com # have emails
    google.com # have emails
    meta.jp # jp has [registrar] type keywords not registrar:
    meta.co.jp # jp has [registrar] type keywords not registrar:
    meta.kr # has both korean and english text
)

for str in ${DOMAINS[@]}
do
    echo "$str"

    # create one dir for each domain we will test
    mkdir -p "$str"

    # dump the raw whois data as in
    whois "$str" | tee "./$str/input"

    # dump the expected output as output
    ../test2.py -d "$str" | tee "./$str/output"
done
