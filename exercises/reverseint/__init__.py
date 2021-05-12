# --- Directions
# Given an integer, return an integer that is the reverse
# ordering of numbers.
# --- Examples
#   reverseInt(15) === 51
#   reverseInt(981) === 189
#   reverseInt(500) === 5
#   reverseInt(-15) === -51
#   reverseInt(-90) === -9

# # Method 1
# def reverseInt(n: int) -> int:
#     # type conversion solution
#     negative = False
#     if n < 0:
#         negative = True
#         n = n*-1
    
#     reversed = ''
#     for c in str(n):
#         reversed = c + reversed

#     reversed = int(reversed)
#     reversed = reversed*-1 if negative else reversed

#     return reversed


# Method 2
def reverseInt(n: int) -> int:
    # doesn't use type conversion
    result = 0
    negative = True if n < 0 else False
    n = n*-1 if negative else n

    while n >= 10:
        result += (n%10)
        result = result*10
        n //= 10
    
    result += n
    result = result*-1 if negative else result

    return result
