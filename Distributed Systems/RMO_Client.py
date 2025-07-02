import Pyro4 
 
# Connect to the server using the URIs for multiple objects 
greeting_uri = "PYRONAME:example.greeting" 
calculator_uri = "PYRONAME:example.calculator" 

greeting = Pyro4.Proxy(greeting_uri) 
calculator = Pyro4.Proxy(calculator_uri) 
 
# Call remote methods 
print(greeting.say_hello("Alice")) 
print(f"10 + 5 = {calculator.add(10, 5)}") 
print(f"10 - 5 = {calculator.subtract(10, 5)}") 
 
