# Disclaimer: This is quick and dirty code used to demonstrate how to code rapidly, not how to code beautifully.

import socket

localIP     = "127.0.0.1" # You'll need to enter the correct IP here
localPort   = 5678
bufferSize  = 1024

class Stock:
    
    def __init__(self, ticker, init_price):
        self.ticker = ticker
        self.price = init_price
        self.orders_bid = []
        self.orders_ask = []
        
    def buy(self, price):
        print("Buying", self.ticker, "for", price)
        
        matched = False
        for quote in self.orders_ask:
            if quote <= price:
                print("Executed!")
                self.orders_ask.remove(quote)
                self.price = price
                matched = True
                break
        
        if not matched:
            self.orders_bid.append(price)
            self.orders_bid.sort(reverse=True)
        
        print("Bids:", self.orders_bid)
        print("Asks:", self.orders_ask)
        
    def sell(self, price):
        print("Selling", self.ticker, "for", price)
        matched = False
        for quote in self.orders_bid:
            if quote >= price:
                print("Executed!")
                self.orders_bid.remove(quote)
                self.price = price
                matched = True
                break
        if not matched:
            self.orders_ask.append(price)
            self.orders_ask.sort()
        
        print("Bids:", self.orders_bid)
        print("Asks:", self.orders_ask)
    	
def processClientMessage(clientMessage):
    try:
        if clientMessage == "LIST":
            print("Preparing Listing")
			
            response = "\n--------------\n"
            for ticker in STOCKS.keys():
                response = response + ticker + " ---- " + str(STOCKS[ticker].price) + " CHF\n"
            response = response + "-------------\n"
            return response
        else:
			# BUY/SELL TICKER PRICE -> [BUY/SELL TICKER PRICE]
            message_parts = clientMessage.split()
            
            order_type = message_parts[0]
            
            if order_type == "BUY":
                ticker_symbol = message_parts[1]
                if not ticker_symbol in STOCKS.keys():
                    return "This stock does not exist."
                else:
                    order_price = int(message_parts[2])
                    print("Received BUY Order: ", ticker_symbol, order_price)
                    STOCKS[ticker_symbol].buy(order_price)
                    return "OK"
                    
            elif order_type == "SELL":
                ticker_symbol = message_parts[1]
                if not ticker_symbol in STOCKS.keys():
                    return "This stock does not exist."
                else:
                    order_price = int(message_parts[2])
                    print("Received SELL Order: ", ticker_symbol, order_price)
                    STOCKS[ticker_symbol].sell(order_price)
                    return "OK"
            
            else:
                return "Invalid Command"
    except:
        return "Invalid Command"

# Init stocks
STOCKS = {}
STOCKS["LVMH"] = Stock("LVMH", 100)
STOCKS["TSLA"] = Stock("TSLA", 80)
STOCKS["BMW"] = Stock("BMW", 50)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
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
	# Determine what should be done with the client message, and process it
    response = processClientMessage(clientMsg)
    
    # Sending a reply to client
    UDPServerSocket.sendto(str.encode(response), address)