import socket

# client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Receiving Data from server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")
# closing connection
client_socket.close()
