import socket
#from socket import *

# server host name
server_host = '127.0.0.1'

# server running port number
server_port = 5000

# Creation of server socket
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind the provided host address and port number to server socket
serverSocket.bind((server_host, server_port))

# Listen for the client request for connection, 1 represents at a time only one client can connect
serverSocket.listen(1)

# Accept the request and store client address
clientAdded, clientAddress = serverSocket.accept()

# you can print the client address if you want , by using
print("Connection recieved from: ",str(clientAddress))

# Recieve the message sent by client
msg = clientAdded.recv(1024)

# While loop so that message is recieved continuously
while msg:
    i = 0
    while i < 2:
        # Decode the msg to variable
        received_message = msg.decode()

        # Calculate the count of characters received
        char_count = len(received_message)

        # print the message at SERVER side terminal
        print('Received From Client:' ,received_message)

        # Send the char count , by encoding it
        #message_to_send = str(char_count)
        message_to_send = received_message + ", What is your name?"
        clientAdded.send(message_to_send.encode())

        # Send the upper case message by encoding it
        message_to_send = received_message.upper()
        clientAdded.send(message_to_send.encode())

        # Check if the any message is recieved and continue the loop
        msg = clientAdded.recv(1024)
        i += 10

# Decode the msg to variable
    received_message = msg.decode()

        # Calculate the count of characters received
    #char_count = len(received_message)

        # print the message at SERVER side terminal
    print('Received From Client:' ,received_message)

        # Send the char count , by encoding it
        #message_to_send = str(char_count)
    message_to_send = "Hello " + received_message + ", Welcome to SIT202!"
    clientAdded.send(message_to_send.encode())

        # Send the upper case message by encoding it
    message_to_send = received_message.upper()
    clientAdded.send(message_to_send.encode())

        # Check if the any message is recieved and continue the loop
    msg = clientAdded.recv(1024)


# Disconnect the client
clientAdded.close()
