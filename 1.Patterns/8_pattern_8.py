"""
*********
 *******
  *****
   ***
    *
"""

def pattern_8(n):
    for i in range(n):
        spaces = " " * i
        stars = "*" * (2 * (n - i) - 1)
        print(spaces + stars) 
        
pattern_8(5)