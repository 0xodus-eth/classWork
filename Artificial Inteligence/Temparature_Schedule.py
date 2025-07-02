import matplotlib.pyplot as plt

# 1. Total number of iterations
iterations = 100
initial_temp = 10

# 2. Compute temperature schedule
iters = list(range(iterations))
temperatures = [initial_temp / (i + 1) for i in iters]

# 3. Plot
plt.plot(iters, temperatures, color='orange')
plt.title("Temperature Decay over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()