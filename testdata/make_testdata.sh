#! /usr/bin/bash

WHERE=$( dirname $0 )

getDomains()
{
    cat DOMAINS.txt |
    awk '
    /^[ \t]*;/ { next }
    /^[ \t]*#/ { next }
    /^[ \t]*$/ { next }
    { print $1 }
    '
}

verifyNameservers()
{
    local str="$1"

    grep name_servers  "./$str/output" |
    awk '{ $1 = $2 = ""; print }' |
    awk -F, '{print NF}'

    grep "name server" "./$str/nameservers" |
    wc -l
}

makeDataForDomain()
{
    local str="$1"

    # create one dir for each domain we will test
    mkdir -p "$str"

    # dump the raw whois data as in
    whois "$str" |
    tee "./$str/input"

    # dump the expected output as output
    ../bin/test2.py -d "$str" |
    tee "./$str/output"

    # dump the nameservers via host
    host -t ns "$str" |
    tee "./$str/nameservers"

    # verifyNameservers "$str"
}

main()
{
    local force="$1"

    cd "${WHERE}"
    getDomains |
    while read str
    do
        [ "$force" == "force" ] && {
            makeDataForDomain "$str"
            continue
        }

        [ ! -d "$str" ] && {
            makeDataForDomain "$str"
        }
    done
}

main $*
