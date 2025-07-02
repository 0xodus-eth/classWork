import socket
import time

MULTICAST_GROUP = '224.1.1.1' 
PORT = 5007 

# Create UDP socket for sending multicast messages
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Set TTL (Time To Live) for multicast packets
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

print(f"Multicast server sending to {MULTICAST_GROUP}:{PORT}") 

message_count = 1
while True: 
    message = f"Hello from multicast server! Message #{message_count}"
    server_socket.sendto(message.encode(), (MULTICAST_GROUP, PORT))
    print(f"Sent: {message}")
    message_count += 1
    time.sleep(2)  # Send a message every 2 seconds 
