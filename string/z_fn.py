def z_fn(s):
    """Z-function implementation. In this implementation, z[0] = length(s).

    Code from https://cp-algorithms.com/string/z-function.html.
    """
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = 0, 0
    for i in range(n):
        if i <= r:
            z[i] = min (r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

def prefix_occurrences(s):
    """Computes the number of occurences of each prefix of a given string.

    Returns an array a of same length as s such that a[i] is the number
    of times the prefix s[0..i(included)] appears in s.
    """
    n = len(s)
    z = z_fn(s)
    a = [0 for _ in range(n)]
    for v in filter(lambda v: v != 0, z):
        a[v-1] += 1
    for i in range(n-1, 0, -1):
        a[i-1] += a[i]
    return a
