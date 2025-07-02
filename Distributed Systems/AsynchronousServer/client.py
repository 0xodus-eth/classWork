import Pyro4
import time
import threading
from concurrent.futures import ThreadPoolExecutor

# Connect to the server using the URI
greeting_uri = "PYRONAME:example.greeting"
greeting = Pyro4.Proxy(greeting_uri)

# Method 1: Simple threading approach
print("--- Threading-based async approach ---")

def make_remote_call(name):
    """Function to make the remote call in a separate thread"""
    return greeting.say_hello(name)

# Start the call in a separate thread
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(make_remote_call, "Alice")
    
    # Do other work while waiting
    print("Doing other work while waiting for the response...")
    for i in range(3):
        print(f"Working... {i+1}")
        time.sleep(0.5)
    
    # Get the result (will block if not ready)
    response = future.result()
    print(f"Received: {response}")

# Method 2: Manual threading
print("\n--- Manual threading approach ---")

result = None
done = False

def threaded_call():
    global result, done
    result = greeting.say_hello("Bob")
    done = True

# Start thread
thread = threading.Thread(target=threaded_call)
thread.start()

# Do other work
print("Doing other work while waiting...")
while not done:
    print("Still working...")
    time.sleep(0.5)

thread.join()
print(f"Threaded result: {result}")