import socket 
import threading 
def handle_client(client_socket): 
    request = client_socket.recv(1024) 
    print(f"Received: {request.decode()}") 
    client_socket.send(b'Hello from server') 
    client_socket.close() 
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(('localhost', 12345)) 
server.listen(5) 
 
while True: 
    client_sock, addr = server.accept() 
    print(f"Connection from {addr}") 
    client_thread = threading.Thread(target=handle_client, args=(client_sock,)) 
    client_thread.start() 
 
