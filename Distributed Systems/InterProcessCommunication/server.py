import socket
import threading
import base64
import time

def encrypt_message(message):
    """Simple base64 encryption"""
    try:
        encoded = base64.b64encode(message.encode()).decode()
        return encoded
    except Exception as e:
        print(f"Encryption error: {e}")
        return message

def decrypt_message(encrypted_message):
    """Simple base64 decryption"""
    try:
        decoded = base64.b64decode(encrypted_message.encode()).decode()
        return decoded
    except Exception as e:
        print(f"Decryption error: {e}")
        return encrypted_message

def handle_client(conn, addr):
    """Handle individual client connection"""
    print(f"[{time.strftime('%H:%M:%S')}] New client connected: {addr}")
    
    try:
        while True:
            # Receive data from client
            data = conn.recv(1024)
            if not data:
                print(f"[{time.strftime('%H:%M:%S')}] Client {addr} disconnected")
                break
            
            # Decrypt the received message
            encrypted_message = data.decode()
            decrypted_message = decrypt_message(encrypted_message)
            print(f"[{time.strftime('%H:%M:%S')}] Received from {addr}: {decrypted_message}")
            
            # Create response message
            response = f"Server received: {decrypted_message} at {time.strftime('%H:%M:%S')}"
            
            # Encrypt and send response
            encrypted_response = encrypt_message(response)
            conn.send(encrypted_response.encode())
            
    except ConnectionResetError:
        print(f"[{time.strftime('%H:%M:%S')}] Client {addr} forcibly disconnected")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Error handling client {addr}: {e}")
    finally:
        # Clean up the connection
        try:
            conn.close()
            print(f"[{time.strftime('%H:%M:%S')}] Connection with {addr} closed")
        except Exception as e:
            print(f"Error closing connection: {e}")

def start_server():
    """Start the multi-threaded server"""
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Allow socket reuse
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket to a specific host and port
        server_socket.bind(('localhost', 12345))
        
        # Listen for incoming connections (max 5 connections waiting in queue)
        server_socket.listen(5)
        print(f"[{time.strftime('%H:%M:%S')}] Multi-threaded server started on localhost:12345")
        print("Server supports:")
        print("- Multiple concurrent clients")
        print("- Base64 encryption/decryption")
        print("- Exception handling")
        print("-" * 50)
        
        while True:
            try:
                # Accept a connection from a client
                conn, addr = server_socket.accept()
                
                # Create a new thread to handle the client
                client_thread = threading.Thread(
                    target=handle_client, 
                    args=(conn, addr),
                    daemon=True  # Thread will die when main program exits
                )
                client_thread.start()
                
            except KeyboardInterrupt:
                print(f"\n[{time.strftime('%H:%M:%S')}] Server shutting down...")
                break
            except Exception as e:
                print(f"[{time.strftime('%H:%M:%S')}] Error accepting connection: {e}")
                
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Server startup error: {e}")
    finally:
        try:
            server_socket.close()
            print(f"[{time.strftime('%H:%M:%S')}] Server socket closed")
        except:
            pass

if __name__ == "__main__":
    start_server()