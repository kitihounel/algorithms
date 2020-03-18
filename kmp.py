"""KMP string matching algorithm

Code of prefix function from https://cp-algorithms.com/prefix-function.html
Code of KMP algorithm from https://www.geeksforgeeks/kmp-algorithm-for-pattern-searching/
"""

def compute_pi(s):
    p = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        j = p[i-1]
        while j > 0 and s[i] != s[j]:
            j = p[j-1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p

def kmp(text, pattern):
    p = compute_pi(pattern)
    i, j = 0, 0
    indexes = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            indexes.append(i-j)
            j = p[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = p[j-1]
            else:
                i += 1
        else:
            pass
    return indexes
