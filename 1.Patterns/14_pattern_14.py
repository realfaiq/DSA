"""
A
AB
ABC
ABCD
ABCDE
"""

def pattern_14(n):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
                 'X', 'Y', 'Z']
    for i in range(n):
        for j in range(i+1):
            print(alphabets[j], end="")
        print("")
        
pattern_14(5)