import Pyro4

# Connect to the server using URI
uri = "PYRONAME:example.greeting"
greeting = Pyro4.Proxy(uri)

# Call the remote method
print(greeting.say_hello("Client"))