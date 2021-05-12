# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

# ignore spaces
# if two characters have the same count, return first character
# distinguish lowercase and uppercase


def maxChar(input_string: str) -> str:
    # uses 'dictionary' data structure
    char_count = {}

    # get character counts
    for c in input_string:
        # skip empty spaces
        if c == ' ':
            continue
        try:
            char_count[c] += 1
        except:
            char_count[c] = 1

    # get character with highest count
    max_occurrence = ''
    max_count = 0

    for char in char_count:
        if char_count[char] > max_count:
            max_occurrence = char
            max_count = char_count[char]

    return max_occurrence
