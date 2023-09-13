#! /bin/bash

doIt()
{
    black --line-length 160 whois
    pylama --max-line-length 160 whois/
}

main()
{
    ls *.py >/dev/null 2>/dev/null && doIt
    # ./test.py
    mypy --implicit-optional --install-types --non-interactive --namespace-packages whois
}

main
