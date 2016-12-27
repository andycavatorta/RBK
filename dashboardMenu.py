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
      "p":self.performance_mode,
      "o":self.raw_osc
    }
    self.goodValue = False
    while True:  
      print "** Dashboard Mode **"
      self.display("Select a function:\n")
      self.display("  s - Signal Generator\n")
      self.display("  p - Performance Mode\n")
      self.display("  o - Raw Osc Msgs\n")
      self.input = sys.stdin.readline()
      try:
        self.fmap[self.input[:-1]]()
        self.goodValue = True
      except Exception as e:
        print "menu_dashboard: invalid value:", self.input

  def signal_generator(self):
    self.goodValue = False
    while self.goodValue == False:
      try:
        sop.init()
        self.goodValue = True
      except Exception as e:
        print e
        self.goodValue = True

  def performance_mode(self):
    self.goodValue = False
    while self.goodValue == False:
      self.display("Filter by: network, MIDI, pulse, square_wave, digital, all:\n")
      self.input_raw = sys.stdin.readline()
      try:
        self.input_f = self.input_raw[:-1]
        self.collector.get(self.input_f)
        self.goodValue = True
      except Exception as e:
        print "performance_mode:invalid value:", input
    return

    def raw_osc(self):
      self.goodValue = False
      while self.goodValue == False:
        self.display("Filter by: network, MIDI, pulse, square_wave, digital, all - '?' to exit:\n")
        self.input_raw = sys.stdin.readline()
        try:
          self.input_f = self.input_raw[:-1]
          self.collector.get_osc(self.input_f)
          self.goodValue = True
        except Exception as e:
          print "performance_mode:invalid value:", input
      return 


