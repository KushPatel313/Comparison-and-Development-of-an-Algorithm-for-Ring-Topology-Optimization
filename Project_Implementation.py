import time

def select_nodes(matrix, current, exclude):
    # Select two nodes with the minimum cost excluding the specified nodes
    costs = [(matrix[current][j], j) for j in range(len(matrix)) if j not in exclude]
    return sorted(costs, key=lambda x: x[0])[:2]

def tsp_full_ring(matrix):
    n = len(matrix)  # Number of nodes
    conn_nodes = [[] for _ in range(n)]  # List to store connected nodes for each node

    for i in range(n):
        if i == 0:
            # Connect starting node to two nodes with the lowest cost/weight
            rx1, rx2 = select_nodes(matrix, i, {i})
            conn_nodes[i] = [rx1[1], rx2[1]]
        elif i == n - 2:
            # For the second-to-last node, connect to one new node (nx)
            last_node = conn_nodes[i-1][-1]  # Last node connected in the previous step
            nx = select_nodes(matrix, last_node, set(conn_nodes[i-1]))[0]
            conn_nodes[i].append(nx[1])
        elif i == n - 1:
            # For the last node, connect it back to the start
            conn_nodes[i].append(conn_nodes[0][0])
        else:
            # For other nodes, connect to two new nodes (rx1, rx2)
            last_node = conn_nodes[i-1][-1]
            rx1, rx2 = select_nodes(matrix, last_node, set(conn_nodes[i-1]))
            conn_nodes[i].extend([rx1[1], rx2[1]])

        # Pruning to keep only 100 elements
        if (i+2) % 10 == 0 and i != 0:
            conn_nodes[i] = conn_nodes[i][:100]

    # Now find the minimum cost path starting from each node
    min_cost = float('inf')
    min_path = None
    for st in range(n):
        path = [st]
        current = st
        visited = {st}
        cost = 0
        for _ in range(n - 1):
            next_node = select_nodes(matrix, current, visited)[0][1]
            cost += matrix[current][next_node]
            path.append(next_node)
            visited.add(next_node)
            current = next_node
        # Add the cost to return to the starting node
        cost += matrix[path[-1]][st]
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

# Example usage:
# Define a cost matrix for testing (this should be replaced by actual data)
# Given 12x12 matrix

original_matrix =  [
    [0, 930, 993, 1138, 218, 458, 1194, 637, 234, 577, 529, 371],
    [930, 0, 1748, 857, 510, 901, 1022, 785, 659, 421, 130, 399],
    [993, 1748, 0, 564, 795, 901, 1076, 749, 795, 612, 441, 669],
    [1138, 857, 564, 0, 768, 1460, 481, 930, 49, 948, 381, 806],
    [218, 510, 795, 768, 0, 1380, 583, 534, 434, 516, 1133, 949],
    [458, 901, 901, 1460, 1380, 0, 946, 552, 658, 1030, 929, 654],
    [1194, 1022, 1076, 481, 583, 946, 0, 754, 1372, 928, 816, 930],
    [637, 785, 749, 930, 534, 552, 754, 0, 1372, 1257, 769, 616],
    [234, 659, 795, 494, 345, 491, 372, 1257, 0, 390, 757, 321],
    [577, 421, 612, 948, 516, 658, 928, 769, 390, 0, 681, 363],
    [529, 130, 441, 381, 1133, 1030, 816, 769, 757, 681, 0, 928],
    [371, 399, 669, 806, 949, 929, 930, 616, 321, 363, 928, 0]
]
# Convert to a 9x9 matrix
cost_matrix = [row[:12] for row in original_matrix[:12]]

start_time = time.time()

# Perform some operations
# time.sleep(1)  # Simulating some computational work

# Calculate computational time

# Calculate computational time
computational_time = time.time() - start_time

# Call the function with the cost matrix
tsp_path, tsp_cost = tsp_full_ring(cost_matrix)
tsp_path, tsp_cost

print(tsp_path)
print(tsp_cost)
# print("Computational time required:", computational_time, "seconds")
computational_time = (time.time() - start_time) * 1000  # Convert to milliseconds
print("Computational time required:", computational_time, "milliseconds")
