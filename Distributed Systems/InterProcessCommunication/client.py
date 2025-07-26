import socket
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

def connect_to_server():
    """Connect to server with exception handling and encryption"""
    client_socket = None
    
    try:
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set connection timeout
        client_socket.settimeout(10)
        
        print("Connecting to server...")
        # Connect to the server running on localhost at port 12345
        client_socket.connect(('localhost', 12345))
        print("Connected to server successfully!")
        
        # Interactive messaging loop
        while True:
            try:
                # Get message from user
                message = input("\nEnter message (or 'quit' to exit): ")
                
                if message.lower() == 'quit':
                    break
                
                # Encrypt and send message to the server
                encrypted_message = encrypt_message(message)
                client_socket.send(encrypted_message.encode())
                print(f"Sent (encrypted): {encrypted_message}")
                
                # Receive the server's response (up to 1024 bytes)
                data = client_socket.recv(1024)
                if not data:
                    print("Server closed the connection")
                    break
                
                # Decrypt and display server response
                encrypted_response = data.decode()
                decrypted_response = decrypt_message(encrypted_response)
                print(f"Received (decrypted): {decrypted_response}")
                
            except KeyboardInterrupt:
                print("\nClient interrupted by user")
                break
            except socket.timeout:
                print("Server response timeout")
                break
            except Exception as e:
                print(f"Error during communication: {e}")
                break
                
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Make sure the server is running.")
    except socket.timeout:
        print("Error: Connection timeout. Server might be unreachable.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if client_socket:
            try:
                client_socket.close()
                print("Connection closed.")
            except Exception as e:
                print(f"Error closing connection: {e}")

def test_multiple_clients():
    """Test function to simulate multiple clients"""
    import threading
    
    def client_thread(client_id):
        """Function to run client in a separate thread"""
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 12345))
            
            # Send a few messages
            for i in range(3):
                message = f"Hello from client {client_id}, message {i+1}"
                encrypted_message = encrypt_message(message)
                client_socket.send(encrypted_message.encode())
                
                data = client_socket.recv(1024)
                decrypted_response = decrypt_message(data.decode())
                print(f"Client {client_id} received: {decrypted_response}")
                
                time.sleep(1)
                
            client_socket.close()
            
        except Exception as e:
            print(f"Client {client_id} error: {e}")
    
    # Create multiple client threads
    threads = []
    for i in range(3):
        thread = threading.Thread(target=client_thread, args=(i+1,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Enhanced Client with Exception Handling and Encryption")
    print("=" * 60)
    print("Features:")
    print("- Base64 encryption/decryption")
    print("- Exception handling for connection errors")
    print("- Interactive messaging")
    print("- Connection timeout handling")
    print("-" * 60)
    
    choice = input("Choose mode:\n1. Interactive client\n2. Test multiple clients\nEnter choice (1 or 2): ")
    
    if choice == "2":
        print("Testing multiple clients...")
        test_multiple_clients()
    else:
        connect_to_server()