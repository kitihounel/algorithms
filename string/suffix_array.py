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
    """Suffix array construction

    Code adapted from https://hackerrank.com/topics/suffix-array
    """
    n = len(s)
    a = [Suffix(j, s) for j in range(n)]
    ranks = [ord(c) for c in s]
    length = 1
    while length < n:
        for j, suffix in enumerate(a):
            x = ranks[j]
            y = ranks[j+length] if j + length < n else -1
            suffix.rank = (x, y)
            suffix.index = j
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

def lcp_array(s, suffixes):
    """Longest common prefix array with Kasai algorithm

    Code adapted from https://hackerrank.com/topics/lcp-array
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
        k = k - 1 if k != 0 else 0

    return a

s = "abcdefa"
a = suffix_array(s)
p = lcp_array(s, a)
print(a, p)
