from collections import defaultdict

def idfs(s, neighbors, start_time):
    """Iterative DFS"""
    if start_time is None:
        start_time = 0
    discovery_time = {s:start_time}
    finish_time = {}
    current_time = start_time + 1
    q = [s]
    visited = {s}
    neighbor_pointers = defaultdict(int)
    while len(q) != 0:
        u = q.pop()
        pushed_again = False
        a = neighbors[u]
        j = neighbor_pointers[u]
        while j < len(a):
            v = a[j]
            if v not in visited:
                pushed_again = True
                q.append(u)
                q.append(v)
                visited.add(v)
                discovery_time[v] = current_time
                current_time += 1
            j += 1
            if pushed_again:
                break
        neighbor_pointers[u] = j
        if not pushed_again:
            finish_time[u] = current_time
            current_time += 1
    return discovery_time, finish_time, current_time

def visit(u, neighbors, visited: set):
    visited.add(u)
    for v in neighbors[u]:
        if v not in visited:
            visit(v, neighbors, visited)

def rdfs(vertices, neighbors):
    visited = set()
    for u in vertices:
        if u not in visited:
            visit(u, neighbors, visited)
