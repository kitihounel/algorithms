from itertools import product

def coin_change(amount, coins):
    """Find a solution to an instance of the coin change problem.

    The coins should preferably be sorted in ascending order.
    Code adapted from an UCT course about dynamic programming.
    """
    inf = 10 ** 9
    counts = [inf for _ in range(amount+1)]
    coinUsed = [-1 for _ in range(amount+1)]

    counts[0] = 0
    for value, coin in product(range(1, amount+1), coins):
        j = value - coin
        if j >= 0 and counts[j] < counts[value]:
            counts[value] = counts[j] + 1
            coinUsed[value] = coin

    ans = []
    if counts[amount] != inf:
        i = amount
        while i > 0:
            ans.append(coinUsed[i])
            i -= coinUsed[i]

    return ans
