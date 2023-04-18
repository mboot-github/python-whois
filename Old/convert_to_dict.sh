#! /usr/bin/env bash

FILE="whois/tld_regexpr.py"
FILE2="whois/tld_regexpr2.py"

cat "$FILE" |
perl -np -e '
# translate all tld to DICT and substitute for the real tld in case of _
s/^([a-z]+)_([a-z]+)\s+=/ZZ["$1.$2"] =/;
s/^([a-z]+)\s+=/ZZ["$1"] =/;
# if we refer to a tld also change _ to .
s/"extend":\s+"(\w+)_(\w+)"/"extend": "$1.$2"/;
' |
tee "$FILE2"
