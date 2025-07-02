from math import exp
import matplotlib.pyplot as plt

# 1. Setup
iterations = 100
initial_temp = 10
iters = list(range(iterations))
temperatures = [initial_temp / (i + 1) for i in iters]

# 2. Different cost differences
deltas = [0.01, 0.1, 1.0]  # Corrected variable name from 'delts' to 'deltas'

# 3. Compute and plot Metropolis criterion
for d in deltas:
    acceptance_probs = [exp(-d / t) for t in temperatures]
    plt.plot(iters, acceptance_probs, label=f"ΔE = {d:.2f}")  # Fixed f-string formatting

# 4. Final plot
plt.title("Metropolis Acceptance Probability")
plt.xlabel("Iteration")
plt.ylabel("P(accept worse move)")
plt.legend()
plt.grid(True)  # Corrected 'true' to 'True'
plt.show()