#  --- Directions
#  Given a string, return true if the string is a palindrome
#  or false if it is not.  Palindromes are strings that
#  form the same word if it is reversed. *Do* include spaces
#  and punctuation in determining if the string is a palindrome.
#  --- Examples:
#    palindrome("abba") === true
#    palindrome("abcdefg") === false


# Method 1
def palindrome(input_string: str) -> bool:
    assert type(input_string) is str, "Input should be a string"
    # straightforward solution - reverse input and compare
    return input_string == input_string[::-1]


# # Method 2
# def palindrome(input_string: str) -> bool:
#     assert type(input_string) is str, "Input should be a string"
#     # recursive
#     if len(input_string) < 2:
#         return True
#     if input_string[0] != input_string[-1]:
#         return False
#     return palindrome(input_string[1:-1])


# # Method 3
# def palindrome(input_string: str) -> bool:
#     assert type(input_string) is str, "Input should be a string"
#     # iterative
#     if len(input_string) < 2:
#         return True
        
#     while len(input_string) >= 2:
#         if input_string[0] != input_string[-1]:
#             return False
#         input_string = input_string[1:-1]

#     return True


# # Method 4
# def palindrome(input_string: str) -> bool:
#     # xor solution - access only one character at a time from input
#     # reduce(lambda x,y:ord(x)^ord(y), input_string) won't work in place of loop 
#     # as previous result would be an int and it can't be converted to ASCII
#     assert type(input_string) is str, "Input should be a string"
#     if len(input_string) < 2:
#         return True

#     xor_result = 0
#     for c in input_string:
#         xor_result ^= ord(c)

#     middle_char = input_string[len(input_string)//2]
    
#     return (xor_result == 0) or (xor_result == ord(middle_char))
