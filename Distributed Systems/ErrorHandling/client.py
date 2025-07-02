import Pyro4 
 
# Connect to the server using the URI 
calculator_uri = "PYRONAME:example.calculator" 
calculator = Pyro4.Proxy(calculator_uri) 
 
try: 
    print(f"10 / 0 = {calculator.divide(10, 0)}")  # This will raise an exception 
except Pyro4.errors.CommunicationError as e: 
    print(f"Communication error: {e}") 
except ValueError as e: 
    print(f"Error in remote method: {e}") 
 

 

