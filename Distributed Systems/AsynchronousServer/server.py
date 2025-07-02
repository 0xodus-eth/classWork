import Pyro4 
import time 
 
@Pyro4.expose 
class Greeting: 
    def say_hello(self, name): 
        time.sleep(5)  # Simulate a delay in processing 
        return f"Hello, {name}!" 
 
# Setup the daemon and the name server 
daemon = Pyro4.Daemon() 
try:
    ns = Pyro4.locateNS() 
    # Register objects 
    greeting_uri = daemon.register(Greeting()) 
    
    # Register objects with the name server 
    ns.register("example.greeting", greeting_uri) 
    print(f"Server is ready... URI: {greeting_uri}")
except:
    greeting_uri = daemon.register(Greeting()) 
    print(f"Name server not found. Direct URI: {greeting_uri}")
 
# Start the server's request loop 
daemon.requestLoop()