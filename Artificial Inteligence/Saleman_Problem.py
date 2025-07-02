import itertools

def calculate_tour_distance(tour, dist_matrix):
    """Calculate the total distance of a given tour."""
    distance = 0
    for i in range(len(tour) - 1):
        distance += dist_matrix[tour[i]][tour[i + 1]]
    return distance

def travelling_salesman_brute_force(dist_matrix, start_city=0):
    """Solve TSP using brute force by checking all permutations."""
    n = len(dist_matrix)
    cities = list(range(n))
    cities.remove(start_city)  # Remove the starting city
    
    min_distance = float('inf')
    min_path = None
    
    # Generate all permutations of the remaining cities
    for perm in itertools.permutations(cities):
        # Create the full tour: start -> perm -> start
        tour = [start_city] + list(perm) + [start_city]
        distance = calculate_tour_distance(tour, dist_matrix)
        
        if distance < min_distance:
            min_distance = distance
            min_path = tour
    
    return min_distance, min_path

def print_solution(distance, path):
    """Print the TSP solution in a readable format."""
    print("Optimal Tour:")
    print(" -> ".join(f"City {city}" for city in path))
    print(f"Total Distance: {distance}")

def main():
    # Example distance matrix for 4 cities
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    # Solve TSP starting from city 0
    distance, path = travelling_salesman_brute_force(dist_matrix, start_city=0)
    
    # Print the solution
    print_solution(distance, path)

if __name__ == "__main__":
    main()