"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

def palindrome(x: int) -> bool:
    reversed = ""
    str_x = str(x)
    if str_x[0] == "-":
        return False
    for i in range(len(str_x) - 1, -1, -1):
        reversed += str_x[i]
    
    if int(reversed) == x:
        return True
    else:
        return False

print(palindrome(-654))