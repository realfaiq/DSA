def print_linearly_from_N_to_1_backtracking(counter, n):
    if counter > n:
        return
    print_linearly_from_N_to_1_backtracking(counter+1, n)
    print(counter, end="")
    
print_linearly_from_N_to_1_backtracking(1, 5)
        