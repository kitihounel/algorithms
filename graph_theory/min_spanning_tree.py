from operator import itemgetter

class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.weights = {}
        self.subset_count = n

    def __getitem__(self, i):
        # Check for previously unknown object
        if i not in self.parents:
            self.parents[i] = i
            self.weights[i] = 1
            return i

        # Find path of objects leading to the root
        path = [i]
        root = self.parents[i]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # Compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, i, j):
        p, q = self[i], self[j]
        if p == q:
            return False

        r, d = (p, q) if self.weights[p] > self.weights[q] else (q, p)
        self.weights[r] += self.weights[d]
        self.parents[d] = r
        self.subset_count -= 1
        return True

def min_spanning_tree(n, edges):
    """Min spanning tree construction using Kruskal algorithm.
    
    The first argument is the number of vertices in the graph and the second
    is the edges list. Each edge is a triple (src, dst, weight).
    The return value is a triple with:
        - a list with the edges in the min spanning tree,
        - the cost of the min spanning tree and,
        - an integer, the number of connected components in the tree (1 if the
          tree is connected, another value if there a several components).
    """
    edges.sort(key=itemgetter(2))
    ds = UnionFind(n)
    tree = []
    cost = 0
    for u, v, w in edges:
        if ds.union(u, v):
            cost += w
            e = (u, v)
            tree.append(e)
    tree.sort()
    return tree, cost, ds.subset_count

if __name__ == "__main__":
    print("Checking min spanning trees...")
    
    edges = [(0, 1, 1), (1, 2, 2), (1, 3, 3), (2, 3, 0)]
    assert min_spanning_tree(4, edges) == ([(0, 1), (1, 2), (2, 3)], 3, 1)

    edges = [(0, 1, 100)]
    assert min_spanning_tree(2, edges) == ([(0, 1)], 100, 1)

    edges = []
    assert min_spanning_tree(3, edges) == ([], 0, 3)

    print("All tests passed.")
