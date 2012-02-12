import subprocess
import sys

PYTHON_VERSION = sys.version_info[0]



def _do_whois_query(dl):
	"""
		Linux 'whois' command wrapper
	"""
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