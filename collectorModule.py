import sys
import threading

class Collector(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.messages = []
    self.final_list = []

  def run(self):
    pass

  def collect(self,_type, _msg):
    self.msg = _msg
    self.type = _type
    self.messages.append((self.type,self.msg)) 

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


