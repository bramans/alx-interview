#!/usr/bin/python3
""" Calculate Minimum Operations """

def minOperations(n):
    """
    Calculates the minimum number of operations needed to result in exactly
    n 'H' characters in the file, based on prime factorization logic without 
    separating the steps.
    
    Returns:
        The minimum number of operations as an integer.
        Returns 0 if n is less than or equal to 1.
    """
    if n < 2:
        return 0

    total_operations = 0
    divisor = 2

    while divisor <= n:
        # If divisor is a factor of n, reduce n by dividing and accumulate operations
        while n % divisor == 0:
            total_operations += divisor
            n //= divisor
        divisor += 1

    return total_operations

