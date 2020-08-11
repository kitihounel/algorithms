"""Sqrt decomposition. From https://iq.opengenus.org/range-minimum-query-square-root-decomposition/"""
from math import ceil, sqrt
from operator import floordiv

def build(a, fn):
    n = len(a)
    k = ceil(sqrt(n))
    m = floordiv(n, k) + (1 if n % k != 0 else 0)
    buckets = [0 for _ in range(m)]
    ptr = -1
    for i in range(n):
        if i % k == 0:
            ptr += 1
            buckets[ptr] = a[i]
        else:
            buckets[ptr] = fn(buckets[ptr], a[i])
    return buckets

def update(a, i, value, buckets, fn):
    # To make the update funtion work with any function,
    # it runs in O(sqrt(N)) instead of O(1).
    n = len(a)
    k = ceil(sqrt(n))
    ptr = floordiv(i, k)
    lo = ptr * k
    hi = min(lo + k, n) - 1
    if i == lo == hi:
        buckets[ptr] = value
    else:
        if i == lo:
            tmp = query(a, lo+1, hi, buckets, fn)
        elif i == hi:
            tmp = query(a, lo, hi-1, buckets, fn)
        else:
            u = query(a, lo, i-1, buckets, fn)
            v = query(a, i+1, hi, buckets, fn)
            tmp = fn(u, v)
        buckets[ptr] = fn(tmp, value)
    a[i] = value

def query(a, l, r, buckets, fn):
    k = ceil(sqrt(len(a))) 
    ans = a[l]
    l += 1
    while l < r and l % k != 0 and l != 0:
        ans = fn(ans, a[l])
        l += 1
    while l + k <= r:
        i = floordiv(l, k)
        ans = fn(ans, buckets[i])
        l += k
    while l <= r:
        ans = fn(ans, a[l])
        l += 1
    return ans
