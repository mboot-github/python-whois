import re
import sys
import datetime

PYTHON_VERSION = sys.version_info[0]



class Domain:

	def __init__(self, data):
		self.name				= data['domain_name'][0].strip().lower()
		self.registrar			= data['registrar'][0].strip()
		self.creation_date		= str_to_date(data['creation_date'][0])
		self.expiration_date	= str_to_date(data['expiration_date'][0])
		self.last_updated		= str_to_date(data['updated_date'][0])

		#----------------------------------
		# name_servers
		tmp = []
		for x in data['name_servers']:
			if isinstance(x, str): tmp.append(x)
			else:
				for y in x: tmp.append(y)

		self.name_servers = set()
		for x in tmp:
			x = x.strip(' .')
			if x:
				if ' ' in x:
					x, _ = x.split(' ', 1)
					x = x.strip(' .')

				self.name_servers.add(x.lower())

		#----------------------------------












# http://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_FORMATS = [
	'%d-%b-%Y',						# 02-jan-2000
	'%d.%m.%Y',						# 02.02.2000
	'%d/%m/%Y',						# 01/06/2011
	'%Y-%m-%d',						# 2000-01-02
	'%Y.%m.%d',						# 2000.01.02
	'%Y/%m/%d',						# 2005/05/30

	'%Y.%m.%d %H:%M:%S',			# 2002.09.19 13:00:00
	'%Y%m%d %H:%M:%S',			    # 20110908 14:44:51
	'%Y-%m-%d %H:%M:%S',		    # 2011-09-08 14:44:51
	'%d.%m.%Y  %H:%M:%S',			# 19.09.2002 13:00:00
	'%d-%b-%Y %H:%M:%S %Z',			# 24-Jul-2009 13:20:03 UTC
	'%Y/%m/%d %H:%M:%S (%z)',		# 2011/06/01 01:05:01 (+0900)
	'%Y/%m/%d %H:%M:%S',			# 2011/06/01 01:05:01
	'%a %b %d %H:%M:%S %Z %Y',		# Tue Jun 21 23:59:59 GMT 2011
	'%a %b %d %Y',					# Tue Dec 12 2000
	'%Y-%m-%dT%H:%M:%S',			# 2007-01-26T19:10:31
	'%Y-%m-%dT%H:%M:%SZ',			# 2007-01-26T19:10:31Z
	'%Y-%m-%dT%H:%M:%S%z',			# 2011-03-30T19:36:27+0200
	'%Y-%m-%dT%H:%M:%S.%f%z',		# 2011-09-08T14:44:51.622265+03:00
	'%Y-%m-%dt%H:%M:%S.%f',			# 2011-09-08t14:44:51.622265
]


def str_to_date(s):
	s = s.strip().lower()
	if not s or s == 'not defined': return

	s = s.replace('(jst)', '(+0900)')
	s = re.sub('(\+[0-9]{2}):([0-9]{2})', '\\1\\2', s)

	if PYTHON_VERSION < 3: return str_to_date_py2(s)

	for format in DATE_FORMATS:
		try: return datetime.datetime.strptime(s, format)
		except ValueError as e: pass

	raise ValueError("Unknown date format: '%s'" % s)


def str_to_date_py2(s):
	tmp = re.findall('\+([0-9]{2})00', s)
	if tmp: tz = int(tmp[0])
	else: tz = 0

	for format in DATE_FORMATS:
		try: return datetime.datetime.strptime(s, format) + datetime.timedelta(hours=tz)
		except ValueError as e: pass

	raise ValueError("Unknown date format: '%s'" % s)

