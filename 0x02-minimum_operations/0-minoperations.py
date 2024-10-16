#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
	"""Calculates the fewest number of operations needed
        to result in exactly n H characters in the file"""
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
        
        # Optimization: If factor > sqrt(n), n must be prime
        if factor * factor > n:
            if n > 1:
                operations += n
            break
    
    return operations
