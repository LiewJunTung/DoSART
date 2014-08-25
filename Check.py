__author__ = 'Liew'

# import httplib
import requests
#import socket

status = ""
server = ""

# def checkUpOrDown(IP):
#     global status
#     try:
#         conn = httplib.HTTPConnection(IP, timeout=1)
#         conn.request("HEAD", "/")
#         r1 = conn.getresponse()
#         status = r1.reason
#         return status
#     except socket.error:
#         status = "timeout"
#         return status

def checkUpOrDown(IP):
    global status
    try:
        checkOS(IP)
        IP = "http://" + IP
        conn = requests.get(IP, timeout=1)
        if conn.status_code == 200:
            status = "OK"
        return status
    except conn.error:
        status = "timeout"
        return status

def checkOS(IP):
    global server

    IP = "http://" + IP
    conn = requests.get(IP, timeout=1)
    server = conn.headers['server']
    if "Ubuntu" in server:
        server = "Ubuntu Server"
    if "Microsoft-IIS/8.0" in server:
        server = "Windows"
    return server



# def close_if_time_pass(seconds):
#     global status
#     """
#     Threading function, after N seconds print something and exit program
#     """
#     time.sleep(seconds)
#     if status == "":
#         return "OK"
#     else:
#         return "Launch FAILED"

def main(ip="192.168.56.102"):
    # define close_if_time_pass as a threading function, 5 as an argument
    # t = threading.Thread(target=close_if_time_pass,args=(2,))
    # start threading
    # t.start()
    # ask him his name
    return checkUpOrDown(ip)