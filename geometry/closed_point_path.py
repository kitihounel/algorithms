"""Simple closed path. From https://geeksforgeeks.org/find-simple-closed-path-for-a-given-set-of-points."""
from functools import cmp_to_key
from operator import itemgetter

COLINEAR, CLOCKWISE, COUNTER_CLOCKWISE = 0, 1, 2


def orientation(p, q, r):
    v = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    return CLOCKWISE if v > 0 else COUNTER_CLOCKWISE if v < 0 else COLINEAR


def distance(p, q):
    dx, dy = p[0] - q[0], p[1] - q[1]
    return dx * dx + dy * dy


def closed_point_path(a):
    lo_point = min(a, key=itemgetter(1, 0))

    def cmp(p, q):
        o = orientation(lo_point, p, q)
        if o == 0:
            return -1 if distance(lo_point, q) >= distance(lo_point, p) else 1
        return -1 if o == COUNTER_CLOCKWISE else 1

    return sorted(a, key=cmp_to_key(cmp))
