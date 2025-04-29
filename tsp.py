import itertools

def tsp_bruteforce(distances):
    n = len(distances)
    min_path = None
    min_distance = float('inf')
    
    for permutation in itertools.permutations(range(1, n)):
        current_distance = distances[0][permutation[0]]
        for i in range(len(permutation)-1):
            current_distance += distances[permutation[i]][permutation[i+1]]
        current_distance += distances[permutation[-1]][0]
        
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = (0,) + permutation + (0,)
    
    return min_path, min_distance

# Example usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, distance = tsp_bruteforce(distances)
print(f"Optimal path: {path}, Distance: {distance}")