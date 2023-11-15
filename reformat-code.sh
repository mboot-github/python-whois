#! /bin/bash

LL=160

doIt()
{
    black --line-length $LL whois
    pylama --max-line-length $LL whois/
}

main()
{
    ls *.py >/dev/null 2>/dev/null && doIt
    # ./test.py
    mypy --implicit-optional --install-types --non-interactive --namespace-packages whois
}

main
