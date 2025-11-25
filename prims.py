import heapq

def prim(n, graph):
    # Initialize a list to store the MST
    mst = []
    
    # A list to track if a node is in the MST or not
    in_mst = [False] * n
    
    # Min-heap (priority queue) to store edges in the form (weight, (u, v))
    # Start with node 0 and initialize the heap with edges from node 0
    min_heap = [(0, 0)]  # (weight, node)
    
    total_weight = 0
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)  # Extract the node with the minimum edge weight
        
        if in_mst[u]:  # Skip if the node is already included in MST
            continue
        
        in_mst[u] = True  # Include node u in MST
        total_weight += weight  # Add weight of this edge to the total MST weight
        
        # Add the edge to the MST
        if weight != 0:  # Ignore the first "0" weight edge used to start the algorithm
            mst.append((u, weight))
        
        # Explore the neighbors of the node u
        for v, edge_weight in graph[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (edge_weight, v))  # Add the neighboring edge to the heap
    
    return mst, total_weight


# Example usage
n = 5  # Number of vertices
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7), (4, 9)],
    4: [(3, 9)]
}

# Get MST using Prim’s Algorithm
mst, total_weight = prim(n, graph)

# Output the MST edges and total weight
print("Edges in the Minimum Spanning Tree (MST):")
for u, weight in mst:
    print(f"Edge (u, v) = {u} with weight {weight}")

print(f"Total weight of the MST: {total_weight}")
