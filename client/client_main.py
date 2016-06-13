import os
import sys
import socket
#import zmq

# constants
HOSTNAME = socket.gethostname()
BASE_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
CLIENT_PATH = "%s/client/" % (BASE_PATH )
#DEVICES_PATH = "%s/client/devices/" % (BASE_PATH )
COMMON_PATH = "%s/common/" % (BASE_PATH )
#HOST_SPECIFIC_PATH = "%s/client/devices/%s/" % (BASE_PATH, HOSTNAME)

# local paths
sys.path.append(BASE_PATH)
sys.path.append(COMMON_PATH)
sys.path.append(CLIENT_PATH)
#sys.path.append(HOST_SPECIFIC_PATH)

import signalGeneratorCommandLine
