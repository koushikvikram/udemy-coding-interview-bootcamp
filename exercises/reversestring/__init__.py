# --- Directions
# Given a string, return a new string with the reversed
# order of characters

# --- Examples
# reverse('apple') === 'leppa'
# reverse('hello') === 'olleh'
# reverse('Greetings!') === '!sgniteerG'


def reverse(input_string):
    output = ''

    for char in input_string:
        output = char + output

    return output
