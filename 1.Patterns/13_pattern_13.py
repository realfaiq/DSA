"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

def pattern_13(n):
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" ".join(row))

pattern_13(5)