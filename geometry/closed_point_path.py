"""Simple closed path. Adapted from https://geeksforgeeks.org/find-simple-closed-path-for-a-given-set-of-points."""
from functools import cmp_to_key
from operator import itemgetter


COLINEAR, CLOCKWISE, COUNTER_CLOCKWISE = 0, 1, -1


def orientation(p, q, r):
    v = (r[1] - q[1]) * (q[0] - p[0]) - (q[1] - p[1]) * (r[0] - q[0])
    return COUNTER_CLOCKWISE if v > 0 else CLOCKWISE if v < 0 else COLINEAR


def distance(p, q):
    dx, dy = p[0] - q[0], p[1] - q[1]
    return dx * dx + dy * dy


def closed_point_path(points: list):
    lo_point = min(points, key=itemgetter(1, 0))

    def cmp(p, q):
        o = orientation(lo_point, p, q)
        return o if o != COLINEAR else distance(lo_point, p) - distance(lo_point, q)

    return sorted(points, key=cmp_to_key(cmp))


if __name__ == '__main__':
    print('Testing convex hull function...')
    
    points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    path = [(0, 0), (3, 1), (1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (0, 3)]
    assert closed_point_path(points) == path

    points = [(3, 2), (1, 1), (1, 2), (3, 1)]
    path = [(1, 1), (3, 1), (3, 2), (1, 2)]
    assert closed_point_path(points) == path

    points = [(0, 10), (0, 15), (0, -15), (0, -25), (0, 7)]
    assert closed_point_path(points) == sorted(points)

    points = [(0, -15), (0, -25), (0, 7), (3, -20), (-5, 7)]
    path = [(0, -25), (3, -20), (0, -15), (0, 7), (-5, 7)]
    assert closed_point_path(points) == path

    print('Tests successfully passed.')
