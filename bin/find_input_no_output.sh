#! /bin/bash

get_status_output()
{
    ls ./tmp/ |
    while read item
    do
        d="tmp/$item"
        [ -s "$d/input" ] && {
            [ ! -f "$d/output" ] && {
                echo "# NO_OUTPUT for $item"
            }
        }
    done
}
    
main()
{
    get_status_output
}

main
