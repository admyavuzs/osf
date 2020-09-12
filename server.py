import http.server
import socketserver
from http import HTTPStatus
from prometheus_client import start_http_server

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(b'Hello Python')
        
        if  self.path=='/health':
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(b'I am healty')

#httpd = socketserver.TCPServer(('', 8080), Handler)
#httpd.serve_forever()

if __name__ == "__main__":
    start_http_server(8081)
    server = http.server.HTTPServer(('', 8080), Handler)
    server.serve_forever()
