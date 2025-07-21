"""
*
**
***
****
*****
****
***
**
*
"""

def pattern_10(n):
    mid = (n + 1) // 2
    for i in range(mid):
        stars = "*" * (i + 1)
        print(stars)

    for j in range(mid - 1, 0, -1):
        stars = "*" * j
        print(stars)

pattern_10(9)