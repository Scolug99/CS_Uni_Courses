import http.server
import socketserver

HTTP_PORT = 8080

def generateHtmlStringFromScoreboard():
	# Open scores file and read it line-by-line into 'lines'
    highscoresFile = open("food-and-walls-highscores.txt","r")
    lines = highscoresFile.readlines() 
    
    # HTML Heading
    returnHtml = "<h1>Scoreboard</h1>"
    
    # HTML Table
    returnHtml += "<table>"
    
    for line in lines: 
        elements = line.split(",")
    
        scoreDate = elements[0]
        playerName = elements[1]
        score = elements[2]
        
        returnHtml += "<tr><td>" + playerName + "</td><td>" + score + "</td></tr>"

    # Finalize HTML Table
    returnHtml += "</table>"
    
    return returnHtml
    
class MyCustomRequestHandler(http.server.BaseHTTPRequestHandler):
            
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        payload_html_head = "<html><body>"
        payload_html_content = generateHtmlStringFromScoreboard()
        payload_html_tail = "</body></html>"
        payload_html_combined = (payload_html_head + payload_html_content + payload_html_tail).encode("utf8")
        
        self.wfile.write(payload_html_combined)
            

httpd = socketserver.TCPServer(("", HTTP_PORT), MyCustomRequestHandler)
print("Serving http requests at port", HTTP_PORT)
httpd.serve_forever()