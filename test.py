import whois
from pprint import pprint

keys = ['creation_date','updated_date','expiration_date','registrar']

domsins = ['www.google.com','www.google.org','www.fsdfsdfsdfsd.google.com']


for d in domsins:
	print('-'*80)
	w = whois.query(d)
	for k in keys:
		print(k, w[k])
