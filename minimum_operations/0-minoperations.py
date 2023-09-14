#!/usr/bin/python3
""" Minimum operations Repo - ALU Interview Project """

import math

def min_operations(n):
  """
  Calculates the fewest number of operations needed to result in exactly n H characters in the file.

  Args:
    n: The number of H characters to be achieved.

  Returns:
    The fewest number of operations needed.
  """

  if n <= 1:
    return 0

  operations = 0
  for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
      ops += i
      n //= i

  if n > 1:
    operations += n

  return operations

