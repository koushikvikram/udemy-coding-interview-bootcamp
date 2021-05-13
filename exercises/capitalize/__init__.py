# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'


# Process
# 1. Capitalize the first letter of each word in the string
# 2. string -> string (capitalized), 1 input -> 1 output
# 3. '' -> '', 'a' -> 'A', 'hello' -> 'Hello', 'hi, how are you' -> 'Hi, How Are You'.
# What if there are no spaces, but just punctuations? -> not mentioned in the question, but just think about it
# eg. 'hi,how are you?' -> 'Hi,How Are You?'
# What about numbers and special characters? They can't be capitalized. -> again, not mentioned in the question, but think about it
# All these are unnecessary complications which we need not think about unless asked. 
# Our algorithm might not work for an example like johndoe@gmail.com
# 4. Strategy
# method 1 - split string on ' ', capitalize each word and join all words on ' '. 
# method 2 - How can this be done without using a list (and .split(' '))?
# loop over input string and if previous character is ' ', replace current character with it's capitalized version
# 5. pseudocode
# method 1
# words list = input string split on ' '
# loop over words
#   capitalize each word and assign back to words list
# join words in the list using ' ' and return the joint string
# 
# method 2
# initialize output string
# capitalize first letter of input string and append it output string
# loop over input string from 2nd character
#   if previous character is ' '
#       capitalize current character and append it to output string
#   else
#       append character to output string
# return output string


# # method 1
# def capitalize(input_str: str) -> str:
#     # works on empty strings too
#     words = input_str.split(" ")
    
#     for i in range(len(words)):
#         words[i] = words[i].capitalize()
    
#     return ' '.join(words)
    

# # method 2
# def capitalize(input_str: str) -> str:
#     # handle empty strings
#     if input_str == '':
#         return ''

#     output_str = ''
#     output_str += input_str[0].capitalize()
    
#     for i in range(1, len(input_str)):
#         if input_str[i-1] == ' ':
#             output_str += input_str[i].capitalize()
#         else:
#             output_str += input_str[i]
    
#     return output_str
        