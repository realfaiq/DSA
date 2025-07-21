"""
   A  
  ABA 
 ABCBA
ABCDCBA
"""

def pattern_17(n):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
                 'X', 'Y', 'Z']
    for i in range(n):
        spaces = " " * ((n - i) - 1)
        print(spaces + ''.join(alphabets[j] for j in range(i+1)) + ''.join(alphabets[j] for j in range(i-1, -1, -1)))        
        
pattern_17(4)        