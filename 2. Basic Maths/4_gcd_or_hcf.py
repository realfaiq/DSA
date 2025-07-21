"""
Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

The Greatest Common Divisor of any two integers is the largest number that divides both integers.
"""

def gcd(n1: int, n2: int) -> int:
    greater = n2
    divisor = 0
    if n1 > n2:
        greater = n1
    for i in range(1, greater):
        if n1%i == 0 and n2%i == 0:
            divisor = i
    
    return divisor

print(gcd(20, 15))