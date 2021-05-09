# --- Directions
# Given a string, return a new string with the reversed
# order of characters

# --- Examples
# reverse('apple') === 'leppa'
# reverse('hello') === 'olleh'
# reverse('Greetings!') === '!sgniteerG'


def reverse(input_string: str) -> str:
    output = ''
    # loop over input and append each character in front
    for char in input_string:
        output = char + output

    return output
