import os
import sys
import multiprocessing
import dps
import signalOutputProcess as sop

class Dashboard(multiprocessing.Process):
  def __init__(self):
    multiprocessing.Process.__init__(self) 

  def run(self):
    pass

  def display(self, msg):
    self.msg = msg
    sys.stdout.write("%s"%(self.msg))

  def menu_dashboard(self):
    self.fmap = {
      "s":self.signal_generator,
      "p":self.peroformance_mode
    }  
    self.goodValue = False
    while self.goodValue == False:
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
    except Exception as e:
      print e
      self.menu_dashboard()


  def peroformance_mode(self):
    pass

dashboard = Dashboard()
dashboard.daemon = True
dashboard.start()
dashboard.menu_dashboard()
