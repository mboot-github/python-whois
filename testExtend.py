#!/usr/bin/python3
import whois

Verbose = True


def t1(domain: str, text: str):
    print(f"{text}: {domain}")
    try:
        d = whois.query(domain)
        if d:
            print(d.__dict__)
        else:
            print(d)
    except Exception as e:
        print(domain, e)


def xMain():
    aDictToTestOverride = {
        "si": {  # changing a existing one
            "domain_name": r"domain:\s+(.+)",
            "status": r"status:\s+(.+)",
            "registrar": r"registrar:\s+(.+)",
            "name_servers": r"nameserver:\s*(.+)",
            "creation_date": r"created:\s+(.+)",
            "expiration_date": None,
            "updated_date": None,
            "registrant_country": None,
        },
        "mk": {  # defining a non existant one, meanwhile this is now supported so the test is meaningless
            "extend": "com",
            "domain_name": r"domain:\s+(.+)",
            "status": r"status:\s+(.+)",
            "registrar": r"registrar:\s+(.+)",
            "name_servers": r"nserver:\s*(.+)",
            "creation_date": r"registered:\s+(.+)",
            "expiration_date": r"expire:\s+(.+)",
            "updated_date": r"changed:\s+(.+)",
            "registrant_country": None,
            "registrant": r"registrant:\s+(.+)",
        },
    }

    domains = [
        "google.si",
        "google.mk",
    ]
    for domain in domains:
        t1(domain, "BEFORE")

    whois.mergeExternalDictWithRegex(aDictToTestOverride)

    for domain in domains:
        t1(domain, "AFTER")


xMain()

"""

% Domain Information over Whois protocol
%
% Whoisd Server Version: 3.9.0
% Timestamp: Fri Nov 25 16:49:33 2022

domain:       google.mk
registrant:   UNET-R11
admin-c:      UNET-C12
nsset:        UNET-NS191
registrar:    UNET-REG
registered:   13.05.2008 14:00:00
changed:      17.04.2014 12:50:32
expire:       13.05.2023

contact:      UNET-R11
org:          Google LLC
name:         Google LLC
address:      Amphiteatre Parkway 1600
address:      Mountain View
address:      94043
address:      US
phone:        +1.6502530000
fax-no:       +1.6502530000
e-mail:       ccops@markmonitor.com
registrar:    UNET-REG
created:      25.03.2014 11:48:02
changed:      29.09.2021 16:26:23

contact:      UNET-C12
name:         Mark Monitor Inc.
address:      3540 East Longwing Lane Suite 300
address:      Meridian
address:      83646
address:      US
phone:        +1.2083895740
e-mail:       ccops@markmonitor.com
registrar:    UNET-REG
created:      25.03.2014 11:48:00
changed:      19.11.2019 16:47:01

nsset:        UNET-NS191
nserver:      ns2.google.com
nserver:      ns1.google.com
tech-c:       UNET-C12
registrar:    UNET-REG
created:      17.04.2014 12:50:22
changed:      17.04.2014 21:02:14


"""
