from collections import deque


def bfs(start, neighbors):
    q = deque()
    q.append(start)
    visited = {start}
    while len(q) != 0:
        u = q.popleft()
        a = [v for v in neighbors[u] if v not in visited]
        q.extend(a)
        visited.update(a)
