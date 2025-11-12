Dear Students,

in the sessions on Wednesday and Friday, I showed several demonstrations. Here is a brief guide through these demos (and some that I wasn't able to show), so you can try this at home as well!

Have fun!
Simon


----


# Demo 1: Network Infrastructure Exploration

In this demo, we explored our machine's network environment and traced the network routes to a few remote servers.

- Open your Terminal / Console

- Find Information about network interfaces your machine is connected to
--- arp -a - to use the Address Resolution Protocol, see Lecture on Data Link Layer)
--- ipconfig -all (Unix: ifconfig -all) - to display information about your computer's network connections

- Pick one of the interfaces and find its [IP-Address]

- Test whether that interface responds to communication
--- ping [IP-Address]

- Check that this interface is only one network hop away from your machine
--- tracert [IP-Address] (Unix: traceroute [IP-Address])

- Trace the network hops to some other network interfaces, where traceroute resolves hostnames to IP addresses by itself
--- tracert google.com
--- tracert sri.com

- We also looked at my machine's routing table
--- route print



# Demo 2: DNS and a Conversation with a Web Server

In this demo, we used the DNS to find the IP of a remote host and then used telnet to connect to that remote host, send an HTTP request, and see the HTTP response.

- We attempted to contact the host example.org; first, we resolved its IP address via DNS
--- nslookup example.org
--- As a response, we learned the IPv4 address of the remote host (93.184.216.34) as well as its IPv6 address (2606:2800:220:1:248:1893:25c8:1946)

- Next, we established a TCP connection to any HTTP server that might run on that host, by connecting using its IP and the default port of the HTTP protocol, i.e. port 80
--- telnet 93.184.216.35 80 (on Windows, you might need to install or enable telnet)
--- Note: All characters typed into the socket that telnet opens are directly sent to the remote server and thus not displayed locally. To see what we typed, we activated telnet's "localecho" function. To do that, we opened the TCP connection, then typed CTRL+], then typed the command "set localecho", confirmed by pressing [Return] and exited this configuration interface by pressing [Return] again.

- The TCP connection is established and the terminal turns black. Now, every character that you type is directly sent to the remote machine through this so-called socket.

- First, I showed you what happens if I type an "s". The remote machine responds with an HTTP response that tells us that it has not implemented any HTTP Method that starts with "s". In a way, the remote server is apologizing to us for that, by displaying a status code of "501 Not Implemented" (i.e., it sees this as a server-side problem). Very friendly!

- Next, I formulated a correct HTTP request and typed 
--- GET / HTTP/1.1\r\nHost: example.org\r\n\r\n
--- Note: "\r\n" is a carriage-return followed by a new-line. You typically type this by pressing the [Return] or [Enter] key on your keyboard.

- The server responded by sending an HTTP response of "200 OK" indicating that it was able to appropriately process our request. This 200 OK was followed by several headers and the HTTP Content, i.e. the representation in HTML of the resource we requested.



# Demo 3: Static and Dynamic Web Content
## Folder: simple-webservers

In this demo, we created a local Web server that served content over port 8000 using the HTTP protocol.

- We started from sample-static-server.py (in directory "static"). That code makes use of python's SimpleHTTPRequestHandler to just serve the contents of the directory it is launched in. Run it by typing:
--- python sample_static_server.py

- We then accessed (using a Web browser) the URI http://localhost:8000 which displays the contents of the directory that this code was run in

- We created a simple Web site in the sub-directory here-is-my-website and accessed the some-website.html file from the browser. This file contains HTML markup and can thus be rendered by the browser. To demonstrate this, we added a random picture to the site.

- Next, we wanted to create a server that can serve dynamic content (see directory "dynamic"). For this, I first showed you the file sample_dynamic_server.py that also just contained the statement "Hello World", in HTML markup so that it is properly rendered by a Web browser.

- Next, I showed you the file sample_datetime.py that merely printed the current date.
--- python sample_datetime.py

- Then, we combined these two files: we imported sample_datetime into the sample_dynamic_server and then replaced "Hello World" with a call to the CurrentDate() function (line 15 in the code)
--- python sample_dynamic_server.py

- When you access http://localhost:8000 while running this server, your browser will display the current date.

- Finally, I showed you how we would turn this into a machine API. We changed the returned media type from "text/html" to "application/json" and packed our CurrentDate() into a JSON object instead of surrounding it with HTML markup. The data that this API provides (i.e., the current date) can now be more easily accessed by other software, via HTTP.

- This Web site can however not only be accessed from your device! You can replace the "localhost" with your IP (which you find using the ipconfig/ifconfig command). Now, that address (e.g., http://192.168.0.1:8000) can be used from any device that is connected to your network. And if you ask your internet service provider to assign you a static IP (at some cost), you can even get an IP address that is reachable world-wide.



# Demo 4: Stockexchange
## Folder: stockexchange

Have a look at the Guided Exercise slides for this demo.



# Demo 5: Food and Walls
## Folder: food-and-walls

This demo exists to illustrate how you might create a (very) simple game that features an online scoreboard (see food-and-walls-networked). Here, the 'client' runs the game's main logic, the 'server' runs a basic server that collects highscores, and the 'webserver' serves these highscores on a website.



# Commands

Here are some of the commands I showed in the lecture. Have fun trying them out on your system, none of this can damage your system!

Network Address Resolution
- arp -a

Trace Network Routing:
- Unix/Mac: traceroute
- Win: tracert
- Example: tracert www.google.com

Routing Table
- Unix/Max: ip route
- Win: route print

Host Address Resolution
- nslookup www.google.com