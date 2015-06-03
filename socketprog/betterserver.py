# This is a server side socket programming. it
# Opens a socket, binds it to an address (and a
# Port). It Listens for incoming connections.
# Accept connections. Then read and send
# This uses thread to handle multiple connections
# between the server and the clients

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

### Function to handle multiple Connections ###
def clientthread(conn):
    # send message to connected client
    conn.send("Welcome to the Server. Type something and hit ENTER! ")
    # infinite loop so that the function do no terminate and thread do not end
    while True:
        #Recieving msg from client
        data = conn.recv(1024)
        reply = 'OK...'  + data
        if not data: break
        if data =='quit': break
        conn.sendall(reply)
    #coming out of the loop
    conn.close()

# Keep talking with the client
while 1:
    # wait to accept a connection -blocking call
    conn, addr = mysocket.accept()
    # Displays client information
    print "connected with " + addr[0] + ":" + str(addr[1])
    # start_new_thread takes 1st argument as a function name 2nd arg is a tupple
    start_new_thread(clientthread, (conn,))

mysocket.close()

