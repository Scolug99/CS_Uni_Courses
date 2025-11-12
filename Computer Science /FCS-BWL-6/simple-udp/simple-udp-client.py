# Disclaimer: This is quick and dirty code used to demonstrate how to code rapidly, not how to code beautifully.

import socket

serverAddressPort   = ("127.0.0.1", 5678)  # 127.0.0.1 is a "loopback" IP, to talk to yourself.
bufferSize          = 1024

# Create a UDP socket at the client side to talk to the server at the above address and port
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    msg = input('> ')
    
    # Stop if user enters "BYE"
    if msg == "BYE":
        break;
    
    # Encode message to get the bytes (i.e., 8-bit chunks) to send
    bytesToSend = str.encode(msg)
    
    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    
    # Wait for response from server, and receive it
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    
    # Decode and print server response
    msg = msgFromServer[0].decode()
    print(msg)