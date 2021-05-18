# --- Directions
# Write a function that accepts an integer N
# and returns a NxN spiral matrix.
# --- Examples
#   matrix(2)
#     [[1, 2],
#     [4, 3]]
#   matrix(3)
#     [[1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]]
#  matrix(4)
#     [[1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7]]


# ------------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------- Solution 1 --------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------- #


"""
def zero_matrix(n):
    '''creates a matrix of zeros of dimension nxn'''
    output_matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        output_matrix.append(row)

    return output_matrix


def step(canvas, direction, i, j, n):
    '''Returns the index of the next step in the current direction. 
    If not possible, turn right and return index of next step'''
    turn_right = {
        'front': 'down', 
        'down': 'back', 
        'back': 'up',
        'up': 'front'
        }
    new_indices = {
        'front': (i, j+1),
        'back': (i, j-1),
        'up': (i-1, j),
        'down': (i+1, j)
        }
    
    new_i, new_j = new_indices[direction]

    # if next step is out of bounds or if next step is not 0 (i.e. the position has already been traversed),
    # turn right and take next step
    if new_i >= n or new_j >= n or canvas[new_i][new_j]!=0:
        direction = turn_right[direction]
        new_i, new_j = new_indices[direction]
    
    return (new_i, new_j, direction)


def matrix(n):
    '''Our main function. Returns a spiral matrix.'''
    assert n > 0, 'n should be greater than 0'
    # create a matrix of zeros
    canvas = zero_matrix(n)
    
    # set initial direction
    direction = 'front'
    
    # set initial index and initial value
    i, j = 0, 0
    canvas[i][j] = 1
    
    # traverse the canvas and set values
    # by using a for loop instead of while, we're avoiding the termination condition
    for value in range(2, n*n + 1):
        i, j, direction = step(canvas, direction, i, j, n)
        canvas[i][j] = value

    return canvas
    

def print_spiral_matrix(n):
    spiral_matrix = matrix(n)
    for row in spiral_matrix:
        str_row = [str(char) for char in row]
        print('\t'.join(str_row))


print_spiral_matrix(4)
"""


# ---------------------------------------------------------------------------------------------------------------------------------
'''
The Process

1. Understand the problem, analyze it and explain it in your own words
Traversing the matrix in a spiral means turning right once the end is reached.
End here means end of row/column or an already traversed position in the matrix

2. Inputs and Outputs
int -> List[List[int]]
1 input, 1 output
output should be of dimension (input x input)

3. Examples and Edge Cases
input should be >= 1
eg. matrix(2) -> [[1, 2],
                  [4, 3]]
    
    matrix(3) -> [[1, 2, 3],
                  [8, 9, 4],
                  [7, 6, 5]]

4. Strategy
There are n*n values in the matrix in total
loop over these values and step through the matrix in a spiral order to set these values at the correct positions

5. Pseudocode
We'll start with a zero matrix of dimension (input x input)
We'll start at position (0, 0) and set it to 1
We'll set the starting direction as 'front'
The, we'll loop from values 2 to n*n
    take a step in the current direction and set that location's value as current index of loop
    if it's not possible to take a step in the current direction or if the value in the next step is already filled,
    change direction, take a step and set value
'''


# ------------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------- Solution 2 --------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------- #

'''
Pseudocode
----------
Create empty array of arrays called 'results'
Create a counter variable starting at 1
As long as (start column <= end column) AND (start row <= end row)
    # side 1 - top row
    loop from start column to end column
        at results[start_row][i] assign counter variable
        increment counter
    increment start row
    
    # side 2 - right column
    loop from start row to end row
        at results[i][end_column] assign counter variable
        increment counter
    decrement end column

    # side 3 - bottom row
    loop from end column to start column
        at results[end_row][i] assign counter variable
        increment counter
    decrement end row

    # side 4 - left column
    loop from end row to start row
        at results[i][start_column] assign counter variable
        increment counter
    increment start column
'''


def matrix(n):
    results = []

    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        results.append(row)

    counter = 1
    start_column, end_column = 0, n-1
    start_row, end_row = 0, n-1

    while (start_column <= end_column) and (start_row <= end_row):
        # top row
        for i in range(start_column, end_column+1):
            results[start_row][i] = counter
            counter += 1
        start_row += 1

        # right column
        for i in range(start_row, end_row+1):
            results[i][end_column] = counter
            counter += 1
        end_column -= 1

        # bottom row
        for i in range(start_column, end_column+1)[::-1]:
            results[end_row][i] = counter
            counter += 1
        end_row -= 1

        # left column
        for i in range(start_row, end_row+1)[::-1]:
            results[i][start_column] = counter
            counter += 1
        start_column += 1

    return results


print(matrix(4))
