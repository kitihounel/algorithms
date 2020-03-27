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

def next_power_of_two(n):
    """Return the smallest power of 2 greater or equal to an integer."""
    return 1 if n <= 0 else n if not (n & (n - 1)) else 1 << n.bit_length()

def suffix_array(s):
    """Suffix array construction.

    Code adapted from https://hackerrank.com/topics/suffix-array.
    """
    n = len(s)
    a = [Suffix(j, s) for j in range(n)]
    ranks = [ord(c) for c in s]
    maxLength = next_power_of_two(n)
    chunkLength = 1
    while chunkLength <= maxLength:
        h = div(chunkLength, 2)
        for suffix in a:
            x = ranks[suffix.index]
            y = ranks[suffix.index + h] if suffix.index + h < n else -1
            suffix.rank = (x, y)
        a.sort()

        rank = 0
        ranks[a[0].index] = rank
        for j in range(1, n):
            previous, current = a[j-1], a[j]
            if previous.rank != current.rank:
                rank += 1
            ranks[current.index] = rank

        chunkLength *= 2

    return [suffix.index for suffix in a]

def suffix_array_v2(s):
    """Suffix array construction, altenative implementation."""
    n = len(s)
    suffixes = [j for j in range(n)]
    ranks = [ord(c) for c in s]
    sortKeys = [None for j in range(n)]
    maxLength = next_power_of_two(n)
    chunkLength = 1
    while chunkLength <= maxLength:
        h = div(chunkLength, 2)
        for j in suffixes:
            sortKeys[j] = (ranks[j], ranks[j+h] if  j + h < n else -1)
        suffixes.sort(key=lambda j: sortKeys[j])

        ranks[suffixes[0]] = 0
        for j in range(1, n):
            p, c = suffixes[j-1], suffixes[j]
            ranks[c] = ranks[p] + (1 if sortKeys[p] != sortKeys[c] else 0)

        chunkLength *= 2

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
