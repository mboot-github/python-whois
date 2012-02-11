com = {
'extend': None,
'not_found_message': "No match for \"",

'domain_name':      'Domain Name:\s?(.+)',
'registrar':        'Registrar:\s?(.+)',
'whois_server':     'Whois Server:\s?(.+)',
'referral_url':     'Referral URL:\s?(.+)',
'updated_date':     'Updated Date:\s?(.+)',
'creation_date':    'Creation Date:\s?(.+)',
'expiration_date':  'Expiration Date:\s?(.+)',
'name_servers':     'Name Server:\s?(.+)',
'status':           'Status:\s?(.+)',
'emails':           '[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


org = {
'extend': 'com',

'creation_date':    'Created On:\s?(.+)',
'updated_date':     'Last Updated On:\s?(.+)',
}
