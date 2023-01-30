#! /usr/bin/bash

getDomains()
{
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
        meta.com.tr # has utf 8 response text and different formatting style
        hello.xyz # has sometimes IANA Source beginning on mac
    )
}

verifyNameservers()
{
    local str="$1"

    grep name_servers  "./$str/output" | awk '{ $1 = $2 = ""; print }' | awk -F, '{print NF}'
    grep "name server" "./$str/nameservers" | wc -l

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
    ../test2.py -d "$str" |
    tee "./$str/output"

    # dump the nameservers via host
    host -t ns "$str" |
    tee "./$str/nameservers"

    # verifyNameservers "$str"
}

makeDataIfNotExist()
{
    for str in ${DOMAINS[@]}
    do
        [ -d "$str" ] && continue
        makeDataForDomain "$str"
    done
}

makeDataIfExist()
{
    for str in ${DOMAINS[@]}
    do
        makeDataForDomain "$str"
    done
}

main()
{
    local force="$1"
    getDomains
    makeDataIfNotExist
    [ "$force" == "force" ] && {
        makeDataIfExist
    }
}

main $*
