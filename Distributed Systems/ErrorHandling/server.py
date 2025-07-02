import Pyro4 
 
@Pyro4.expose 
class Calculator: 
    def add(self, a, b): 
        return a + b 
 
    def subtract(self, a, b): 
        return a - b 
 
    def divide(self, a, b): 
        if b == 0: 
            raise ValueError("Cannot divide by zero") 
        return a / b 
 
# Setup the daemon and the name server 
daemon = Pyro4.Daemon() 
ns = Pyro4.locateNS() 
 
# Register objects 
calculator_uri = daemon.register(Calculator) 
 
# Register objects with the name server 
ns.register("example.calculator", calculator_uri) 

print("Server is ready...") 
 
# Start the server's request loop 
daemon.requestLoop() 
 
