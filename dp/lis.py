from bisect import bisect_left


def lis(a):
    """Return indexes of items in the longest increasing subseq of the input list."""
    if len(a) == 0:
        return []

    previous = [-1]
    queue = [ a[0] ]
    indexes = [0]
    for j in range(1, len(a)):
        item = a[j]
        if item <= queue[0]:
            # New subsequence starts.
            queue[0] = item
            indexes[0] = j
            previous.append(-1)
        elif item > queue[-1]:
            # Current item extends the LIS..
            previous.append(indexes[-1])
            queue.append(item)
            indexes.append(j)
        else:
            # Current item replaces an item in a subseq, maybe the last element.
            # Note: the smaller is the last element in the LIS, the better it is.
            k = bisect_left(queue, item)
            previous.append(indexes[k-1])
            queue[k] = item
            indexes[k] = j

    j, result = indexes[-1], []
    while j != -1:
        result.append(j)
        j = previous[j]
    result.reverse()

    return result


if __name__ == '__main__':
    print('Testing lis function...')

    assert lis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert lis([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9]
    assert lis([5, 19, 5, 81, 50, 28, 29, 1, 83, 23]) == [0, 1, 5, 6, 8]
    
    print('Tests successfully passed.')
