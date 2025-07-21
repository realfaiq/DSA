"""
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *
"""

def pattern_20(n):
    mid = (n * 2) // 2
    for i in range(mid - 1, -1, -1):
        spaces = " " * (i * 2)
        print("*" * (mid - i) + spaces + "*" * (mid - i))
        
    for j in range(1, mid + 1):
        spaces = " " * (j * 2)
        print("*" * (mid - j) + spaces + "*" * (mid - j))
        
pattern_20(6)