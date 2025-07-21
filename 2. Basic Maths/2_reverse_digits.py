"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

def reverse(x: int) -> int:
    reversed = ""
    str_x = str(x)
    negative = False
    if str_x[0] == "-":
        negative = True
    if not negative:
        for i in range(len(str_x) - 1, -1, -1):
            reversed += str_x[i]
    else:
        for i in range(len(str_x) - 1, 0, -1):
            reversed += str_x[i]
    
    if negative:
       reversed = "-" + reversed

    if int(reversed) > (2**31) - 1 or int(reversed) < -2**31:
        return 0
    else:
        return int(reversed)
            
print(reverse(1534236469))