# Balanced ternary explanations

The conversion algorithm given in `balanced-ternary.md` and the function in `balanced-ternary.md`
may not look similar, but they do the same job.

## Explanation of the algorithm in `balanced-ternary.md`

The algorithm replaces $2$ by $-1$ and adds $1$ to the next position. In the same way,
it replaces $3$ by $0$ and adds $1$ to the next position. When we replace $2$ by $-1$ at position
$i$, we remove $3 * 3^i = 3^{i+1}$ from the number. And when we replace
$3$ by $0$ we remove $3 * 3^i = 3^{i+1}$. So when we add $1$ to the digit at position $i+1$,
we simply balance things out because we simply add $3^{i+1}$ to the number again.

## Explanation of the algorithm in `balanced-ternary.md`

The function implemented `balanced-ternary.md` looks like this:

```python
def int_to_bt(x):
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
```

The part of the function that made me scratch my head for a moment is:

```python
if x % 3 == 2:
    digits.append(-1)
    x += 1
```

$x \equiv 2\ mod\ 3$ means two things:
- $x = 3 * q + 2$, with $q = \lfloor x \div 3 \rfloor$ and
- $y = x + 1$ is a multiple of $3$ and $y \div 3 = q + 1$.

What is hidden behind the code is: $3 * (q + 1) - 1 = 3 * q + 3 - 1 = 3 * q + 2$.
