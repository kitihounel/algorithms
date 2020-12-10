def rexp(b, e):
    """Fast exponentiation, recursive version.

    This function is based on the fact that a^b = a^(b/2) * a^(b/2) * (a if b is odd else 0).
    """
    if e == 0 or b == 1:
        return 1
    elif b == 0:
        return 0 
    else:
        q, m = divmod(e, 2)
        p = rexp(b, q)
        return p * p * (b if m == 1 else 1) # The expression in braces can be replaced by (b ** m)

def iexp(b, e):
    """Fast exponentiation, iterative version.

    This function uses the binary representation of the exponent to work.
    For example, suppose that we want to compute b^13.
    We know that 13 = 8 + 4 + 1. So b^13 = b^8 * b^4 * b^1.
    Then, all we have to do is to compute the binary representation of the exponent (e)
    and use the powers of b that correspond to the bits set to 1.
    """
    acc, p = b, 1
    while e != 0:
        q, r = divmod(e, 2)
        if r == 1:
            p *= acc
        e, acc = q, acc * acc
    return p

# When trying to understand this algorithm, GeeksForGeeks article about modular exponentation helped us.
def mod_exp(b, e, m):
    """Modular exponentiation."""
    acc, p = b, 1
    while e != 0:
        q, r = divmod(e, 2)
        if r == 1:
            p = (p * acc) % m
        e = q
        acc = acc * acc % m
    return p

if __name__ == "__main__":
    print("Testing exponentiation function.")
    assert rexp(10, 5) == iexp(10, 5) == pow(10, 5)
    assert rexp(7, 3) == iexp(7, 3) == pow(7, 3)
    assert rexp(2, 12) == iexp(2, 12) == pow(2, 12)
    assert rexp(0, 12) == iexp(0, 12) == pow(0, 12)
    assert rexp(11, 0) == iexp(11, 0) == pow(11, 0)
    assert rexp(145211, 2048) == iexp(145211, 2048) == pow(145211, 2048)
    print("Tests successfully passed.")
    print("Testing modular exponentiation function")
    assert mod_exp(10, 5, 7) == pow(10, 5, 7)
    assert mod_exp(7, 3, 4) == pow(7, 3, 4)
    assert mod_exp(2, 12, 2) == pow(2, 12, 2)
    assert mod_exp(0, 12, 124) == pow(0, 12, 124)
    assert mod_exp(11, 0, 6) == pow(11, 0, 6)
    assert mod_exp(145211, 785, 678521) == pow(145211, 785, 678521)
    assert mod_exp(6342545211, 774585, 1000000009) == pow(6342545211, 774585, 1000000009)
    print("Tests successfully passed.")
