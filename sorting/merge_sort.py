"""Merge sort.

Code from https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#Python
"""


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # Change the direction of this comparison to change the direction of the sort.
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])

    return result


def merge_sort(ls):
    if len(ls) <= 1:
        return ls
 
    middle = len(ls) // 2
    left = ls[:middle]
    right = ls[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


if __name__ == '__main__':
    print('Testing merge function...')
    assert merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5]
    assert merge([1], [7, 8, 9]) == [1, 7, 8, 9]
    assert merge([9, 10, 11], [7, 8, 9]) == [7, 8, 9, 9, 10, 11]
    print('Tests successfully passed.')

    print('Testing merge sort function...')
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([1, 12, 7, 9, 8]) == [1, 7, 8, 9, 12]
    assert merge_sort([-1, 8, -9, -7, 10, 11]) == [-9, -7, -1, 8, 10, 11]
    print('Tests successfully passed.')
