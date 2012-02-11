import whois
from pprint import pprint

keys = ['creation_date','updated_date','expiration_date','registrar']

domsins = ['www.google.com','www.google.org','www.fsdfsdfsdfsd.google.com','google.net','google.pl']


for d in domsins:
	print('-'*80)
	print(d)
	w = whois.query(d)
	for k in keys:
		print(k, w[k])
