"""
A
BB
CCC
DDDD
EEEEE
"""

def pattern_16(n):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
                 'X', 'Y', 'Z']
    for i in range(n):
        for j in range(i+1):
            print(alphabets[i], end="")
        print("")

pattern_16(5)    