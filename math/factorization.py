from operator import floordiv

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = floordiv(n, 2)
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n = floordiv(n, f)
        f += 2
    if n != 1:
        factors.append(n)
    return factors
