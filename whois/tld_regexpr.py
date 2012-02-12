com = {
'extend': None,

'domain_name':				r'Domain Name:\s?(.+)',
'registrar':				r'Registrar:\s?(.+)',
'registrant':				None,

'creation_date':			r'Creation Date:\s?(.+)',
'expiration_date':			r'Expiration Date:\s?(.+)',
'updated_date':				r'Updated Date:\s?(.+)',

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

'registrant':				r'Registrant:\n\s*(.+)',

'creation_date':			r'Registered on:\s*(.+)',
'expiration_date':			r'Renewal date:\s*(.+)',
'updated_date':				r'Last updated:\s*(.+)',

'name_servers':				r'Name Servers:\s?(.+)',
'status':					r'Registration status:\n\s*(.+)',
}

pl = {
'extend': 'uk',

'creation_date':			r'\ncreated:\s*(.+)\n',
'updated_date':				r'\nlast modified:\s*(.+)\n',

'name_servers':				r'\nnameservers:\s?(.+)',
'status':					r'\nStatus:\n\s*(.+)',
}

ru = {
'extend': 'com',

'domain_name':				r'\ndomain:\s*(.+)',

'creation_date':			r'\ncreated:\s*(.+)',
'expiration_date':			r'\npaid-till:\s*(.+)',

'name_servers':				r'\nnserver:\s*(.+)',
'status':					r'\nstate:\s*(.+)',
}

jp = {
'domain_name':				r'\[Domain Name\]\s?(.+)',
'registrar':				None,
'registrant':				r'\[Registrant\]\s?(.+)',

'creation_date':			r'\[Created on\]\s?(.+)',
'expiration_date':			r'\[Expires on\]\s?(.+)',
'updated_date':				r'\[Last Updated\]\s?(.+)',

'name_servers':				r'\[Name Server\]\s?(.+)',
'status':					r'\[Status\]\s?(.+)',
'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


de = {
'extend': 'com',

'domain_name':				r'\ndomain:\s*(.+)',

'updated_date':				r'\nChanged:\s?(.+)',
}

eu = {
'extend': 'com',

'domain_name':				r'\ndomain:\s*(.+)',
'registrar':				r'Name:\s?(.+)',
}

biz = {
'extend': 'com',

'registrar':				r'Sponsoring Registrar:\s?(.+)',
'registrant':				r'Registrant Organization:\s?(.+)',

'creation_date':			r'Domain Registration Date:\s?(.+)',
'expiration_date':			r'Domain Expiration Date:\s?(.+)',
'updated_date':				r'Domain Last Updated Date:\s?(.+)',

'status':					None,
}

info = {
'extend': 'biz',

'creation_date':			r'Created On:\s?(.+)',
'expiration_date':			r'Expiration Date:\s?(.+)',
'updated_date':				r'Last Updated On:\s?(.+)',

'status':					r'Status:\s?(.+)',
}

name = {
'extend': 'com',

'status':					r'Domain Status:\s?(.+)',
}

us = {
'extend': 'name',
}

co = {
'extend': 'biz',

'status':					r'Status:\s?(.+)',
}

me = {
'extend': 'biz',

'creation_date':			r'Domain Create Date:\s?(.+)',
'expiration_date':			r'Domain Expiration Date:\s?(.+)',
'updated_date':				r'Domain Last Updated Date:\s?(.+)',

'name_servers':				r'Nameservers:\s?(.+)',
'status':					r'Domain Status:\s?(.+)',
}

be = {
'extend': 'pl',

'domain_name':				r'\nDomain:\s*(.+)',
'registrar':				r'Company Name:\n?(.+)',

'creation_date':			r'Registered:\s*(.+)\n',

'status':					r'Status:\s?(.+)',
}