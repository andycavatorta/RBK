import time
import netifaces as ni
import commands
import multiprocessing

class Bip(multiprocessing.Process):
	def __init__(self):
		multiprocessing.Process.__init__(self) 

	def _ledonoff(self,interval, rep):	
		for x in range(rep):
			commands.getstatusoutput('echo 1 >/sys/class/leds/led0/brightness')
			time.sleep(interval) 
			commands.getstatusoutput('echo 0 >/sys/class/leds/led0/brightness')
			time.sleep(interval)
	def _blinkNumber(self,character):
		character = self.ipAddress[character]
		if character == '.':
			self._ledonoff(0.2,5)
		else:
			self._ledonoff(0.5,character)
		time.sleep(1.8)
	def _startStop(self):
		self._ledonoff(0.1,20)

	def _castInt(self,x):
			if self.ipAddress[x] != '.':
				self.ipAddress[x] = int(self.ipAddress[x])
			else:
				self.ipAddress[x] = self.ipAddress[x]

	def _init(self):
		if commands.getoutput('cat /sys/class/net/eth0/carrier') == '1':
			interfaceName = "eth0"
		elif commands.getoutput('cat /sys/class/net/wlan0/carrier') == '1':
			interfaceName = "wlan0"
		else:
			print "Not connected"
			self._ledonoff(0.1, 30)
		try:
			self.ipAddress = ni.ifaddresses(interfaceName)[ni.AF_INET][0]['addr']
			self.ipAddress = list(self.ipAddress)
			print len(self.ipAddress)
			map(self._castInt, range(len(self.ipAddress)))
		except Exception as e:
			print e

	def run(self):
		self._init()
		print 'starting blink ip...'
		self._startStop()
		time.sleep(2)
		map(self._blinkNumber, range(len(self.ipAddress)))
		time.sleep(2)
		self._startStop()

p = Bip()
p.daemon = True
p.start()