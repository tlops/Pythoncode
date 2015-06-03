###################################################################
####################### CHAT-SERVER- ##############################
##                                                               ##
## This is a live chat server module. The server accept multiple ##
## incoming connections from clients. Read incoming messages     ##
## from each client and broadcast them to all othe connected cl- ##
## ents. It uses port 1982 to listen for connections. the clien- ##
## ts must connect to the server on this port.                   ##
##                                                               ##
## The client uses telnet to connect.                            ##
##                                                               ###################
## http://www.binarytides.com/code-chat-application-server-client-sockets-python/ ##
####################################################################################

import socket, select

# Function to broadcast chat message to all connected clients
def broadcast_msg (sock, message):
    #Do not send message to master socket and the client tha sent mesage
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                #Broken socket connection: E.g. client pressed CTRL^ C
                socket.close()
                CONNECTION_LIST.remove(socket)

if __name__ =="__main__":
    #List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 1982  # The port to use
    HOST = ""    # All interface/ address = 0.0.0.0

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    server_socket.bind((HOST, PORT)) # Binding the port and IPaddr
    server_socket.listen(10) # Socket listening for connections

    # Add server socket to the list of readable connections.
    CONNECTION_LIST.append(server_socket)
    print "Chat server started on port: " + str(PORT) # Opening Msg

    while 1:
        #Get the list of socket that are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST, [], [])
        for sock in read_sockets:
            #New connections
            if sock == server_socket:
                # Handle the case of new connection received
                sockfd, addr =server_socket.accept() # accpets new connection
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected " % addr
                broadcast_data(sockfd, "[%s : %s] entered the room:\n" % addr
            # Managing incoming messages and conections
            else :
            #Data recieved from a client, process it
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)

                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr
                    print "Client (%s,%s) is offline: " %addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()

