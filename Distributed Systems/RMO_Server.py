import Pyro4 
 
@Pyro4.expose 
class Greeting: 
    def say_hello(self, name): 
        return f"Hello, {name}!" 
 
@Pyro4.expose 
class Calculator: 
    def add(self, a, b): 
        return a + b 
 
    def subtract(self, a, b): 
        return a - b 
 
# Setup the daemon and the name server 
daemon = Pyro4.Daemon() 
ns = Pyro4.locateNS() 
 
# Register objects 
greeting_uri = daemon.register(Greeting) 
calculator_uri = daemon.register(Calculator) 
 
# Register objects with the name server 
ns.register("example.greeting", greeting_uri) 
ns.register("example.calculator", calculator_uri) 
 
print("Server is ready...") 
 
# Start the server's request loop 
daemon.requestLoop() 
 
