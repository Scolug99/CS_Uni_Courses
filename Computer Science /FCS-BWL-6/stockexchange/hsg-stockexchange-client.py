# Disclaimer: This is quick and dirty code used to demonstrate how to code rapidly, not how to code beautifully.

import socket

serverAddressPort   = ("127.0.0.1", 5678) # You'll need to enter the correct IP here 
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    msg = input('> ')
    
    if msg == "BYE":
        break;
    
    bytesToSend = str.encode(msg)
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    
    # Receive response from server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    
    msg = msgFromServer[0].decode()
    print(msg)