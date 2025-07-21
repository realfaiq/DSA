"""
Problem Statement: Given an integer N, return the number of digits in N.
"""

def count_digits(n: int) -> int:
    count = 0
    for i in str(n):
        count += 1
    
    return int(count)

print(count_digits(12345))