import sys
import threading

class Collector(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.messages = []
    self.final_list = []
    self.osc_messages = []
    self.final_osc = []

  def run(self):
    pass

  def collect(self,_type, _msg):
    self.msg = _msg
    self.type = _type
    self.messages.append((self.type,self.msg))

  def collect_osc(self, _type, _msg):
    self.msg = _msg
    self.type = _type
    self.osc_messages.append((self.type, self.msg))

  def get(self, _filter):
    self.filter = _filter
    if self.filter == "all":
      for element in self.messages:
        print element
    else:
      self.final_list = [self.t for self.t in self.messages if self.t[0].startswith(self.filter)]
      for element in self.final_list:
        print element
    del self.final_list[:]
    del self.messages[:]

  def get_osc(self, _filter="all"):
    self.filter = _filter
    if self.filter == "all":
      for element in self.osc_messages:
        print element
    else:
      self.final_osc = [self.t for self.t in self.messages if self.t[0].startswith(self.filter)]
      for element in self.final_osc:
        print element
    del self.final_osc[:]
    del self.osc_messages[:]


