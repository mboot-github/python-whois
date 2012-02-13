import subprocess
import time
import sys
import os

PYTHON_VERSION = sys.version_info[0]
CACHE = {}
CACHE_MAX_AGE = 60*60*48	# 48h

if PYTHON_VERSION >= 3:
	import json

else:
	import simplejson as json




def cache_load(cf):
	if not os.path.isfile(cf): return
	global CACHE
	f = open(cf, 'r')
	try: CACHE = json.load(f)
	except: pass
	f.close()


def cache_save(cf):
	global CACHE
	f = open(cf, 'w')
	json.dump(CACHE, f)
	f.close()





def do_query(dl, force=0, cache_file=None, slow_down=0):
	k = '.'.join(dl)
	if cache_file: cache_load(cache_file)
	if force or k not in CACHE or CACHE[k][0] < time.time() - CACHE_MAX_AGE:
		CACHE[k] = (
			int(time.time()),
			_do_whois_query(dl),
		)
		if cache_file: cache_save(cache_file)
		if slow_down: time.sleep(slow_down)

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