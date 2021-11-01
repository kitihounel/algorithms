from functools import cmp_to_key
from operator import itemgetter


COLINEAR, COUNTER_CLOCKWISE, CLOCKWISE = 0, -1, 1


def orientation(a, b, c):
    v = (c[1] - b[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - b[0])
    return COUNTER_CLOCKWISE if v > 0 else CLOCKWISE if v < 0 else COLINEAR


def distance(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def make_cmp(lo_point):
    """Create comparison fn used in convex hull fn to sort points by polar angle."""
    def cmp(p, q):
        o = orientation(lo_point, p, q)
        return o if o != 0 else distance(lo_point, p) - distance(lo_point, q)
    return cmp 


def convex_hull(points: list):
    """Find convex hull of a given set of 2d-points using Graham scan.
    
    The list should contain at least three points and there should be no duplicate.
    Each point is a tuple of two integers.
    """
    lo_point = min(points, key=itemgetter(1, 0))
    cmp = make_cmp(lo_point)
    points.sort(key=cmp_to_key(cmp))
    assert lo_point is points[0]

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


if __name__ == '__main__':
    print('Testing convex hull function...')
    
    points = [(-51, -6), (-30, -34), (-24, -74), (41, -6), (73, 17)]
    assert convex_hull(points) == [(-24, -74), (73, 17), (-51, -6)]

    points = [
        (-9, -3), (-4, -6), (-4, -2), (-3, -9), (-3, 15), (0, 6), (0, 11),
        (3, -4), (3, 16), (5, 19), (12, 13), (12, 17), (16, -7), (16, -3),
        (16, 3), (16, 6), (17, -4), (17, 5), (19, -8)
    ]
    h = [(-3, -9), (19, -8), (17, 5), (12, 17), (5, 19), (-3, 15), (-9, -3)]
    assert convex_hull(points) == h

    points = [(0, 0), (0, 3), (1, 1), (1, 2), (2, 2), (3, 1), (3, 3), (4, 4)]
    assert convex_hull(points) == [(0, 0), (3, 1), (4, 4), (0, 3)]

    print('Tests successfully passed.')
