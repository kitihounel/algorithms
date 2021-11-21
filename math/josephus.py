def josephus(n, k):
    """Iterative O(N) solution to Josephus problem using 1-indexing.
    
    See https://cp-algorithms.com/others/josephus_problem.html for a good introduction.
    """
    a = 1
    for i in range(1, n + 1):
        a = (a + k - 1) % i + 1
    return a


def bin_josephus(n):
    """Solve Josephus problem for k=2 with 1-indexing.

    If n is a power of 2, the survivor is always 1.
    Otherwise, n = 2^p + l (for some p), and the survivor will be 2l + 1.
    Details in this video: https://www.youtube.com/watch?v=uCsD3ZGzMgE.
    """
    s = bin(n)
    return int(s[3:] + '1', 2)


if __name__ == "__main__":
    print('Testing Josephus problem solution.')

    n, k = 3756, 4
    assert josephus(n, k) == 3399

    n, k = 10000, 3
    assert josephus(n, k) == 2692

    n, k = 25615, 6
    assert josephus(n, k) == 1372

    n, k = 9751, 47
    assert josephus(n, k) == 9456

    n, k = 5, 2
    assert josephus(n, k) == 3

    n, k = 25, 18
    assert josephus(n, k) == 2

    n, k = 85, 7
    assert josephus(n, k) == 38

    assert bin_josephus(1024) == 1
    assert bin_josephus(2 ** 16) == 1
    assert bin_josephus(2 ** 27) == 1
    assert bin_josephus(10) == 5
    assert bin_josephus(7) == 7
    assert bin_josephus(1025) == 3

    print('Tests successfully passed.')
