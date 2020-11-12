from itertools import product

def matrix_product(a, b):
    m, n, o = len(a), len(b[0]), len(b)
    p = [[0 for _ in range(n)] for _ in range(m)]
    for i, j, k in product(range(m), range(n), range(o)):
        p[i][j] += a[i][k] * b[k][j]
    return p

if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    assert matrix_product(a, a) == [[7, 10], [15, 22]]

    b = [[1, 0, -2], [0, 3, -1]]
    c = [[0, 3], [-2, -1], [0, 4]]
    assert matrix_product(b, c) == [[0, -5], [-6, -7]]

    i = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert matrix_product(i, i) == i

    d = [[6, 4, 24], [1, -9, 8]]
    assert matrix_product(d, i) == d

    e = [[15, 7, -9], [5, -5, -2], [12, 8, 3]]
    assert matrix_product(i, e) == e
