"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *   
"""

def pattern_9(n):
    mid = (n + 1) // 2 

    # Top half of the diamond (pyramid)
    for i in range(mid):
        spaces = " " * (mid - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    # Bottom half of the diamond (inverted pyramid)
    for i in range(mid - 2, -1, -1):
        spaces = " " * (mid - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

pattern_9(9)