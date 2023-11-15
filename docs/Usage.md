# Usage

## Requirements

  * Install the cli `whois` of your operating system if it is not present already,
  * Debian / Ubuntu:
      * `sudo apt install whois`
  * Fedora/Centos/Rocky:
      * `sudo yum install whois`

## whois used in python (compatible with the Danny Cork version)

### example for fedora 37


    sudo yum install whois
    pip install whoisdomain

    python
    # to make it compatible with Danny_Cork whois
    >>> import whoisdomain as whois
    >>> d = whois.query('google.com')
    >>> print(d.__dict__)

    {'name': 'google.com', 'tld': 'com', 'registrar': 'MarkMonitor, Inc.', 'registrant_country': 'US', 'creation_date': datetime.datetime(1997, 9, 15, 9, 0), 'expiration_date': datetime.datetime(2028, 9, 13, 9, 0), 'last_updated': datetime.datetime(2019, 9, 9, 17, 39, 4), 'status': 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'statuses': ['clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)', 'clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)', 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)', 'serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)', 'serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)'], 'dnssec': False, 'name_servers': ['ns1.google.com', 'ns2.google.com', 'ns3.google.com', 'ns4.google.com'], 'registrant': 'Google LLC', 'emails': ['abusecomplaints@markmonitor.com', 'whoisrequest@markmonitor.com']}

    >>> print (d.expiration_date)
    2028-09-13 09:00:00

    >>> print(d.name)
    google.com

    >>> print (d.creation_date)
    1997-09-15 09:00:00
