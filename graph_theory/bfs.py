from collections import deque
from graph_theory.dfs import visit


def bfs(s, neighbors):
    q = deque()
    q.append(s)
    visited = {s}
    while len(q) != 0:
        u = q.popleft()
        for v in neighbors[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
