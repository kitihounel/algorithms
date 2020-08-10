from collections import namedtuple
from sys import stdin, stderr

Interval = namedtuple("Interval", ["begin", "end", "index"])

def min_interval_cover(target, parts):
    """Minimum interval cover algorithm."""

    def first_true(iterable, default=False, pred=None):
        return next(filter(pred, iterable), default)

    # This handles the case of a point interval which is not
    # well handled by standard algorithm.
    if target.begin == target.end:
        pred = lambda p: p.begin <= target.begin <= p.end
        p = first_true(parts, None, pred)
        return (True, [p]) if p is not None else (False, [])

    lo, hi = target.begin, target.begin
    best, picked = -1, []
    for j, s in enumerate(parts):
        if s.begin <= lo:
            if s.end > hi:
                hi = s.end
                best = j
        else:
            if s.begin > hi:
                # It is impossible to cover the target interval.
                break
            if s.end <= hi:
                # The current interval lies inside [lo, hi] and is useless.
                continue
            # The current best interval belongs to the cover.
            picked.append(parts[best])
            lo, hi = parts[best].end, s.end
            best = j
        # Minor optimization. We stop as soon as we reach target interval end.
        if hi >= target.end:
            picked.append(parts[best])
            break

    return (True, picked) if hi >= target.end else (False, [])
