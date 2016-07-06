#############################################
##### MODULES, EVENIRONMENT AND GLOBALS #####
#############################################

import os
#import time
import sys
import traceback

BASE_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
COMMON_PATH = "%s/common/" % (BASE_PATH )
DEVICES_PATH = "%s/client/devices/" % (BASE_PATH )
SERVER_PATH = "%s/server/" % (BASE_PATH )
STORE_PATH = "%s/store/" % SERVER_PATH

# local paths
sys.path.append(BASE_PATH)
sys.path.append(COMMON_PATH)
sys.path.append(SERVER_PATH)

import signalGenerator

CRLF = "\n"

def display(msg):
  sys.stdout.write("%s"%(msg))

def menuChannel():
  while True:
    params = {}
    display("Select a channel (0-23):")
    input_raw = sys.stdin.readline()
    try:
      input_int = int(input_raw[:-1])
      if 0<= input_int <=23:
        params["channel"] = input_int
        menuFunction(params)
        #print ">>> params=",params
    except Exception as e:
      print "menuChannel:please enter a number between 0 and 23:"

def menuFunction(params):
  fmap = {
    "s":menuSquareWave,
    "d":menuDigital,
    "p":menuPulse,
    "v":menuValues
  }  
  goodValue = False
  while goodValue == False:
    display("Select a function:\n")
    display("  s - Square Wave\n")
    display("  d - Digital (on/off)\n")
    display("  p - Pulse \n")
    display("  v - Channel Values \n")
    input = sys.stdin.readline()
    try:
      fmap[input[:-1]](params)
      goodValue = True
    except Exception as e:
      print "menuFunction: invalid value:", input
      print traceback.print_exc()

def menuSquareWave(params):
  params["function"] = "square wave"
  menuFreq(params)
  menuPWM(params)
  #signalGenerator.channels.enqueue(params["channel"],{"function":params["function"],"":params[""]})
  signalGenerator.channels.enqueue(params["channel"],{"function":params["function"],"frequency":params["frequency"],"duty cycle":params["duty cycle"]})
  #signalGenerator.channels.channels_l[params["channel"]].squareWave(params["frequency"],params["duty cycle"])

def menuDigital(params):
  params["function"] = "digital"
  goodValue = False
  while goodValue == False:
    display("Enter an on/off value (0 or 1):")
    input_raw = sys.stdin.readline()
    try:
      input_int = int(input_raw[:-1])
      if input_int in (0,1):
        signalGenerator.channels.enqueue(params["channel"],{"function":params["function"],"bool":input_int})
        #signalGenerator.channels.channels_l[params["channel"]].digital(input_int)
        goodValue = True
    except Exception as e:
      print "menuDigital:invalid value:", input
      print traceback.print_exc()
  return 

def menuPulse(params):
  params["function"] = "pulse"
  goodValue = False
  while goodValue == False:
    display("Enter a pulse length in seconds (precise to two decimal places):")
    input_raw = sys.stdin.readline()
    try:
      input_f = float(input_raw[:-1])
      if 0.0 <= input_f:
        #signalGenerator.channels.channels_l[params["channel"]].pulse(input_f)
        signalGenerator.channels.enqueue(params["channel"],{"function":params["function"],"pulselength":input_f})
        goodValue = True
    except Exception as e:
      print "menuPulse:invalid value:", input
      print traceback.print_exc()
  return 

def menuValues(params):
  states = signalGenerator.channels.getStates()
  for i in range(len(states)):
    print "ch:", i, states[i][0],"Hz,", states[i][1], "%"
  #print states

def menuFreq(params):
  goodValue = False
  while goodValue == False:
    display("Enter a frequency in Hz (%f-%f):" % (signalGenerator.FREQ_MIN,signalGenerator.FREQ_MAX))
    input_raw = sys.stdin.readline()
    try:
      input_f = float(input_raw[:-1])
      if signalGenerator.FREQ_MIN <= input_f <= signalGenerator.FREQ_MAX:
        params["frequency"] = input_f
        goodValue = True
        osc_bin_str = ('{0:017b}'.format(int(signalGenerator.FPGA_CLOCK_SPEED_DIVIDED / input_f)))[::-1]
        print input_f, "Hz rounded to", signalGenerator.FPGA_CLOCK_SPEED_DIVIDED / int(osc_bin_str[::-1], 2), "Hz"

    except Exception as e:
      print "menuFreq:invalid value:", input
      print traceback.print_exc()
  return 
  
def menuPWM(params):
  goodValue = False
  while goodValue == False:
    display("Enter a duty cycle value (0.0-100.0):")
    input_raw = sys.stdin.readline()
    try:
      input_f = float(input_raw[:-1])
      if 0.0 <= input_f <= 100.0:
        params["duty cycle"] = input_f
        goodValue = True
    except Exception as e:
      print "menuPWM:invalid value:", input
  return 

menuChannel()
