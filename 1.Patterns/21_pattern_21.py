"""
******
*    *
*    *
*    *
*    *
******
"""

def pattern_21(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            spaces = " " * (n - 2)
            print("*" + spaces + "*")
            
pattern_21(8)
        