from functools import cmp_to_key
from operator import itemgetter


COLINEAR, COUNTER_CLOCKWISE, CLOCKWISE = 0, -1, 1


def orientation(a, b, c):
    v = (c[1] - b[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - b[0])
    return COUNTER_CLOCKWISE if v > 0 else CLOCKWISE if v < 0 else COLINEAR


def distance(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2   


def lowest_point_index(points: list):
    j = 0
    key = itemgetter(1, 0)
    for i in range(1, len(points)):
        if key(points[i]) < key(points[j]):
            j = i
    return j


def make_cmp(lo_point):
    """Create comparison fn used in convex hull fn to sort points by polar angle."""
    def cmp(p, q):
        o = orientation(lo_point, p, q)
        return o if o != 0 else distance(lo_point, p) - distance(lo_point, q)
    return cmp 


def convex_hull(points: list):
    """Find convex hull of a given set of 2d-points.
    
    The list should contain at least three points and there should be no duplicate.
    Each point is a tuple of two integers.
    """
    i = lowest_point_index(points)
    points[0], points[i] = points[i], points[0]
    lo_point = points[0]
    cmp = make_cmp(lo_point)
    points.sort(key=cmp_to_key(cmp))

    a = [lo_point]
    for j in range(1, len(points) - 1):
        if orientation(lo_point, points[j], points[j+1]) != COLINEAR:
            a.append(points[j])
    a.append(points[-1])

    if len(a) <= 3:
        return a

    h = [a[0], a[1], a[2]]
    for j in range(3, len(a)):
        p = a[j]
        while len(a) > 1 and orientation(h[-2], h[-1], p) != COUNTER_CLOCKWISE:
            h.pop()
        h.append(p)

    return h
