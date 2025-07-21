"""
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************
"""

def pattern_19(n):
    mid = (n*2) // 2
    for i in range(mid):
        spaces = " " * i * 2 
        print("*" * (mid - i) + spaces + ("*" * (mid - i)))
    
    for j in range(mid - 1, -1, -1):
        spaces = " " * j * 2 
        print("*" * (mid - j) + spaces + ("*" * (mid - j)))
    
pattern_19(6)
