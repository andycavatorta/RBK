# one tight loop and multiple schedulers

import threading
import time

TIMER_INTERVAL = 0.00001

class Timer(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.timers = []

  def register(self,ref,ms):
    self.timers.append([ref,ms,time.time()])

  def unregister(self, ref):
    for timer in self.timers:
        if timer[0] == ref:
            self.timers.remove(timer)

  def run(self):
    lasttime = time.time()
    iterations = 0
    total = 0.0
    while True:
        thistime = time.time()
        if lasttime + 0.001 < thistime:
            iterations += 1
            total += (thistime - lasttime)
            lasttime = thistime
            for timer in self.timers:
                if lasttime > timer[2]:
                    timer[2] = lasttime + timer[1]
                    timer[0]() # this function must take no time
        time.sleep(TIMER_INTERVAL)
    print repr(total / iterations)
timer = Timer()
timer.start()

#def setOscillator(hz, channel):





"""
# test

lt1 = 0
lt2 = 0
lt3 = 0

def testOutput1():
    global lt1
    t = time.time()
    print "1", t - lt1
    lt1 = t
def testOutput2():
    global lt2
    t = time.time()
    print "2", t - lt2
    lt2 = t
def testOutput3():
    global lt3
    t = time.time()
    print "3", t - lt3
    lt3 = t

timer.register(testOutput1, 1.0)
timer.register(testOutput2, 0.1)
timer.register(testOutput3, 0.01)

time.sleep(3)
timer.unregister(testOutput3)
"""