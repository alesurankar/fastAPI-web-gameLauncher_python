# python socket_client.py


import socket

def send_message():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))
    client.sendall(b"Hello Server!")
    data = client.recv(1024)
    client.close()
    return data
