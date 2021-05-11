# --- Directions
# Given a string, return a new string with the reversed
# order of characters

# --- Examples
# reverse('apple') === 'leppa'
# reverse('hello') === 'olleh'
# reverse('Greetings!') === '!sgniteerG'

from functools import reduce


# method 1
def reverse(input_string: str) -> str:
    assert type(input_string) is str, 'Input should be of type string'
    output = ''
    
    # loop over input and append each character in front
    for char in input_string:
        output = char + output

    return output


# # method 2
# def reverse(input_string: str) -> str:
#     '''works only when input string is at least 2 characters long'''
#     assert type(input_string) is str, 'Input should be of type string'
#     if len(input_string) < 2:
#         raise Exception("input string should be at least 2 characters long")

#     return reduce(lambda x,y:y+x, list(input_string))


# # method 3
# def reverse(input_string: str) -> str:
#     '''using indexing'''
#     assert type(input_string) is str, 'Input should be of type string'
#     return input_string[::-1]   
