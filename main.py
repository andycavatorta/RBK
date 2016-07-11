""" IMPORTS AND GLOBALS """

import json
import os
import socket
import sys

BASE_PATH = "%s/%s" % os.path.split(os.path.dirname(os.path.realpath(__file__)))

COMMON_PATH = "%s/common/" % (BASE_PATH )
DATA_PATH = "%s/data/" % (BASE_PATH )
LOG_PATH = "%s/logs/" % (BASE_PATH )
sys.path.append(BASE_PATH)
sys.path.append(COMMON_PATH)

import packageManager
import errorlog as elog

SETTINGS = {} # overwritten below

""" START GLOBAL SYSTEMS """

try:
	packageManager.update(
	    BASE_PATH,
	    DATA_PATH,
	    LOG_PATH,
	    COMMON_PATH,
	    errorlogger
	)

except:
	elog.elog.logerror()

""" FETCH NEW PYTHON CODE """

#stat_t = githubSync.main(BASE_PATH)
#print repr(stat_t)
#errorlogger(stat_t)

with open(COMMON_PATH + 'settings.json', 'r') as f:
    SETTINGS = json.load(f, encoding="UTF-8")


""" LOAD HOST-SPECIFIC CODE """
"""
HOSTNAME = socket.gethostname()
if unicode(HOSTNAME) in SETTINGS["servers"]:
	print "load server"
else:
	CLIENT_PATH = "%s/client/" % (BASE_PATH )
	sys.path.append(CLIENT_PATH)
	import client_main
"""
""" NETWORK DISCOVERY AND SELF-ASSEMBLY """




