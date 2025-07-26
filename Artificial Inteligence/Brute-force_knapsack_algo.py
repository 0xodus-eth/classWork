import random
import time
from itertools import combinations

# Define a class to hold item details
class Item:
    def __init__(self, name, size, value):
        self.name = name
        self.size = size
        self.value = value

# Brute-force knapsack solver
def knapsack(items, capacity):
    max_value = 0
    best_combo = []
    
    # Generate all possible combinations of items
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            total_size = sum(item.size for item in combo)
            total_value = sum(item.value for item in combo)
            
            # Check if combo fits within capacity and has better value
            if total_size <= capacity and total_value > max_value:
                max_value = total_value
                best_combo = combo
    
    return max_value, best_combo

# Function to generate a random list of N items
def generate_items(n):
    items = []
    for i in range(n):
        name = f"Item{i+1}"
        size = random.randint(1, 5)  # Size in range 1 to 5
        value = random.randint(1, 10)  # Value in range 1 to 10
        items.append(Item(name, size, value))
    
    return items


# Run multiple tests with different knapsack sizes
def run_tests():
    for size_multiplier in [1.0, 2.5, 4.0]:  # Different capacity scales
        print(f"\nTesting with backpack size multiplier: {size_multiplier}")
        for n in [10, 12, 14, 16, 18, 20, 22]:  # Varying number of items
            total_time = 0
            for _ in range(10):  # Run 10 trials for each size
                items = generate_items(n)
                capacity = int(size_multiplier * n)
                start = time.time()
                value, combo = knapsack(items, capacity)
                end = time.time()
                total_time += (end - start)
            avg_time = total_time / 10
            print(f"N={n}, Capacity={capacity}, Avg Time={avg_time:.4f} sec")

# Add this to actually run the tests
if __name__ == "__main__":
    run_tests()