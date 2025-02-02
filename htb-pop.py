# this python script runs a HTTP server and uses paplay to note when you get a request.
# nice for xss and ssrf stuff

from http.server import BaseHTTPRequestHandler, HTTPServer
import os

port=9999

class webserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()
        os.system("paplay /usr/share/sounds/freedesktop/stereo/bell.oga")
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("localhost",port),webserver)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server.")
        server.server_close()
