# Code from brilliant.org/wiki/extended-euclidean-algorithm.
def egcd(a, b):
    """Extended euclidean algorithm, iterative implementation."""
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    g = b
    return g, x, y

# Code from geeksforgeeks.com/euclidean-algorithms-basic-and-extended.
def egcd_recursive(a, b):
    """Extended euclidean algorithm, recursive implementation."""
    if a == 0:
        return b, 0, 1
    g, u, v = egcd(b % a, a)
    x = v - (b // a) * u
    y = u
    return g, x, y

if __name__ == "__main__":
    print("Comparing results of both versions of extended gcd...")
    assert egcd(0, 15) == egcd_recursive(0, 15)
    assert egcd(15, 0) == egcd_recursive(15, 0)
    assert egcd(125478, 158452) == egcd_recursive(125478, 158452)
    assert egcd(31, 4520) == egcd_recursive(31, 4520)
    assert egcd(31, 47) == egcd_recursive(31, 47)
    assert egcd(2 ** 30, 1024) == egcd_recursive(2 ** 30, 1024)
    assert egcd(41, 41000) == egcd_recursive(41, 41000)
    print("All tests passed.")
