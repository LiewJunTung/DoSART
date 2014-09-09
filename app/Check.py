__author__ = 'Liew'

import requests

status = ""
server_os = ""

def checkUpOrDown(IP, TO=0.025):
    global status
    try:
        checkOS(IP)
        IP = "http://" + IP
        conn = requests.get(IP, timeout=TO)
        if conn.status_code == 200:
            status = "OK"
        return status
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        status = "timeout"
        return status

def checkOS(IP):
    global server_os

    IP = "http://" + IP
    conn = requests.get(IP, timeout=1)
    server_os = conn.headers['server']
    if "Ubuntu" in server_os:
        server_os = "Ubuntu"
    if "Microsoft-IIS/8.0" in server_os:
        server_os = "Windows"
    return server_os


def main(ip="192.168.56.102", TO=0.025):
    return checkUpOrDown(ip, TO)
