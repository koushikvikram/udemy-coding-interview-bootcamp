# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a pyramid shape
# with N levels using the # character.  Make sure the
# pyramid has spaces on both the left *and* right hand sides
# --- Examples
#   pyramid(1)
#       '#'
#   pyramid(2)
#       ' # '
#       '###'
#   pyramid(3)
#       '  #  '
#       ' ### '
#       '#####'


# # method 1
# def pyramid(N: int) -> None:
#     # for loop solution
#     for row in range(1, N+1):
#         steps = ''
#         start, end = N-(row-1), N+(row-1)
#         for column in range(1, 2*N):
#             # if column in range(start, end+1): # 'in' operation has O(n) runtime, comparison operation has O(1) runtime
#             if column >= start and column <= end:
#                 steps += '#'
#             else:
#                 steps += ' '
#         print(steps)


# # method 2
# def pyramid(N: int) -> None:
#     # while loop solution
#     row = 0
#     while row < N:
#         steps = ''
#         while len(steps) < 2*N-1:
#             # if len(steps) in range(N-row-1, N+row): # 'in' has O(n) runtime, comparison operator has O(1) runtime
#             if (len(steps) >= N-row-1) and (len(steps) <= N+row-1):
#                 steps += '#'
#             else:
#                 steps += ' '
#         print(steps)
#         row += 1
    

# method 3
def pyramid(N, row=0, steps=''):
    # recursive solution
    # base case
    if row == N:
        return
    # if len(steps) in range(N-row-1, N+row):  # replacing 'in' with comparison operator reduces time complexity from O(n) to O(1)
    if (len(steps) >= N-row-1) and (len(steps) <= N+row-1):
        steps += '#'
    else:
        steps += ' '
    # recursive case
    if len(steps) == 2*N-1:
        print(steps)
        row += 1
        return pyramid(N, row)
    return pyramid(N, row, steps)


pyramid(3)

# ---------------------------------------------------------------------------------------------------------------------------------
'''
The Process
-----------
1. Understand the problem, analyze it and explain in your own words
2. Check input and output types, check number of inputs and outputs
3. Come up with examples of inputs and expected outputs, edge cases
4. Strategy for solving the problem, patterns, data structures, algorithms
5. Pseudocode
6. Code + BUD optimization
'''

'''
1. Print a pyramid of 'N' rows using the character - '#'.
Make sure that there are spaces on both sides of the '#' when 'N' > 1
The last row will not have any spaces. It's length will be (2*N - 1) 
The penultimate row will have two spaces - one on either side 
The middle character of any row will be a '#'
Any character in the positions (N-1)-(row-1) to (N-1)+(row-1)+1 will be a '#', everything else will be a ' '

2. int -> None
single input, output printed, nothing returned

3. Eg. 
pyramid(1)
    '#'

pyramid(2)
    '#'
   '###'

pyramid(3)
    '#'
   '###'
  '#####'

4. strategy - could use loop/recursion
within each row, for indexes within range (N-1)-(row-1) to (N-1)+(row-1)+1, append '#' to string, else append ' '

5. pseudocode

pseudocode #1 - for loop
------------------------
for row in 1 to N
    create an empty string called steps
    for column in 1 to 2N-1
        if current index falls within range (N-1)-(row-1) to (N-1)+(row-1)+1, append '#' to steps
        else append ' ' to steps
    print steps


pseudocode #2 - while loop
--------------------------
row = 0
while row < N:
    steps = ''
    while len(steps) < 2*N-1:
        if len(steps) in range(N-row-1, N-row):
            steps += '#'
        else:
            steps += ' '
    print(steps)
    row += 1


pseudocode #3 - recursion
-------------------------
(N: int, row=0, steps='')
# base case
if row equals N
    terminate
if length of steps is in range N-row-1 and N+row-1
    append '#' to steps
else
    append ' ' to steps
# recursive case
if length of steps is lesser than 2*N - 1
    call function recursively with current version of steps
else
    print steps
    call function recursively with incremented row and default argument of steps 
'''
# ---------------------------------------------------------------------------------------------------------------------------------
