# imports

import json
import os
import socket
import sys

BASE_PATH = "%s/%s" % os.path.split(os.path.dirname(os.path.realpath(__file__)))

COMMON_PATH = "%s/common/" % (BASE_PATH )
sys.path.append(BASE_PATH)
sys.path.append(COMMON_PATH)

import githubSync

def processError(err_t):
	if err_t[0] > 0:
		print "processError:", err_t[2], err_t[1]

stat_t = githubSync.main(BASE_PATH)
print repr(stat_t)
processError(stat_t)

with open(COMMON_PATH + 'settings.json', 'r') as f:
    SETTINGS = json.load(f, encoding="UTF-8")

HOSTNAME = socket.gethostname()

if unicode(HOSTNAME) in SETTINGS["servers"]:
	print "load server"
else:
	CLIENT_PATH = "%s/client/" % (BASE_PATH )
	sys.path.append(CLIENT_PATH)
	import client_main
	



