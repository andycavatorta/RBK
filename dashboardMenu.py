import sys
import threading
import signalOutputProcess as sop

#OIDOSADA

class Dashboard(threading.Thread):
  def __init__(self, collect):
    threading.Thread.__init__(self) 
    self.collector = collect
    self.break_value = None

  def run(self):
    self.menu_dashboard()

  def display(self, msg):
    self.msg = msg
    sys.stdout.write("%s"%(self.msg))

  def menu_dashboard(self):
    self.fmap = {
      "s":self.signal_generator,
      "p":self.performance_mode,
      "o":self.raw_osc,
      "l":self.live_mode
    }
    self.goodValue = False
    while True: 
      print "********************" 
      print "** Dashboard Mode **"
      print "********************\n"
      self.display("Select a function:\n")
      self.display("  s - Signal Generator\n")
      self.display("  p - Performance Mode\n")
      self.display("  o - Raw Osc Msgs\n")
      self.display("  l - Live Mode\n")
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
      self.display("Filter by: network, MIDI, signal, all:\n")
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
      # self.display("Filter by osc:\n")
      # self.input_raw = sys.stdin.readline()
      try:
        # self.input_f = self.input_raw[:-1]
        self.collector.get_osc()
        self.goodValue = True

      except Exception as e:
        print "raw_osc:invalid value:", input
    return

  def key_poll(self):
    self.input_raw = sys.stdin.readline()
    self.input_f = self.input_raw[:-1]
    self.break_value = self.input_f

  def live_mode(self):
    self.goodValue = False
    self.break_value = None
    self.display("Filter by: network, MIDI, signal, all\n")
    self.display("Type '?' and hit Enter anytime to exit:\n")
    self.input_raw = sys.stdin.readline()
    self.key = threading.Thread(target=self.key_poll)
    self.key.start()
    while self.goodValue == False:
      try:
        self.input_f = self.input_raw[:-1]
        self.collector.get(self.input_f)
        if self.break_value == '?':
          self.key.join()
          self.collector.clear_all()
          self.goodValue = True
      except Exception as e:
        print "live_mode:invalid value:", input
    return


