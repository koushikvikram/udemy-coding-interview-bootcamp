# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False


# def get_char_counts(input_str: str) -> dict:
#     char_counts = {}

#     for c in input_str:
#         if c.isalnum():
#             try:
#                 char_counts[c] += 1
#             except:
#                 char_counts[c] = 1
    
#     return char_counts


# def compare_dicts(d1: dict, d2: dict) -> bool:
#     if len(d1) != len(d2):
#         return False
    
#     for k in d1:
#         try:
#             if d1[k] != d2[k]:
#                 return False
#         except:
#             return False
    
#     return True


# def anagrams(input1: str, input2: str) -> bool:
#     # convert to lowercase so that uppercase and lowercase letters are considered the same
#     input1 = input1.lower() 
#     input2 = input2.lower()

#     char_counts_input1 = get_char_counts(input1)
#     char_counts_input2 = get_char_counts(input2)

#     # return char_counts_input1 == char_counts_input2  # can be used instead of compare_dicts
#     return compare_dicts(char_counts_input1, char_counts_input2)


# method 2
from typing import List


def clean_string(input_str: str) -> str:
    output_str = ''

    for c in input_str:
        if c.isalnum():
            output_str += c
    
    return output_str


def compare_chars(input1: List[str], input2: List[str]) -> bool:
    if len(input1) != len(input2):
        return False
    
    # return input1 == input2 
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            return False
    
    return True


def anagrams(input1: str, input2: str) -> bool:
    # using sort and compare
    input1 = input1.lower()
    input2 = input2.lower()

    input1 = clean_string(input1)
    input2 = clean_string(input2)

    # sorted('cab') -> ['a', 'b', 'c']
    input1 = sorted(input1)
    input2 = sorted(input2)

    return compare_chars(input1, input2)
