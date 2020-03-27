def next_power_of_two(n):
    """Return the smallest power of 2 greater or equal to an integer."""
    return 1 if n <= 0 else n if not (n & (n - 1)) else 1 << n.bit_length()
