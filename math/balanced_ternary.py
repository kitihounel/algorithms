def balanced_ternary(n: int):
    flip = False
    if n < 0:
        flip = True
        n *= -1

    digits = []
    while True:
        m = n % 3
        if m == 0 or m == 1:
            digits.append(m)
        else:
            digits.append(-1)
            n += 1
        n //= 3
        if n == 0:
            break
    if flip:
        digits = [d * -1 for d in digits]
    return digits

if __name__ == "__main__":
    print("Testing balanced ternary function.")
    assert balanced_ternary(64) == [1, 0, 1, -1, 1]
    assert balanced_ternary(237) == [0, 1, -1, 0, 0, 1]
    assert balanced_ternary(-5) == [1, 1, -1]
    print("Tests successfully passed.")
