from graph_utilities import generate_random_adjacency_matrix, is_valid_adjacency_matrix

n = 10  # number of vertices
m = 3   # number of components

# Generate the random adjacency matrix
adjacency_matrix = generate_random_adjacency_matrix(n, m)
print("Generated Adjacency Matrix:")
print(adjacency_matrix)

# Check if adjacency - no need
if not is_valid_adjacency_matrix(adjacency_matrix):
    print("Error: The generated matrix does not satisfy the criteria for an adjacency matrix.")
else:
    print("The generated matrix is a valid adjacency matrix.")
