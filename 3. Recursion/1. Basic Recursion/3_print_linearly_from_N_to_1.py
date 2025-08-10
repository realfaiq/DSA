def print_linearly_from_N_to_1(n):
    if n < 1:
        return
    print(n, end="")
    print_linearly_from_N_to_1(n-1)
    
print_linearly_from_N_to_1(5)