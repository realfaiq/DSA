"""
6 6 6 6 6 6 6 6 6 6 6 
6 5 5 5 5 5 5 5 5 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 2 1 2 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 5 5 5 5 5 5 5 5 6 
6 6 6 6 6 6 6 6 6 6 6
"""

def pattern_22(n):
    size = 2 * n - 1
    for i in range(size):
        row = []
        for j in range(size):
            min_dist = min(i, j, size - 1 - i, size - 1 - j)
            val = n - min_dist
            row.append(str(val))
        print(" ".join(row))

    
pattern_22(6)