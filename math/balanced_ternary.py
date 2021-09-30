def int_to_bt(x: int) -> str:
    """Convert an integer to its balanced ternary representation.

    The returned string contains only the symbols -(-1), 0(0), and +(1).

    For a good explaination on balanced ternary, read the following articles:
    - https://cp-algorithms.com/algebra/balanced-ternary.html
    - https://www.cis.upenn.edu/~matuszek/cit590-2015/Pages/balanced-ternary.html
    """
    symbols = ['0', '+', '-']

    flip = x < 0
    x = abs(x)
    digits = []
    while True:
        m = x % 3
        if m == 0 or m == 1:
            digits.append(m)
        else:
            digits.append(-1)
            x += 1
        x //= 3
        if x == 0:
            break
    digits.reverse()

    if flip:
        digits[:] = (d * -1 for d in digits)

    return ''.join(symbols[d] for d in digits)


if __name__ == "__main__":
    print("Testing balanced ternary function.")
    assert int_to_bt(64) == '+-+0+'
    assert int_to_bt(-64) == '-+-0-'
    assert int_to_bt(-5) == '-++'
    assert int_to_bt(237) == '+00-+0'
    assert int_to_bt(-237) == '-00+-0'
    print("Tests successfully passed.")
