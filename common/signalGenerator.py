"""

~ to set freq ~

00-mode selector == 0
01-channel_0
02-channel_1
03-channel_2
04-channel_3
05-channel_4
06-osc_reg_00
07-osc_reg_01
08-osc_reg_02
09-osc_reg_03
10-osc_reg_04
11-osc_reg_05
12-osc_reg_06
13-osc_reg_07
14-osc_reg_08
15-osc_reg_09
16-osc_reg_10
17-osc_reg_11
18-osc_reg_12
19-osc_reg_13
20-osc_reg_14
21-osc_reg_15
22-osc_reg_16
23-0

~ to set duty cycle ~

00-mode selector == 1
01-channel_0
02-channel_1
03-channel_2
04-channel_3
05-channel_4
06-pwm_reg_0
07-pwm_reg_1
08-pwm_reg_2
09-pwm_reg_3
10-pwm_reg_4
11-pwm_reg_5
12-pwm_reg_6
13-0
14-0
15-0
16-0
17-0
18-0
19-0
20-0
21-0
22-0
23-0

formats for incoming command : 
    {"function":"square wave", "frequency":<float>, "duty cycle":<float>}
    {"function":"digital", "bool":[True|False]}
    {"function":"pulse, "pulselength":<float>}

"""

import math
import threading
import time
import x24bitParallelPort

FREQ_DIGITAL_DEFAULT = 10000.0 # Hz
FPGA_CLOCK_SPEED_ORIG = 50000000 # Hz
FPGA_CLOCK_DIVISION_FACTOR = 16
MYSTERY_FACTOR = 0.94
FPGA_CLOCK_SPEED_DIVIDED = FPGA_CLOCK_SPEED_ORIG/(FPGA_CLOCK_DIVISION_FACTOR/MYSTERY_FACTOR)  #781250

FREQ_MIN = 1.0 # Hz
FREQ_MAX = 735200.0 # Hz

class Channel(threading.Thread):
    def __init__(self, channel):
        threading.Thread.__init__(self) 
        self.channel = channel
        self.freq = float(FREQ_DIGITAL_DEFAULT)
        self.dutyCycle = 0.0
        self.queue = []
        self.lowFreqSineToggle = False
        self.lowFreqSinePeriod = 0.0
        self.lowFreqSineDutyCycle = 0.0
        self.lowFreqSineActive = False
    def run(self):
        while True:
            if len(self.queue) > 0:
                params = self.queue.pop(0)
                if params["function"] == "pulse":
                    self.pulse(params["pulselength"])
                if params["function"] == "digital":
                    self.digital(params["bool"])
                if params["function"] == "square wave":
                    if params["frequency"] >= 22.5:
                        self.lowFreqSineActive = False
                        self.squareWave(params["frequency"],params["duty cycle"])
                    else:
                        self.lowFreqSineActive = True
                        self.lowFreqSinePeriod = params["frequency"]
                        self.lowFreqSineDutyCycle = params["duty cycle"]
                time.sleep(0.01)
            else:
                if self.lowFreqSineActive:
                    if self.lowFreqSineToggle:
                        self.digital(True)
                        time.sleep(self.lowFreqSinePeriod * (self.lowFreqSineDutyCycle/100))
                    else:
                        self.digital(False)
                        time.sleep(self.lowFreqSinePeriod * ( 1- (self.lowFreqSineDutyCycle/100) ) )
                    self.lowFreqSineToggle = not self.lowFreqSineToggle
                else:
                    time.sleep(0.01)
    def pulse(self,pulselength):
        #self.freq = float(FREQ_DIGITAL_DEFAULT)
        self.dutyCycle = 100.0
        self.sendStateToFPGA(0,1)
        time.sleep(pulselength)
        self.dutyCycle = 0.0
        self.sendStateToFPGA(0,1)
    def digital(self,bool):
        #self.freq = float(FREQ_DIGITAL_DEFAULT)
        self.dutyCycle = 100.0 if bool else 0.0
        self.sendStateToFPGA(0,1)
    def squareWave(self,frequency,dutyCycle):
        if self.dutyCycle != dutyCycle:
            self.dutyCycle = float(dutyCycle)
            self.sendStateToFPGA(0,1)    
        if self.freq != frequency:
            self.freq = float(frequency)
            self.sendStateToFPGA(1,0) 
    def sendStateToFPGA(self, freq_b, ds_b):

        channel_bin_str = '{0:05b}'.format(self.channel)[::-1]
        #print self.channel, channel_bin_str
        if freq_b:
            modeSelector_bin_str = "0"
            osc_bin_str = ('{0:017b}'.format(int(FPGA_CLOCK_SPEED_DIVIDED / self.freq)))[::-1]
            #print self.freq, FPGA_CLOCK_SPEED_DIVIDED / int(osc_bin_str[::-1], 2) 
            x24bitParallelPort.send(list("%s%s%s" % (modeSelector_bin_str, channel_bin_str, osc_bin_str)))
        if ds_b:
            modeSelector_bin_str = "1"
            dutyCycle_bin_str = "000011" if self.dutyCycle > 99 else '{0:06b}'.format(int(max(0,int(self.dutyCycle*0.32)-1)))[::-1]
            padding_bin_str = "000000000000"
            x24bitParallelPort.send(list("%s%s%s%s" % (modeSelector_bin_str, channel_bin_str, dutyCycle_bin_str, padding_bin_str)))
    def enqueue(self, params):
        self.queue.append(params)
    def getState(self):
        return [self.freq, self.dutyCycle]
        
class Channels():
    def __init__(self):
        self.channels_l = [ Channel(x) for x in range(24) ]
        for ch in self.channels_l:
            ch.start()
    def enqueue(self,channel,cmd):

        self.channels_l[channel].enqueue(cmd)
    def getStates(self):
        states = []
        for ch in self.channels_l:
            states.append(ch.getState())
        return states

"""
class LowFreqTimer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fineInterval = 0.0001
        self.courseInterval = 0.001
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
            if lasttime + self.courseInterval < thistime:
                iterations += 1
                total += (thistime - lasttime)
                lasttime = thistime
                for timer in self.timers:
                    if lasttime > timer[2]:
                        timer[2] = lasttime + timer[1]
                        timer[0]() # this function must take no time
            time.sleep(self.fineInterval)
        print repr(total / iterations)

lowfreqtimer = LowFreqTimer()
lowfreqtimer.start()
"""
channels = Channels()
