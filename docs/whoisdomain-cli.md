# WhoisDomain as CLI command

## example for `fedora 37`

    sudo yum install whois
    pip3 install whoisdomain
    whoisdomain -d google.com

    test domain: <<<<<<<<<< google.com >>>>>>>>>>>>>>>>>>>>
    name               'google.com'
    tld                'com'
    registrar          'MarkMonitor, Inc.'
    registrant_country 'US'
    creation_date      1997-09-15 09:00:00
    expiration_date    2028-09-13 09:00:00
    last_updated       2019-09-09 17:39:04
    status             'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)'
    statuses           ['clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)', 'clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)', 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)', 'serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)', 'serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)']
    dnssec             False
    name_servers       ['ns1.google.com', 'ns2.google.com', 'ns3.google.com', 'ns4.google.com']
    registrant         'Google LLC'
    emails             ['abusecomplaints@markmonitor.com', 'whoisrequest@markmonitor.com']


## A short intro into the cli whoisdomain command

    whoisdomain
        [ -h | --usage ]
            print this text and exit

        [ -V | --Version ]
            print the build version string
            and exit

        [ -S | --SupportedTld ]
            print all known top level domains
            and exit

        [ -a | --all]
            test all existing tld currently supported
            and exit

        [ -f <filename> | --file = <filename> " ]
            use the named file to test all domains (one domain per line)
            lines starting with # or empty lines are skipped, anything after the domain is ignored
            the option can be repeated to specify more then one file
            exits after processing all the files

        [ -D <directory> | --Directory = <directory> " ]
            use the named directory, ald use all files ending in .txt as files containing domains
            files are processed as in the -f option so comments and empty lines are skipped
            the option can be repeated to specify more then one directory
            exits after processing all the dirs

        [ -d <domain> | --domain = <domain> " ]
            only analyze the given domains
            the option can be repeated to specify more domain's

        [ -v | --verbose ]
            set verbose to True,
            verbose output will be printed on stderr only

        [ -j | --json ]
            print each result as json

        [ -I | --IgnoreReturncode ]
            sets the IgnoreReturncode to True,

        [ -p | --print ]
            also print text containing the raw output of the cli whois

        [ -R | --Ruleset ]
            dump the ruleset for the requested tld and exit
            should be combined with -d to specify tld's

        [ -C <file> | --Cleanup <file> ]
            read the input file specified and run the same cleanup as in whois.query,
            then exit

        # test two domains with verbose and IgnoreReturncode
        example: whoisdomain -v -I -d meta.org -d meta.com

        # test all supported tld's with verbose and IgnoreReturncode
        example: whoisdomain -v -I -a

        # test one specific file with verbose and IgnoreReturncode
        example: whoisdomain -v -I -f tests/ok-domains.txt

        # test one specific directory with verbose and IgnoreReturncode
        example: whoisdomain -v -I -D tests



## example for Json output with the cli `whoisdomain`

        whoisdomain  -j -d hello.xyz | jq -r .

        {
          "name": "hello.xyz",
          "tld": "xyz",
          "registrar": "Namecheap",
          "registrant_country": "IS",
          "creation_date": "2014-03-20 15:01:22",
          "expiration_date": "2024-03-20 23:59:59",
          "last_updated": "2023-03-14 09:24:32",
          "status": "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
          "statuses": [
            "clientTransferProhibited https://icann.org/epp#clientTransferProhibited"
          ],
          "dnssec": false,
          "name_servers": [
            "dns1.registrar-servers.com",
            "dns2.registrar-servers.com"
          ],
          "registrant": "Privacy service provided by Withheld for Privacy ehf",
          "emails": [
            "abuse@namecheap.com"
          ]
        }
