def print_linearly_from_1_to_N_without_plus_1(counter, n):
    if counter < 1:
        return 
    print_linearly_from_1_to_N_without_plus_1(counter-1, n)
    print(counter, end="")
    
print_linearly_from_1_to_N_without_plus_1(5, 5)