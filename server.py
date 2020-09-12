import http.server
import socketserver
from http import HTTPStatus


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

httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()