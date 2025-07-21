"""
    *
   ***
  ***** 
 ******* 
*********
"""

def pattern_7(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
        
pattern_7(5)