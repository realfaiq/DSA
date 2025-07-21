"""
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.
"""

def armstrong_number(x: int) -> bool:
    str_x = str(x)
    power = len(str_x)
    total = 0
    for i in str_x:
        total += int(i) ** power
    
    if total == x:
        return True
    else:
        return False
    
print(armstrong_number(123))