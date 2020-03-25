from operator import floordiv as div

class Suffix:
    def __init__(self, index, s):
        self.index = index
        self.string = s
        self.rank = (-1, -1)

    def __lt__(self, other):
        if not isinstance(other, Suffix):
            raise Exception("Invalid argument for comparison with Suffix")
        return self.rank < other.rank

def suffix_array(s):
    """Suffix array construction.

    Code adapted from https://hackerrank.com/topics/suffix-array.
    """
    n = len(s)
    a = [Suffix(j, s) for j in range(n)]
    ranks = [ord(c) for c in s]
    length = 1
    while length < n:
        for suffix in a:
            m = div(length, 2)
            x = ranks[suffix.index]
            y = ranks[suffix.index + m] if suffix.index + m < n else -1
            suffix.rank = (x, y)
        a.sort()

        rank = 0
        ranks[a[0].index] = rank
        for j in range(1, n):
            previous, current = a[j-1], a[j]
            if previous.rank != current.rank:
                rank += 1
            ranks[current.index] = rank

        length *= 2

    return [suffix.index for suffix in a]

def suffix_array_v2(s):
    """Suffix array construction, altenative implementation."""
    n = len(s)
    suffixes = [j for j in range(n)]
    ranks = [ord(c) for c in s]
    sortKeys = [None for j in range(n)]
    length = 1
    while length < len(s):
        m = div(length, 2)
        for j in suffixes:
            sortKeys[j] = (ranks[j], ranks[j+m] if  j + m < n else -1)
        suffixes.sort(key=lambda j: sortKeys[j])

        ranks[suffixes[0]] = 0
        for j in range(1, n):
            p, c = suffixes[j-1], suffixes[j]
            ranks[c] = ranks[p] + (1 if sortKeys[p] != sortKeys[c] else 0)

        length *= 2

    return suffixes

def lcp_array(s, suffixes):
    """Longest common prefix array with Kasai algorithm.

    Code adapted from https://hackerrank.com/topics/lcp-array.
    Explaination about the meaning of values in the LCP is from
    the article of GeeksForGeeks about LCP array.
    A value a[i] indicates length of the longest common prefix of the
    suffixes indexed by suffixes[i] and suffixes[i+1].
    suffixes[n-1] is not defined as there is no suffix after it.
    """
    n = len(s)
    a = [0 for _ in range(n)]
    rank = {v:j for j, v in enumerate(suffixes)}

    k = 0
    for i in range(n):
        r = rank[i]
        if r == n - 1:
            k = 0
            continue
        j = suffixes[r+1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]:
            k += 1
        a[r] = k
        k = k - 1 if k > 0 else 0

    return a
