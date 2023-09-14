#!/usr/bin/python3
"""Minimum Operations - Alu-interview"""

import math

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required to achieve n H characters.
             If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0

    # Iterate through numbers from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            operations += i
            n //= i

    # If n is still greater than 1, add it to operations
    if n > 1:
        operations += n

    return operations

# Example usage:
if __name__ == "__main__":
    n = 9
    result = minOperations(n)
    print(f"Number of operations to achieve {n} H characters: {result}")
