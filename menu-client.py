import os
import sys
import subprocess

BASE_PATH = "%s/%s" % os.path.split(os.path.dirname(os.path.realpath(__file__)))
COMMON_PATH = "%s/common/" % (BASE_PATH )
sys.path.append(COMMON_PATH)

import signalOutputProcess as sop

def display(msg):
  sys.stdout.write("%s"%(msg))

def first_choice():
  answers = ["Performance", "Signal Generator"]
  while True:
    display("Select a mode (Performance - Signal Generator):")
    input_raw = sys.stdin.readline()
    try:
      input_string = input_raw[:-1]
      if input_string in answers:
        if input_string == "Performance":
          performance_mode()
        else:
          signal_generator()
    except Exception as e:
      print "menuChannel:please enter a number between 0 and 23:"

def performance_mode():
  print "Executing performance"
  try:
    subprocess.call(['./main.py', "-client"])
  except Exception as e:
    print e

def signal_generator():
  sop.init()

if __name__ == '__main__':
  first_choice()