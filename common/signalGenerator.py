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
MYSTERY_FACTOR = 0.93
FPGA_CLOCK_SPEED_DIVIDED = FPGA_CLOCK_SPEED_ORIG/(FPGA_CLOCK_DIVISION_FACTOR/MYSTERY_FACTOR)  #781250

FREQ_MIN = 22.50 # Hz
FREQ_MAX = 735200.0 # Hz

class Channel(threading.Thread):
    def __init__(self, channel):
        threading.Thread.__init__(self) 
        self.channel = channel
        self.freq = float(FREQ_DIGITAL_DEFAULT)
        self.dutyCycle = 0.0
        self.queue = []
    def run(self):
        while True:
            if len(self.queue) > 0:
                params = self.queue.pop(0)
                if params["function"] == "pulse":
                    self.pulse(params["pulselength"])
                if params["function"] == "digital":
                    self.digital(params["bool"])
                if params["function"] == "square wave":
                    self.squareWave(params["frequency"],params["duty cycle"])
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
        #if self.freq != frequency and self.dutyCycle != dutyCycle:
        #    self.freq = float(frequency)
        #    self.dutyCycle = float(dutyCycle)
        #    self.sendStateToFPGA(1,1)
        if self.dutyCycle != dutyCycle:
            self.dutyCycle = float(dutyCycle)
            self.sendStateToFPGA(0,1)    
        if self.freq != frequency:
            self.freq = float(frequency)
            self.sendStateToFPGA(1,0) 
    def sendStateToFPGA(self, freq_b, ds_b):

        channel_bin_str = '{0:05b}'.format(self.channel)
        print self.channel, channel_bin_str
        if freq_b:
            modeSelector_bin_str = "0"
            osc_bin_str = ('{0:017b}'.format(int(FPGA_CLOCK_SPEED_DIVIDED / self.freq)))[::-1]

            print self.freq, FPGA_CLOCK_SPEED_DIVIDED / int(osc_bin_str, 2)  
            print self.freq, FPGA_CLOCK_SPEED_DIVIDED / int(osc_bin_str[::-1], 2) 
            # print"--->",FPGA_CLOCK_SPEED_DIVIDED,self.freq,osc_bin_str
            #osc_bin_str = '{0:017b}'.format(int(FPGA_CLOCK_SPEED_DIVIDED / self.freq))

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

channels = Channels()

"""
FREQ_MIN = 110.0 # Hz
FREQ_MAX = 30007.0 # Hz
FREQ_DIGITAL_DEFAULT = 10000 # Hz

class Channel(threading.Thread):
    def __init__(self, channel):
        threading.Thread.__init__(self) 
        self.channel = channel
        self.decicents = 0
        self.freq = float(FREQ_MIN)
        self.queue = []
        self.pwm = 0.0
        self.setFreq(self.freq)
        self.setPwm(self.pwm)
    def formatCommand(self,command):  # command = [pwm|freq]
        channel_bin_str = '{0:05b}'.format(self.channel)
        if command=="cents":
            command_bin_str = "0"
            #slices = int(FREQ_MAX/self.freq)
            #adjustedFreq_f = float(FREQ_MAX/slices)
            decicentId = '{0:018b}'.format(self.decicents)
            #print "formatCommand decicent=", self.decicents, decicentId
            return list(channel_bin_str + command_bin_str + decicentId)

        if command=="pwm":
            command_bin_str = "1"
            pwm_bin_str = '{0:018b}'.format(max(0,int(self.pwm*10.24)-1))
            return list(channel_bin_str + command_bin_str + pwm_bin_str)  
    def setFreq(self, freq): # Hz
        if FREQ_MIN <= float(freq) and float(freq) <= FREQ_MAX:
            self.freq = freq
            self.decicents = self.freqToCents()
            command_l = self.formatCommand("cents")
            #print "Channel %d frequency %f adjusted to %f" % (self.channel, freq, adjustedFreq)
            x24bitParallelPort.send(command_l)
        else:
            print "Freqency out of range (0Hz-262,144Hz)", freq
    def freqToCents(self):
        create number for each 0.1 cent of pitch corresponding to freq, starting at 0.21484375 Hz
        decicents = int(1200* math.log((self.freq/FREQ_MIN),2))
        freq_adjusted = FREQ_MIN * math.pow(2.0,(decicents/1200.0))
        #print "frequency quantized to", freq_adjusted
        return decicents
    def setPwm(self, pwm_f): # float%
        if 0.0 <= pwm_f <= 100.0:
            self.pwm = pwm_f
            command_l = self.formatCommand("pwm")
            x24bitParallelPort.send(command_l)
        else:
            print "PWM out of range (0.0-100.0)", pwm_f
    def squareWave(self, freq, pwm):
        self.setFreq(freq)
        self.setPwm(pwm)
    def digital(self, bool):
        self.setFreq(FREQ_DIGITAL_DEFAULT)
        self.setPwm(0.0 if bool==0 else 100.0)
    def pulse(self, pulselength):
        self.digital(1)
        time.sleep(pulselength)
        self.digital(0)
    def get(self):
        return {
            "channel":self.channel,
            "freq":self.freq,
            "pwm":self.pwm
        }
    def run(self):
        while True:
            if len(self.queue) > 0:
                params = self.queue.pop(0)
                if params["function"] == "pulse":
                    self.pulse(params["pulselength"])
                if params["function"] == "digital":
                    self.digital(params["bool"])
                if params["function"] == "square wave":
                    self.squareWave(params["frequency"],params["duty cycle"])
            time.sleep(0.01)
    
    def enqueue(self, params):
        self.queue.append(params)
    def getState(self):
        return [self.freq, self.pwm]

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

channels = Channels()


    incoming_channel_reg[0] <= parallel_in[22];
    incoming_channel_reg[1] <= parallel_in[21];
    incoming_channel_reg[2] <= parallel_in[20];
    incoming_channel_reg[3] <= parallel_in[19];
    incoming_channel_reg[4] <= parallel_in[18];
    incoming_pwm_reg[0] <= parallel_in[17];
    incoming_pwm_reg[1] <= parallel_in[16];
    incoming_pwm_reg[2] <= parallel_in[15];
    incoming_pwm_reg[3] <= parallel_in[14];
    incoming_pwm_reg[4] <= parallel_in[13];
    incoming_pwm_reg[5] <= parallel_in[12];
    incoming_pwm_reg[6] <= parallel_in[11];
    incoming_osc_reg[0] <= parallel_in[10];
    incoming_osc_reg[1] <= parallel_in[9];
    incoming_osc_reg[2] <= parallel_in[8];
    incoming_osc_reg[3] <= parallel_in[7];
    incoming_osc_reg[4] <= parallel_in[6];
    incoming_osc_reg[5] <= parallel_in[5];
    incoming_osc_reg[6] <= parallel_in[4];
    incoming_osc_reg[7] <= parallel_in[3];
    incoming_osc_reg[8] <= parallel_in[2];
    incoming_osc_reg[9] <= parallel_in[1];
    incoming_osc_reg[10] <= parallel_in[0];


    incoming_osc_reg[11] <= parallel_in[22];
    incoming_osc_reg[12] <= parallel_in[21];
    incoming_osc_reg[13] <= parallel_in[20];
    incoming_osc_reg[14] <= parallel_in[19];
    incoming_osc_reg[15] <= parallel_in[18];
    incoming_osc_reg[16] <= parallel_in[17];


intermojo protocol
    00: channel
    01: channel
    02: channel
    03: channel
    04: channel
    05: command [pwm/freq]
    06: data 0
    07: data 1
    08: data 2
    09: data 3
    10: data 4
    11: data 5
    12: data 6
    13: data 7
    14: data 8
    15: data 9
    16: data 10
    17: data 11
    18: data 12 
    19: data 13
    20: data 14
    21: data 15
    22: data 16
    23: data 17

input functions:
    hz (channel, freq in Hz as float between 1 and )
    pitch (channel, octave, pitch, cents)
    pwm (channel, duty cycle as float between 0.0 and 100.0)
    pulse (channel, duration in seconds)
    digital (channel, 0 or 1)

    set (channel, freq, pwm)

    get ()

internal:
    init all channels
        default freq = ?
        default pwm = 0

0.000007629 s

18 data bits = 262144
minimum time slice = 1 sec/ 262144 = 0.000003815 sec or 3.815 x 10^-6

50,000,000 FPGA clock cycles * 0.000003815 = 190.75 clock cycles

"""