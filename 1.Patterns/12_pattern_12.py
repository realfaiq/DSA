"""
1    1
12  21
123321
"""

def pattern_1(n):
    for i in range(1, n + 1):
        left = ''.join(str(j) for j in range(1, i + 1))
        spaces = ' ' * (2 * (n - i))
        right = ''.join(str(j) for j in range(i, 0, -1))
        print(left + spaces + right)

pattern_1(3)
