#!/usr/bin/python3

""" Calculate Minimum Operations """

def min_steps(target_count):
    """
    In a text file, there is a single character 'H'. The text editor can perform
    two operations: Copy All and Paste. Given a number target_count, this method calculates
    the minimum number of operations required to achieve exactly target_count 'H' characters.
    
    Returns:
        An integer representing the minimum number of operations.
        If target_count is impossible to reach, returns 0.
    """
    if not isinstance(target_count, int):
        return 0

    total_operations = 0
    divisor = 2

    while divisor <= target_count:
        if target_count % divisor == 0:
            target_count //= divisor
            total_operations += divisor
            divisor = 1
        divisor += 1

    return total_operations

