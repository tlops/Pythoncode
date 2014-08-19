# This is a server side socket programming. it
# Opens a socket, binds it to an address (and a
# Port). It Listens for incoming connections.
# Accept connections. Then read and send

import socket
import sys

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
mysocket.listen(10) # it will take ten connections, the 11th will be dropped
print "Socket now Listening ..."

### Accept Connections ###
conn, addr = mysocket.accept()
# Displays client information
print "connected with " + addr[0] + ":" + str(addr[1])

### Keeping the connection ###
data = conn.recv(1024)
conn.sendall(data)

conn.close()
mysocket.close()

