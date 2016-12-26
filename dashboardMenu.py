import os
import sys
import threading
import signalOutputProcess as sop

class Dashboard(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self) 

  def run(self):
    print "Run"
    pass

  def display(self, msg):
    self.msg = msg
    sys.stdout.write("%s"%(self.msg))

  def menu_dashboard(self):
    self.fmap = {
      "s":self.signal_generator,
      "p":self.performance_mode
    }  
    print "** Dashboard Mode **"
    self.display("Select a function:\n")
    self.display("  s - Signal Generator\n")
    self.display("  p - Performance Mode\n")
    input = sys.stdin.readline()
    try:
      self.fmap[input[:-1]]()
    except Exception as e:
      print "menu_dashboard: invalid value:", input

  def signal_generator(self):
    try:
      sop.init()
      self.menu_dashboard()
    except Exception as e:
      print e
      self.menu_dashboard()


  def performance_mode(self):
    pass

dashboard = Dashboard()
dashboard.start()
dashboard.menu_dashboard()
