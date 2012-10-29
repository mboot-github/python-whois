import whois
from pprint import pprint


domains = '''
www.google.com
www.fsdfsdfsdfsd.google.com
digg.com
imdb.com
microsoft.com

www.google.org
ddarko.org

google.net
www.asp.net

google.pl
www.ddarko.pl

google.co.uk

google.jp
www.google.co.jp

google.co
google.de
yandex.ru
google.us
google.eu
google.me
google.be
google.biz
google.info
google.name

google.it
google.cz
google.fr

dfsdfsfsdf
test.ez.lv
'''

#domains = ''


for d in domains.split('\n'):
	if d:
		print('-'*80)
		print(d)
		w = whois.query(d, ignore_returncode=1)
		if w:
			wd = w.__dict__
			for k, v in wd.items():
				print('%20s\t"%s"' % (k, v))

