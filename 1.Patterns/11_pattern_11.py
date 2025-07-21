"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

def pattern_11(n):
    for i in range(n):
        for j in range(i + 1):
            if (i + 1) % 2 == 0:
                print("0" if j % 2 == 0 else "1", end="")
            else:
                print("1" if j % 2 == 0 else "0", end="")
        print()

pattern_11(5)