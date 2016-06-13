# imports

import json
import os
import socket
import sys


print os.path.realpath(__file__)
print os.path.split(os.path.dirname(os.path.realpath(__file__)))

BASE_PATH = "%s/%s" % os.path.split(os.path.dirname(os.path.realpath(__file__)))

print BASE_PATH

COMMON_PATH = "%s/common/" % (BASE_PATH )
sys.path.append(BASE_PATH)
sys.path.append(COMMON_PATH)

print COMMON_PATH

import githubSync

stat_t = githubSync.main(BASE_PATH)
print stat_t

"""
with open(COMMON_PATH + 'settings.json', 'r') as f:
    SETTINGS = json.load(f)

HOSTNAME = socket.gethostname()

#---------

simurgh_shell

test installed libraries?

git pull

start appropriate main.py, pass hostname
"""