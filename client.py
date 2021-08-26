import socket
#from socket import *

server_host = '127.0.0.1'
server_port = 5000

# Creation of client socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Binding of client socket to the server address and connection
clientSocket.connect((server_host, server_port))

# Temp variable to be used for sending 10
i = 0

# This program can send 10 messages and would be receiving the reply for the same
while i<1:
    # Take the input from the user for the message to be sent
    msg = input("\nEnter the message: ")

    # Encode the message and send it to the SERVER
    clientSocket.send(msg.encode())

    # Recieve the Character Count from the SERVER
    message_recieved = clientSocket.recv(1024)

    # Print the Char count received after decoding
    #print('Char Count: ',message_recieved.decode())

    # Recieve the message recieved in upper case
    message_recieved = clientSocket.recv(1024)


    # Increment the temp counter
    i+=1

msg = input("\nEnter your name: ")

    # Encode the message and send it to the SERVER
clientSocket.send(msg.encode())

    # Recieve the Character Count from the SERVER
message_recieved = clientSocket.recv(1024)

    # Print the Char count received after decoding
print('Greeting: ',message_recieved.decode())

    # Recieve the message recieved in upper case
message_recieved = clientSocket.recv(1024)



# Disconnect the client Socket
clientSocket.close()
