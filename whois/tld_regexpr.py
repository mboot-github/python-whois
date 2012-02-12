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
}

ru = {
'extend': 'com',

'domain_name':				r'\ndomain:\s*(.+)',

'creation_date':			r'\ncreated:\s*(.+)',
'expiration_date':			r'\npaid-till:\s*(.+)',

'name_servers':				r'\nnserver:\s*(.+)',
'status':					r'\nstate:\s*(.+)',
'emails':					r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
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

"""
NOT Tested:


name = {
'domain_name_id':  'Domain Name ID:\s*(.+)',
'domain_name':     'Domain Name:\s*(.+)',
'registrar_id':    'Sponsoring Registrar ID:\s*(.+)',
'registrar':       'Sponsoring Registrar:\s*(.+)',
'registrant_id':   'Registrant ID:\s*(.+)',
'admin_id':        'Admin ID:\s*(.+)',
'technical_id':    'Tech ID:\s*(.+)',
'billing_id':      'Billing ID:\s*(.+)',
'creation_date':   'Created On:\s*(.+)',
'expiration_date': 'Expires On:\s*(.+)',
'updated_date':    'Updated On:\s*(.+)',
'name_server_ids': 'Name Server ID:\s*(.+)',
'name_servers':    'Name Server:\s*(.+)',
'status':          'Domain Status:\s*(.+)',
}

"""