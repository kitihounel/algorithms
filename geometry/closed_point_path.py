"""Simple closed path. From https://geeksforgeeks.org/find-simple-closed-path-for-a-given-set-of-points."""
from functools import cmp_to_key

COLINEAR = 0
CLOCKWISE = 1
COUNTER_CLOCKWISE = 2

def orientation(p, q, r):
    v = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    return CLOCKWISE if v > 0 else COUNTER_CLOCKWISE if v < 0 else COLINEAR

def distance(p, q):
    dx, dy = p[0] - q[0], p[1] - q[1]
    return dx * dx + dy * dy

def closed_point_path(a):
    refPoint = min(a, key=lambda p: (p[1], p[0]))

    def compare(p, q):
        o = orientation(refPoint, p, q)
        if o == 0:
            return -1 if distance(refPoint, q) >= distance(refPoint, p) else 1
        return -1 if o == COUNTER_CLOCKWISE else 1

    return sorted(a, key=cmp_to_key(compare))
