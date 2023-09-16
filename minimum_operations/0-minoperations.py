#!/usr/bin/python3
""" Minimum operations Repo - ALU Interview Project """

def minOperations(n):
    """Return the fewest number of operations needed."""
    if n == 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations

