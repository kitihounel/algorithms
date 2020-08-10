"""Sqrt decomposition. From https://iq.opengenus.org/range-minimum-query-square-root-decomposition/"""
from math import ceil, sqrt
from operator import floordiv

def build(arr, fn):
    n = len(arr)
    k = ceil(sqrt(n))
    m = floordiv(n, k) + (1 if n % k != 0 else 0)
    feed = [0 for _ in range(m)]
    pointer = -1
    for i in range(n):
        if i % k == 0:
            pointer += 1
            feed[pointer] = arr[i]
        else:
            feed[pointer] = fn(feed[pointer], arr[i])
    return feed

def update(arr, i, value, updValue, feed, fn):
    k = ceil(sqrt(len(arr)))
    pointer = floordiv(i, k)
    feed[pointer] = fn(updValue, feed[pointer])
    arr[i] = value

def query(arr, l, r, feed, fn):
    k = ceil(sqrt(len(arr))) 
    ans = arr[l]
    l += 1
    while l < r and l % k != 0 and l != 0:
        ans = fn(ans, arr[l])
        l += 1
    while l + k <= r:
        i = floordiv(l, k)
        ans = fn(ans, feed[i])
        l += k
    while l <= r:
        ans = fn(ans, arr[l])
        l += 1
    return ans
