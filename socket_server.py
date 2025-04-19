# python socket_server.py

import socket
from socketserver import BaseRequestHandler, TCPServer

class MyHandler(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print(f"Received: {data}")
        self.request.sendall(b"Hello, Client!")

server = TCPServer(('localhost', 9999), MyHandler)
server.serve_forever()
