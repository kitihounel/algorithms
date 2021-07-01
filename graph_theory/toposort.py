from collections import Counter
from heapq import heapify, heappop, heappush

def toposort(vertices: set, neighbors: dict):
    """Topological sort of a graph, using Kahn's algorithm"""
    indegrees = Counter()
    for u in vertices:
        indegrees.update(neighbors[u])
    q = [u for u in vertices if indegrees[u] == 0]
    heapify(q)
    ordering = []
    k = 0
    while len(q) != 0:
        u = heappop(q)
        ordering.append(u)
        k += 1
        for v in neighbors[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                heappush(q, v)
    return False if k != len(vertices) else ordering

if __name__ == "__main__":
    print("Testing toposort function...")
    
    vertices = {1, 2, 3}
    neighbors = {1: [2, 3], 2: [3], 3: []}
    assert toposort(vertices, neighbors) == [1, 2, 3]

    vertices = {1, 2, 3}
    neighbors = {1: [2], 2: [3], 3: [1]}
    assert toposort(vertices, neighbors) is False

    vertices = {1, 2, 3, 4, 5}
    neighbors = {1: [2], 2: [3], 3: [], 4: [5], 5: []}
    assert toposort(vertices, neighbors) == [1, 2, 3, 4, 5]

    print("All tests passed.")
