def merge(left, right):
    """Merge two sorted lists.

    Return a tuple with two elements:
        - the merged list and,
        - the number of swap of two adjacent elements needed to achieve the result.
    """
    result = []
    left_idx, right_idx = 0, 0
    n = 0
    while left_idx < len(left) and right_idx < len(right):
        # Change the direction of this comparison to change the direction of the sort.
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
            n += len(left) - left_idx
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])

    return result, n


def swap_count(ls):
    """Sort a list and count the number of swap of adjacent elements needed using mergesort.
    """
    if len(ls) <= 1:
        return 0

    middle = len(ls) // 2
    left = ls[:middle]
    right = ls[middle:]

    n = swap_count(left) + swap_count(right)
    m, k = merge(left, right)
    ls[:] = m[:]

    return n + k


if __name__ == '__main__':
    print('Testing swap count function...')
    assert swap_count([1, 0, 2, 1, 0]) == 5
    assert swap_count([1, 2, 3, 4, 5]) == 0
    assert swap_count([1, 2, 3, 4, 5, 1]) == 4
    assert swap_count([1, 2, 3, 1, 2, 3]) == 3
    print('Tests successfully passed.')
