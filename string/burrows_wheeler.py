from operator import floordiv as div

class Shift:
    def __init__(self, index, s):
        self.index = index
        self.string = s
        self.rank = (-1, -1)

    def __lt__(self, other):
        if not isinstance(other, Shift):
            raise Exception("Invalid argument for comparison with Shift")
        return self.rank < other.rank

def sorted_cyclic_shifts(s):
    """Sort all cyclic shifts of a string.

    Code adapted from http://cp-algorithms.com/string/suffix-array.html.
    """
    n = len(s)
    shifts = [Shift(j, s) for j in range(n)]
    ranks = [ord(c) for c in s]
    length, limit = 1, 2 * n
    while length < limit:
        h = div(length, 2)
        for shift in shifts:
            x = ranks[shift.index]
            y = ranks[(shift.index + h) % n]
            shift.rank = (x, y)
        shifts.sort()

        rank = 0
        ranks[shifts[0].index] = rank
        for j in range(1, n):
            previous, current = shifts[j-1], shifts[j]
            if previous.rank != current.rank:
                rank += 1
            ranks[current.index] = rank

        length *= 2

    return [shift.index for shift in shifts]

def bwt(s):
    """Burrows-Wheeler transform."""
    shifts = sorted_cyclic_shifts(s)
    t = "".join(s[j-1] for j in shifts)
    return t, shifts.index(0)

class InvBwtMatrixRow():
    def __init__(self):
        self.string = ""
        self.rank = None

    def __lt__(self, other):
        if not isinstance(other, InvBwtMatrixRow):
            raise Exception("Invalid object for comparison with InvBwtMatrixRow")
        return self.rank < other.rank

def inverse_bwt(s, k):
    """Burrows-Wheeler transform. Don't use it because it is not efficient."""
    n = len(s)
    rows = [InvBwtMatrixRow() for _ in range(n)]
    ranks = [-1 for _ in range(n)]
    for _ in range(n):
        for j, c in enumerate(s):
            rows[j].string = c + rows[j].string
            rows[j].rank = (ord(c), ranks[j])
        rows.sort()
        ranks[0] = 0
        for j in range(1, n):
            ranks[j] = ranks[j-1] + (1 if rows[j-1].rank != rows[j] else 0)

    return rows[k].string
