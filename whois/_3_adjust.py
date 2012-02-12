
class Domain:

	def __init__(self, data):
		self.name				= data['domain_name'][0].strip().lower()
		self.registrar			= data['registrar'][0].strip()
		self.creation_date		= str_to_date(data['creation_date'][0])
		self.expiration_date	= str_to_date(data['expiration_date'][0])
		self.last_updated		= str_to_date(data['updated_date'][0])












import datetime


# http://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_FORMATS = [
	'%d-%b-%Y',						# 02-jan-2000
	'%d.%m.%Y',						# 02.02.2000
	'%Y-%m-%d',						# 2000-01-02
	'%Y.%m.%d',						# 2000.01.02
	'%Y/%m/%d',						# 2005/05/30
	'%Y.%m.%d %H:%M:%S',			# 2002.09.19 13:00:00
	'%d-%b-%Y %H:%M:%S %Z',			# 24-Jul-2009 13:20:03 UTC
	'%Y/%m/%d %H:%M:%S (%z)',		# 2011/06/01 01:05:01 (JST)
	'%a %b %d %H:%M:%S %Z %Y',		# Tue Jun 21 23:59:59 GMT 2011
	'%Y-%m-%dT%H:%M:%SZ',			# 2007-01-26T19:10:31Z
	'%Y-%m-%dT%H:%M:%S%z',			# 2011-03-30T19:36:27+0200
]


def str_to_date(s):
	s = s.strip()
	if not s: return

	# TODO: beznadziejne wyjatki !
	if s.endswith('+02:00'): s = s.replace('+02:00', '+0200')
	s = s.replace('(JST)', '(+0900)')

	for format in DATE_FORMATS:
		try: return datetime.datetime.strptime(s, format)
		except ValueError as e: pass

	raise ValueError("Unknown date format: '" + s + "'")
