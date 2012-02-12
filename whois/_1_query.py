import subprocess
import time
import sys

PYTHON_VERSION = sys.version_info[0]
CACHE = {}
CACHE_MAX_AGE = 60*60*48	# 48h



def do_query(dl, force=0):
	k = '.'.join(dl)
	if force or k not in CACHE or CACHE[k][0] < time.time() - CACHE_MAX_AGE:
		CACHE[k] = (
			time.time(),
			_do_whois_query(dl),
		)

	return CACHE[k][1]




def _do_whois_query(dl):
	"""
		Linux 'whois' command wrapper
	"""
	p = subprocess.Popen(['whois', '.'.join(dl)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	r = p.communicate()[0]
	if p.returncode != 0: raise Exception(r)
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