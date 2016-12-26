import sys
import threading
import signalOutputProcess as sop

class Dashboard(threading.Thread):
  def __init__(self, collect):
    threading.Thread.__init__(self) 
    self.collector = collect

  def run(self):
    self.menu_dashboard()

  def display(self, msg):
    self.msg = msg
    sys.stdout.write("%s"%(self.msg))

  def menu_dashboard(self):
    self.fmap = {
      "s":self.signal_generator,
      "p":self.performance_mode
    }
    while True:  
      print "** Dashboard Mode **"
      self.display("Select a function:\n")
      self.display("  s - Signal Generator\n")
      self.display("  p - Performance Mode\n")
      self.input = sys.stdin.readline()
      try:
        self.fmap[self.input[:-1]]()
      except Exception as e:
        print "menu_dashboard: invalid value:", self.input

  def signal_generator(self):
    try:
      sop.init()
      self.menu_dashboard()
    except Exception as e:
      print e
      self.menu_dashboard()


  def performance_mode(self):
    self.collector.get("network")


