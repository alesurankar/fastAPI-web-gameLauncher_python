import socket
import threading

# Create a Socket Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5001))  # Bind to localhost and port 5001
server.listen()

# List to store client connections
clients = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            if msg:
                print(f"Received message: {msg}")
                # Broadcast the message to all connected clients
                for client in clients:
                    if client != client_socket:
                        client.send(msg.encode("utf-8"))
            else:
                break
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

def start_server():
    print("Server started...")
    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
