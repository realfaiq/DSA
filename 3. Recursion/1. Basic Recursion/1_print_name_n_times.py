def print_name_n_times(counter, n, name):
    if counter == n:
        return
    print(name)
    print_name_n_times(counter+1, n, name)
    

print_name_n_times(0, 5, "Faiq")