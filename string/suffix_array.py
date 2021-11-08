class Suffix:
    def __init__(self, index, s):
        self.index = index
        self.string = s
        self.rank = (-1, -1)

    def __lt__(self, other):
        if not isinstance(other, Suffix):
            raise Exception("Invalid argument for comparison with Suffix")
        return self.rank < other.rank


def suffix_array_slow(s):
    """Suffix array construction.

    Code from https://hackerrank.com/topics/suffix-array.
    """
    n = len(s)
    suffixes = [Suffix(j, s) for j in range(n)]
    ranks = [ord(c) for c in s]
    length, limit = 1, 2 * n
    while length < limit:
        h = length // 2
        for suffix in suffixes:
            x = ranks[suffix.index]
            y = ranks[suffix.index + h] if suffix.index + h < n else -1
            suffix.rank = (x, y)
        suffixes.sort()

        rank = 0
        ranks[suffixes[0].index] = rank
        for j in range(1, n):
            previous, current = suffixes[j-1], suffixes[j]
            if previous.rank != current.rank:
                rank += 1
            ranks[current.index] = rank

        length *= 2

    return [suffix.index for suffix in suffixes]


def suffix_array(s):
    """Suffix array construction, faster implementation."""
    n = len(s)
    suffixes = [j for j in range(n)]
    ranks = [ord(c) for c in s]
    sort_keys = [None for j in range(n)]
    length, limit = 1, 2 * n
    while length < limit:
        h = length // 2
        for j in suffixes:
            sort_keys[j] = (ranks[j], ranks[j+h] if  j + h < n else -1)
        suffixes.sort(key=lambda j: sort_keys[j])

        ranks[suffixes[0]] = 0
        for j in range(1, n):
            p, c = suffixes[j-1], suffixes[j]
            ranks[c] = ranks[p] + (1 if sort_keys[p] != sort_keys[c] else 0)

        length *= 2

    return suffixes


def lcp_array(s, suffixes):
    """Longest common prefix array with Kasai algorithm.

    Explaination about the meaning of values in the LCP can be
    found in the article of GeeksForGeeks about LCP array.
    A value a[i] indicates length of the longest common prefix of the
    suffixes indexed by suffixes[i] and suffixes[i+1].
    suffixes[n-1] is not defined as there is no suffix after it.

    Code from https://hackerrank.com/topics/lcp-array.
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
        k = max(k - 1, 0)

    return a


def bwt(s):
    """Compute Burrows-Wheeler transform using suffix array.

    It works by appending the string to itself and computing
    the suffix array of the result string. It then selects suffixes
    which indexes are less than |s|. These suffixes are the cyclic
    shifts of the original string.

    IMPORTANT: there is faster version of this function in the file named
    'burrows_wheeler.py'.
    """
    indexes = [j for j in suffix_array(s * 2) if j < len(s)]
    return "".join(s[j-1] for j in indexes)


def distinct_substring_count(s):
    """Return the number of distinct substrings in a given string.

    Note that the empty substring is not taken into account.
    For explaination, see these pages.
        - stackoverflow.com/questions/34882666, answer by David Eisenstat.
        - https://www.geeksforgeeks.org/count-distinct-substrings-string-using-suffix-array/.
    """
    n = len(s)
    a = suffix_array(s)
    p = lcp_array(s, a)
    return n * (n + 1) // 2 - sum(p)


def repeated_substring_count(s):
    """Return the number of substrings that occurs more than once in a string.

    Related to the 'Repeated Substrings' problem on Kattis,
    https://open.kattis.com/problems/substrings.
    """
    a = suffix_array(s)
    p = lcp_array(s, a)
    k = p[0]
    for i in range(1, len(s)):
        if p[i] > p[i-1]:
            k += p[i] - p[i-1]
    return k
