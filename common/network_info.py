
#!/usr/bin/env python
import netifaces
import urllib2
import socket

interfaces = netifaces.interfaces()

def getLocalIp():
    for interface in interfaces:
        try:
            test = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['broadcast']
        except Exception as e:
            print 'broadcast not available...'
        else:
            print 'found connection returning ip: %s' % (netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr'])
            return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

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