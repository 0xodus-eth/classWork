import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is waiting for client connection...")
client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Sending Data to client
client_socket.send(b"Hello, Client! This is the server speaking.")

# closing connection
client_socket.close()
