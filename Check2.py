import socket

real_create_conn = socket.create_connection

def set_src_addr(*args):
    address, timeout = args[0], args[1]
    source_address = ('192.168.56.103', 0)
    return real_create_conn(address, timeout, source_address)

socket.create_connection = set_src_addr

import requests
r = requests.get('http://192.168.56.102')
print r.content