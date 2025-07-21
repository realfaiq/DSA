"""
ABCDE
ABCD
ABC
AB
A
"""

def pattern_15(n):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
                 'X', 'Y', 'Z']
    for i in range(n, 0, -1):
        for j in range(i):
            print(alphabets[j], end="")
        print("")
        
pattern_15(5)