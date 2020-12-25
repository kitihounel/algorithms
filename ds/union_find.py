"""Union-Find data strucure.

Sources
  - code.activestate.com/recipes/215912
  - code.activestate.com/recipes/221251
"""
class UnionFind:
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, i):
        """Find the root of the set that an object belongs to.

        Object must be hashable; previously unknown objects become new singleton sets.
        """
        # Check for previously unknown object.
        if i not in self.parents:
            self.parents[i] = i
            self.weights[i] = 1
            return i

        # Find path of objects leading to the root.
        path = [i]
        root = self.parents[i]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # Compress the path and return.
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, i, j):
        """Find the sets containing two given objects and merge them."""
        x, y = self[i], self[j]
        if x != y:
            r, d = (x, y) if self.weights[x] > self.weights[y] else (y, x)
            self.weights[r] += self.weights[d]
            self.parents[d] = r

    def union_all(self, *objects):
        """Find the sets containing the given objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
