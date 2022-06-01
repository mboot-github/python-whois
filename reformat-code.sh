#! /bin/bash

doItHere()
{
    black --line-length 120 *.py
    pylama *.py |
    awk '
    /xold/ { next }
    /__init__/ && / W0611/ { next }
    /ReversingLabs\/SDK\// { next }
    / W0401 / { next }
    / E501 / { next }
    / E203 / { next }
    / C901 / { next }
    { print }
    '
}

doIt()
{
    black --line-length 120 .
    pylama . |
    awk '
    /xold/ { next }
    /__init__/ && / W0611/ { next }
    /ReversingLabs\/SDK\// { next }
    / W0401 / { next }
    / E501 / { next }
    / E203 / { next }
    / C901 / { next }
    { print }
    '
}

main()
{
    ls *.py >/dev/null 2>/dev/null && doIt
}

main
