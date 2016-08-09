#############################################
##### MODULES, EVENIRONMENT AND GLOBALS #####
#############################################

import json
import os
import struct
import time
import threading
import sys
import socket
import traceback
#import errorlog as elog

# constants
#PI_NATIVE = os.uname()[4].startswith("arm") # TRUE if running on RPi
#BASE_PATH = "/home/pi/nervebox_2/" if PI_NATIVE else "/home/stella/Dropbox/projects/current/nervebox_2/" 
HOSTNAME = socket.gethostname()
#HOSTNAME = "R8MKII"
BASE_PATH = "%s/%s" % (os.path.split(os.path.dirname(os.path.realpath(__file__)))[0], os.path.split(os.path.dirname(os.path.realpath(__file__)))[1])
CLIENT_PATH = "%s/client/" % (BASE_PATH )
DEVICES_PATH = "%s/client/devices/" % (BASE_PATH )
COMMON_PATH = "%s/common/" % (BASE_PATH )
HOST_SPECIFIC_PATH = "%s/client/devices/%s/" % (BASE_PATH, HOSTNAME)
SERVER_PATH = "%s/server/" % (BASE_PATH )
STORE_PATH = "%s/store/" % SERVER_PATH
clientnames = ("blueberrypie","blackberrypie")
ROLE = sys.argv[1]
print HOST_SPECIFIC_PATH
possible_responses = ["client", "server", "dashboard"]
while ROLE not in possible_responses:
    ROLE = raw_input('Please type dashboard, client or server: ')
if ROLE == "server":
    HOSTNAME = "**SERVER**"
if ROLE == "dashboard":
    HOSTNAME = "**DASHBOARD**"
print 'role: ', ROLE
print 'paths loaded'

# local paths
sys.path.append(BASE_PATH)
sys.path.append(COMMON_PATH)
sys.path.append(CLIENT_PATH)
sys.path.append(SERVER_PATH)
sys.path.append(HOST_SPECIFIC_PATH)

print "path append ok"
print os.path.split(os.path.dirname(os.path.realpath(__file__)))

try:
    # import local modules
    import dps
    import nerveOSC
    if ROLE != "client":
        import parseOsc
        import midiToOsc
        import midiDeviceManager
        import midiserver

    print "import local modules ok"

    # load config
    with open(COMMON_PATH + 'settings.json', 'r') as f:
        SETTINGS = json.load(f)

    #with open(COMMON_PATH + 'mappings.json', 'r') as f:
    #    MAPPINGS = json.load(f)
    #
    #print "load config ok"
    #
    #MAPPING = MAPPINGS["MAPPINGS"]["default"] # todo: the mapping name will have to be dynamically updated



    ######################
    ##### NETWORKING #####
    ######################

    if ROLE == "client":
        subscribernames = ["nervebox"]
        import mapping  # host-specific mapping
        import midiOutput
        midi_output = midiOutput.Midi_Output()
        def osc_handler(msg):
            try:
                category = msg['innerpath'].split('/')
                if category[2] == "sound":
                    new_path = msg["innerpath"].replace('/%s'%HOSTNAME,'')
                    print new_path
                    mapped = mapping.mapping[new_path]
                    print 'AEEEE ',mapped
                    midi_output.send_midi(msg['params'], mapped[1]['status'], mapped[1]['channel'], mapped[1]['pitch'])
            except Exception as e:
                traceback.print_exc()
                print "device: path not found", e


    else:
        subscribernames = filter(lambda x: os.path.isdir(os.path.join(DEVICES_PATH, x)), os.listdir(DEVICES_PATH))
        subscribernames.append("nervebox2")
        subscribernames.append(HOSTNAME)

    print "subscribernames ok"
    print "initializing network..."

    if ROLE == 'server': 
        import vimina
        def osc_handler(msg):
            pass


    dps.init_networking(
        subscribernames,
        HOSTNAME,
        ROLE,
        SETTINGS["pubsub_pubPort"],
        SETTINGS["pubsub_pubPort2"],
        SETTINGS["discovery_multicastGroup"],
        SETTINGS["discovery_multicastPort"],
        SETTINGS["discovery_multicastPort2"],
        SETTINGS["discovery_responsePort"],
        SETTINGS["discovery_responsePort2"],
        osc_handler
    )

except Exception as e:
    print e
    #elog.elog.logerror()
