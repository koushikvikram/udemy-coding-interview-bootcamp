# --- Directions
# Write a function that returns the number of vowels
# used in a string.  Vowels are the characters 'a', 'e'
# 'i', 'o', and 'u'.
# --- Examples
#   vowels('Hi There!') --> 3
#   vowels('Why do you ask?') --> 4
#   vowels('Why?') --> 0


# method 1 - using set
def vowels(input_text: str) -> int:
    input_text = input_text.lower()

    all_vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = 0
    for char in input_text:  # O(n)
        if char in all_vowels:  # O(1) to check membership in set
            count += 1
    
    return count


# # method 2 - using dictionary
# def total(input_dict: dict) -> int:
#     result = 0
#     for k in input_dict:
#         result += input_dict[k]
#     return result

# def vowels(input_text: str) -> int:
#     input_text = input_text.lower()  # O(n)

#     # keep track of each vowel's count
#     vowels_count = {
#         'a': 0, 
#         'e': 0, 
#         'i': 0, 
#         'o': 0, 
#         'u': 0
#     }

#     for char in input_text:  # O(n)
#         try:
#             vowels_count[char] += 1
#         except:
#             pass
    
#     return total(vowels_count)  # O(n)


print(vowels("Why do you ask?"))
