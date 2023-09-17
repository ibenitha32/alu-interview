#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): the number of H characters desired in the file.

    Returns:
        int: the fewest number of operations needed, or 0 if n is not possible
        to achieve.

    """
    if not isinstance(n, int):
        return 0

    op = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            op += i
            i = 1
        i += 1
    return op
