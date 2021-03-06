#!/usr/bin/env python

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
try:
    ROLE = sys.argv[1]
except:
    ROLE = raw_input('Please type dashboard, client or server: ')
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

# local paths
sys.path.append(BASE_PATH)
sys.path.append(COMMON_PATH)
sys.path.append(CLIENT_PATH)
sys.path.append(SERVER_PATH)
sys.path.append(HOST_SPECIFIC_PATH)

print "path append ok"
print os.path.split(os.path.dirname(os.path.realpath(__file__)))

import network_info

import sys
import time


def pauseUntilOnline():
    while True:
        if network_info.getOnlineStatus():
            print "got connection!"
            break
        else:
            print "waiting for connection..."
            time.sleep(1)

pauseUntilOnline()

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

    # print "load config ok"

    ######################
    ##### GITHUB SYNC ####
    ######################

    # print "starting github sync..."

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

    # print "github sync ok"

    ######################
    ##### NETWORKING #####
    ######################

    if ROLE == "client":
        subscribernames = ["nervebox"]
        import collectorModule
        collector = collectorModule.Collector()
        collector.daemon = True
        collector.start()
        import dashboardMenu
        dashboard = dashboardMenu.Dashboard(collector)
        dashboard.daemon = True
        dashboard.start()
        import blinkip
        import mapping  # host-specific mapping
        import midiOutput
        import signalOutput
        signal_output = signalOutput.init() # signal output as a separate process
        # signal_output = signalOutput.Channels()
        midi_output = midiOutput.Midi_Output()
        def osc_handler(msg):
            scale_max = 127
            scale_min = 0
            try:
                print "incoming osc = ", msg
                category = msg['innerpath'].split('/')
                print "category = ", category
                new_path = msg["innerpath"].replace('/%s'%HOSTNAME,'')
                print "new_path = ", new_path
                rhythm_box_actions = mapping.mapping[new_path]
                print "rhythm_box_actions = ", rhythm_box_actions
                for rhythm_box_action in rhythm_box_actions:
                    print "rhythm_box_action = ", rhythm_box_action
                    if category[2] == "sound":
                        if rhythm_box_action[0] == "MIDI":
                            midi_output.send_midi(msg['params'], rhythm_box_action[1]['status'], rhythm_box_action[1]['channel'], rhythm_box_action[1]['pitch'])
                            collector.collect("MIDI", "%s,%s,%s,%s" % (msg['params'], rhythm_box_action[1]['status'], rhythm_box_action[1]['channel'], rhythm_box_action[1]['pitch']))
                        elif rhythm_box_action[0] == "signal":
                            iterate_rhythm_box_action = iter(rhythm_box_action)
                            next(iterate_rhythm_box_action)
                            for signal in iterate_rhythm_box_action:
                                signal_output.send(signal)
                                collector.collect(rhythm_box_action[0], "%s" % (signal)) #%s,%s,%s % (msg['params'], rhythm_box_action[1]['status'], rhythm_box_action[1]['channel'], rhythm_box_action[1]['pitch']))
                    elif category[2] == "control_change":
                        if rhythm_box_action[0] == "MIDI":
                            midi_output.send_midi(None, rhythm_box_action[1]['status'],rhythm_box_action[1]['channel'], rhythm_box_action[1]['cc'], msg['params']['value'])
                            collector.collect("MIDI", "%s,%s,%s,%s" % (rhythm_box_action[1]['cc'], rhythm_box_action[1]['status'], rhythm_box_action[1]['channel'], msg['params']['value']))
                        elif rhythm_box_action[0] == "signal":
                            iterate_rhythm_box_action = iter(rhythm_box_action)
                            next(iterate_rhythm_box_action)
                            if category[3] == "master_tempo":
                                scale_max = 999.0 #* msg['params']['modifier']
                                scale_min = 20.0 #* msg['params']['modifier']
                            else:
                                scale_max = 127
                                scale_min = 0
                            for signal in iterate_rhythm_box_action:
                                if signal['function'] == "square_wave":
                                    if signal['variable_key'] is "duty_cycle":
                                        #signal['duty cycle'] = float(signal['duty_min_max'][0] + (signal['duty_min_max'][1]-signal['duty_min_max'][0])*((msg['params']['value']-scale_min)/(scale_max-scale_min)))
                                        signal['duty cycle'] = float((msg['params']['value']-scale_min*(signal['duty_min_max'][1]-signal['duty_min_max'][0])/scale_max-scale_min)+signal['duty_min_max'][0])
                                    elif signal['variable_key'] is "frequency":
                                        if category[3] != "master_tempo":
                                            signal['frequency'] = float(signal['freq_min_max'][0] + (signal['freq_min_max'][1]-signal['freq_min_max'][0])*((msg['params']['value']-scale_min)/(scale_max-scale_min)))
                                        else:
                                            signal['frequency'] = float((msg['params']['value']/60)*signal['clock_factor'])
                                            print "Frequency = ", signal['frequency']
                                        # signal['frequency'] = float(signal['freq_min_max'][0] + (signal['freq_min_max'][1]-signal['freq_min_max'][0])*((msg['params']['value']-scale_min)/(scale_max-scale_min)))
                                elif signal['function'] == "digital":
                                    if "bool" not in signal:
                                        if msg['params']['value'] < 64:
                                            if "inverse" in signal:
                                                signal['bool'] = 1
                                            else:
                                                signal['bool'] = 0
                                        else:
                                            if "inverse" in signal:
                                                signal['bool'] = 0
                                            else:
                                                signal['bool'] = 1
                                        signal_output.send(signal)
                                        collector.collect(rhythm_box_action[0], "%s" % (signal))
                                        del signal["bool"]
                                        print "sending"
                                        break
                                print "sending out"
                                signal_output.send(signal)
                                collector.collect(rhythm_box_action[0], "%s" % (signal))
                            
            except Exception as e:
                pass
                # traceback.print_exc()
                # print "device: path not found", e
    else:
        import vimina
        def osc_handler(msg):
            pass
        subscribernames = filter(lambda x: os.path.isdir(os.path.join(DEVICES_PATH, x)), os.listdir(DEVICES_PATH))
        subscribernames.append("nervebox2")
        subscribernames.append(HOSTNAME)
        import collectorModule
        collector = collectorModule.Collector()
        collector.start()


    # print "subscribernames ok"
    # print "initializing network..."
    # print 'subscribers: ', subscribernames

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
        osc_handler,
        collector
    )

except Exception as e:
    print e
    #elog.elog.logerror()
