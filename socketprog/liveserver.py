# This is a server side socket programming. it
# Opens a socket, binds it to an address (and a
# Port). It Listens for incoming connections.
# Accept connections. Then read and send

import socket
import sys
from thread import *

HOST = '' # sysmbolic name..all interfaces
PORT = 8888 # some unused port

### Open a socket ###
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\nSocket Created "

### Binds a port to it! ###
try:
    mysocket.bind((HOST,PORT))
except socket.error , msg:
    print "Bind failed. Error Code : " + str(msg[0]) + " message " + msg[1]
    sys.exit()
print "Socket Bind Complete! \n"

### Listens for connection ###
mysocket.listen(10) # it will queue ten connections, the 11th will be dropped
print "Socket now Listening ..."

### Accept Connections ###
while 1:
    conn, addr = mysocket.accept()
    # Displays client information
    print "connected with " + addr[0] + ":" + str(addr[1])

    ### Keeping the connection ###
    data = conn.recv(1024)
    reply = 'Ok...' + data
    if not data: break
    conn.sendall(reply)

conn.close()
mysocket.close()

