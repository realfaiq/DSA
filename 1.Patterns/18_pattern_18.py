"""
E
D E
C D E
B C D E
A B C D E
"""

def pattern_n(n):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
                 'X', 'Y', 'Z']
    for i in range(n):
        index = n - i
        print(' '.join(alphabets[j-1] for j in range(index, n+1)))
        

pattern_n(5)