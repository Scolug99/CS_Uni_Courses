# Disclaimer: This is quick and dirty code used to demonstrate how to code rapidly, not how to code beautifully.

import socket

localIP     = "127.0.0.1" # 127.0.0.1 is a "loopback" IP, to talk to yourself.
localPort   = 5678 # Which port does the server listen on?
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind the socket so that the server listens at the intended IP address and port
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening on port", localPort)

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = message.decode()
    clientIP  = "Client IP Address:{}".format(address)
    
    print("Received: ", clientMsg)
	
    # Sending a reply to client
    response = "Ok!"
    UDPServerSocket.sendto(str.encode(response), address)