import http.server
import socketserver
from datetime import datetime

PORT = 8000

def getCurrentDateTime():
    today = datetime.now()
    return str(today)

class MyCustomRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()        
		
        payload = "Hello HSG-World! The current time is: " + getCurrentDateTime()
                
        payload = payload.encode("utf8")
        self.wfile.write(payload)
            
httpd = socketserver.TCPServer(("", PORT), MyCustomRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()
