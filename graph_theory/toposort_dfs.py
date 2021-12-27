def visit(u, neighbors, visited: set, pending:set, queue: list):
    visited.add(u)
    pending.add(u)
    for v in neighbors[u]:
        if v not in visited:
            visit(v, neighbors, visited, pending, queue)
        elif v in pending:
            raise Exception('Cycle detected. Cannot find a topological ordering.')
    pending.remove(u)
    queue.append(u)


def toposort(vertices, neighbors):
    visited = set()
    pending = set()
    queue = []
    try:
        for u in vertices:
            if u not in visited:
                visit(u, neighbors, visited, pending, queue)
        queue.reverse()
    except:
        queue = False
    return queue


if __name__ == '__main__':
    print('Testing toposort function...')
    
    vertices = [1, 2, 3]
    neighbors = {1: [2, 3], 2: [3], 3: []}
    assert toposort(vertices, neighbors) == [1, 2, 3]

    vertices = [1, 2, 3]
    neighbors = {1: [2], 2: [3], 3: [1]}
    assert toposort(vertices, neighbors) is False

    vertices = [1, 2, 3, 4, 5]
    neighbors = {1: [2], 2: [3], 3: [], 4: [5], 5: []}
    assert toposort(vertices, neighbors) == [4, 5, 1, 2, 3]

    print('Tests successfully passed.')
