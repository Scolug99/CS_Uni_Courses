import socket
from datetime import datetime

UDP_PORT = 5678
LOCAL_IP = "127.0.0.1" # loopback address

highscoresFile = open("food-and-walls-highscores.txt","a")

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((LOCAL_IP, UDP_PORT))
print("UDP server up and listening for incoming highscores on port", UDP_PORT)

# Listen for incoming datagrams
bufferSize = 1024
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

	# Example clientMsg = "Score simon 110"
    clientMsg = message.decode()
     
    print(clientMsg)
    
    clientMsgParts = clientMsg.split()
    # clientMsgParts[0] = "Score"
    # clientMsgParts[1] = "simon"
    # clientMsgParts[2] = "110"
    
    if clientMsgParts[0] == "Score":
        playerName = clientMsgParts[1]
        playerScore = clientMsgParts[2]
		
		# Write to highscores file: Current time, player name, player score
        highscoresFile.write(str(datetime.now()) + "," + playerName + "," + playerScore + "\n")
        highscoresFile.flush()