def lswrc(s):
    """Compute length of the longest substring without repeated characters.

    The returned object is a tuple with two elements. The first element is
    the start index of the left most substring that fulfills the condition
    and the second element is the length of the substring.
    """
    seen = {}
    best_length, current_length = 0, 0
    best_substr_start, current_start = 0, 0

    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= current_start:
            current_start = seen[ch] + 1
            current_length = i - current_start + 1
        else:
            current_length += 1

        if current_length > best_length:
            best_length = current_length
            best_substr_start = current_start

        seen[ch] = i

    return best_substr_start, best_length


if __name__ == '__main__':
    print('Testing lswrc function...')

    assert lswrc('abcabcdc') == (3, 4)
    assert lswrc('bbbb') == (0, 1)
    assert lswrc('abcdefgh') == (0, 8)
    assert lswrc('abcdebakpqrst') == (2, 11)
    assert lswrc('kakacfgdkakacfgdmnopqrstuvvvvvvvvvvv') == (10, 16)
    assert lswrc('uuuuuuuuuuuuuuuuvvvvvvvvvv') == (15, 2)

    print('Tests successfully passed.')
