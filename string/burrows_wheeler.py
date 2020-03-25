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
    length = 1
    while length < n:
        for shift in shifts:
            m = div(length, 2)
            x = ranks[shift.index]
            y = ranks[(shift.index + m) % n]
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

def burrows_wheeler(s):
    """Burrows-Wheeler transform."""
    a = sorted_cyclic_shifts(s)
    return "".join(s[j-1] for j in a)