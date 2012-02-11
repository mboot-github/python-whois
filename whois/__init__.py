import sys
import re


PYTHON_VERSION = sys.version_info[0]




def query(domain):
	assert isinstance(domain, str), Exception('`domain` - must be <str>')
	domain = domain.lower().strip()
	d = domain.split('.')
	if d[0] == 'www': d = d[1:]
	#print(d)

	r = _do_whois_query(d)
	return _do_parse(r, d[-1])




#----------------------------------------------------------------------------------------------------


import subprocess

def _do_whois_query(dl):
	r = subprocess.Popen(['whois', '.'.join(dl)], stdout=subprocess.PIPE).stdout.read()
	return r.decode() if PYTHON_VERSION == 3 else r



"""
import socket

def _do_whois_query(dl):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((('%s.whois-servers.net' % dl[-1], 43)))
	s.send(("%s\r\n" % '.'.join(dl)).encode())

	response = []
	while 1:
		t = s.recv(4096)
		response.append(t)
		if t == b'': break

	s.close()
	return b''.join(response).decode()
"""

#----------------------------------------------------------------------------------------------------

from .tld import TLD_RE

def _do_parse(whois_str, tld):
	r = {}

	sn = re.findall(r'Server Name:\s?(.+)', whois_str, re.IGNORECASE)
	if sn:
		whois_str = whois_str[whois_str.find('Domain Name:'):]

	for k, v in TLD_RE.get(tld, TLD_RE['com']).items():
		r[k] = re.findall(v, whois_str, re.IGNORECASE)

	return r




