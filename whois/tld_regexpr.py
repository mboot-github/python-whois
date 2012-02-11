com = {
'extend': None,
'not_found_message':		'No match for "',

'domain_name':				'\nDomain Name:\s?(.+)',
'registrar':				'\nRegistrar:\s?(.+)',
'whois_server':				'\nWhois Server:\s?(.+)',
'referral_url':				'\nReferral URL:\s?(.+)',
'updated_date':				'\nUpdated Date:\s?(.+)',
'creation_date':			'\nCreation Date:\s?(.+)',
'expiration_date':			'\nExpiration Date:\s?(.+)',
'name_servers':				'\nName Server:\s?(.+)',
'status':					'\nStatus:\s?(.+)',
'emails':					'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

org = {
'extend': 'com',

'creation_date':			'\nCreated On:\s?(.+)',
'updated_date':				'\nLast Updated On:\s?(.+)',
}

uk = {
'extend': 'com',

'registrar_url':			'\nURL:\s*(.+)',
'status':					'\nRegistration status:\n\s*(.+)',
'registrant_name':			'\nRegistrant:\n\s*(.+)',
'creation_date':			'\nRegistered on:\s*(.+)',
'expiration_date':			'\nRenewal date:\s*(.+)',
'updated_date':				'\nLast updated:\s*(.+)',
}

pl = {
'extend': 'uk',

'creation_date':			'\ncreated:\s*(.+)\n',
'updated_date':				'\nlast modified:\s*(.+)\n',
}