
#!/usr/bin/env python
import netifaces
import urllib2
import socket


def getLocalIp():
    try:
        return netifaces.ifaddresses("wlan0")[2][0]['addr']
    except Exception as e:
        pass
    try:
        return netifaces.ifaddresses("eth0")[2][0]['addr']
    except Exception as e:
        pass
    return False

def getGlobalIp():
    try:
        return urllib2.urlopen("http://icanhazip.com").read().strip()
    except Exception as e:
        return False

def getHostName():
    try:
        return socket.gethostname()
    except Exception as e:
        return False

def getOnlineStatus():
    r = getGlobalIp()
    return False if r==False else True