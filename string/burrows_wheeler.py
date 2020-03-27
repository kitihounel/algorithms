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

def next_power_of_two(n):
    """Return the smallest power of 2 greater or equal to an integer."""
    return 1 if n <= 0 else n if not (n & (n - 1)) else 1 << n.bit_length()

def sorted_cyclic_shifts(s):
    """Sort all cyclic shifts of a string.

    Code adapted from http://cp-algorithms.com/string/suffix-array.html.
    """
    n = len(s)
    shifts = [Shift(j, s) for j in range(n)]
    ranks = [ord(c) for c in s]
    maxLength = next_power_of_two(n)
    chunkLength = 1
    while chunkLength <= maxLength:
        h = div(chunkLength, 2)
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

        chunkLength *= 2

    return [shift.index for shift in shifts]

def burrows_wheeler(s):
    """Burrows-Wheeler transform."""
    a = sorted_cyclic_shifts(s)
    return "".join(s[j-1] for j in a)
