#! /usr/bin/bash

DOMAINS=(
    example.net
    example.com
    example.org
    meta.co.uk
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
