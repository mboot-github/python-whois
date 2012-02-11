com = {
'extend': None,
'not_found_message':		r'No match for "',

'domain_name':				r'Domain Name:\s?(.+)',
'registrar':				r'Registrar:\s?(.+)',
'whois_server':				r'Whois Server:\s?(.+)',
'referral_url':				r'Referral URL:\s?(.+)',
'updated_date':				r'Updated Date:\s?(.+)',
'creation_date':			r'Creation Date:\s?(.+)',
'expiration_date':			r'Expiration Date:\s?(.+)',
'name_servers':				r'Name Server:\s?(.+)',
'status':					r'Status:\s?(.+)',
'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

org = {
'extend': 'com',

'creation_date':			r'\nCreated On:\s?(.+)',
'updated_date':				r'\nLast Updated On:\s?(.+)',
}

uk = {
'extend': 'com',

'registrar_url':			r'URL:\s*(.+)',
'status':					r'Registration status:\n\s*(.+)',
'registrant_name':			r'Registrant:\n\s*(.+)',
'creation_date':			r'Registered on:\s*(.+)',
'expiration_date':			r'Renewal date:\s*(.+)',
'updated_date':				r'Last updated:\s*(.+)',
}

pl = {
'extend': 'uk',

'creation_date':			r'\ncreated:\s*(.+)\n',
'updated_date':				r'\nlast modified:\s*(.+)\n',
}