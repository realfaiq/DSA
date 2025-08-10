def print_linearly_1_to_N(counter, n):
    if counter > n:
        return
    print(counter, end="")
    print_linearly_1_to_N(counter+1, n)
    
print_linearly_1_to_N(1, 5)