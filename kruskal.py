class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Initialize parent for each node
        self.rank = [0] * n  # Initialize rank for each node to 0

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])

    mst = []
    disjoint_set = DisjointSet(n)

    # Step 2: Process each edge
    for u, v, weight in edges:
        # Step 3: Check if including this edge forms a cycle
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))  # Include edge in MST
            disjoint_set.union(u, v)  # Union the sets of u and v

    return mst


# Example usage
# Number of vertices (n) and edges (edges as tuples of form (u, v, weight))
n = 4  # Number of vertices
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

# Find the MST using Kruskal's Algorithm
mst = kruskal(n, edges)

# Output the edges in the MST
print("Edges in the Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"({u}, {v}) with weight {weight}")
