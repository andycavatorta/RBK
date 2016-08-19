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
import netifaces as ni
import commands
#import errorlog as elog
# constants
#PI_NATIVE = os.uname()[4].startswith("arm") # TRUE if running on RPi
#BASE_PATH = "/home/pi/nervebox_2/" if PI_NATIVE else "/home/stella/Dropbox/projects/current/nervebox_2/" 
HOSTNAME = socket.gethostname()
BASE_PATH = "%s/%s" % os.path.split(os.path.dirname(os.path.realpath(__file__)))
CLIENT_PATH = "%s/client/" % (BASE_PATH )
DEVICES_PATH = "%s/client/devices/" % (BASE_PATH )
COMMON_PATH = "%s/common/" % (BASE_PATH )
HOST_SPECIFIC_PATH = "%s/client/devices/%s/" % (BASE_PATH, HOSTNAME)
SERVER_PATH = "%s/server/" % (BASE_PATH )
STORE_PATH = "%s/store/" % SERVER_PATH
DATA_PATH = "%s/data/" % (BASE_PATH )
LOG_PATH = "%s/logs/" % (BASE_PATH )
clientnames = ("blueberrypie","blackberrypie")
ROLE = sys.argv[1]
print HOST_SPECIFIC_PATH
possible_responses = set(["client", "server", "dashboard"])
while ROLE not in possible_responses:
    ROLE = raw_input('Please type dashboard, client or server: ')
if ROLE == "server":
    HOSTNAME = "**SERVER**"
if ROLE == "dashboard":
    HOSTNAME = "**DASHBOARD**"
print 'role: ', ROLE
print 'paths loaded'

if ROLE == "client":
    print 'here'
    while commands.getoutput('cat /sys/class/net/wlan0/carrier') == '0':
        time.sleep(5)
        print 'sleeping...'

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

    print "load config ok"

    ######################
    ##### GITHUB SYNC ####
    ######################

    print "starting github sync..."

    import githubSync
    import packageManager

    def errorlogger(err_t):
        if err_t[0] > 0:
            print "errorlogger:", err_t[2], err_t[1]

    ### START GLOBAL SYSTEMS ###

    packageManager.update(
        BASE_PATH,
        DATA_PATH,
        LOG_PATH,
        COMMON_PATH,
        errorlogger
    )

    ### FETCH NEW PYTHON CODE ###

    stat_t = githubSync.main(BASE_PATH)
    print repr(stat_t)

    print "github sync ok"

    ######################
    ##### NETWORKING #####
    ######################

    if ROLE == "client":
        subscribernames = ["nervebox"]
        import blinkip
        import mapping  # host-specific mapping
        import midiOutput
        midi_output = midiOutput.Midi_Output()
        def osc_handler(msg):
            try:
                category = msg['innerpath'].split('/')
                new_path = msg["innerpath"].replace('/%s'%HOSTNAME,'')
                mapped = mapping.mapping[new_path]
                if category[2] == "sound":
                    midi_output.send_midi(msg['params'], mapped[1]['status'], mapped[1]['channel'], mapped[1]['pitch'])
                elif category[2] == "control_change":
                    midi_output.send_midi(None, mapped[1]['status'],mapped[1]['channel'], mapped[1]['cc'], msg['params']['value'])
                elif category[2] == "pitch_wheel":
                    midi_output.send_midi(None, mapped[1]['status'],msg['params']['channel'], msg['params']['value'])
            except Exception as e:
                traceback.print_exc()
                print "device: path not found", e


    else:
        import vimina
        def osc_handler(msg):
            pass
        subscribernames = filter(lambda x: os.path.isdir(os.path.join(DEVICES_PATH, x)), os.listdir(DEVICES_PATH))
        subscribernames.append("nervebox2")
        subscribernames.append(HOSTNAME)

    print "subscribernames ok"
    print "initializing network..."
    print 'subscribers: ', subscribernames

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
