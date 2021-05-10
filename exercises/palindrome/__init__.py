#  --- Directions
#  Given a string, return true if the string is a palindrome
#  or false if it is not.  Palindromes are strings that
#  form the same word if it is reversed. *Do* include spaces
#  and punctuation in determining if the string is a palindrome.
#  --- Examples:
#    palindrome("abba") === true
#    palindrome("abcdefg") === false


def palindrome(input_string: str) -> bool:
    # recursive solution
    if len(input_string) <= 1:
        return True
    if input_string[0] != input_string[-1]:
        return False
    return palindrome(input_string[1:-1])


# def palindrome(input_string: str) -> bool:
#     # iterative solution
#     raise NotImplementedError
