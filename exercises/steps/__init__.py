# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
#   steps(2)
#       '# '
#       '##'
#   steps(3)
#       '#  '
#       '## '
#       '###'
#   steps(4)
#       '#   '
#       '##  '
#       '### '
#       '####'


# assume n >= 1


# # method 1
# def steps(n: int) -> None:
#     for i in range(1, n+1):
#         print("#"*i + ' '*(n-i))


# # method 2        
# def steps(n: int) -> None:
#     all_steps = '#'*n
#     all_spaces = ' '*n    

#     for i in range(1, n+1):
#         print(all_steps[:i] + all_spaces[i:])


# # method 3
# def steps(n: int) -> None:
#     for r in range(n):
#         steps = ''
#         for c in range(n):
#             if c <= r:
#                 steps += '#'
#             else:
#                 steps += ' '
#         print(steps)


# # method 4
# def steps(n, row=0, stairs=''):
#     '''recursive solution'''
#     # base case
#     if row == n:
#         return

#     if len(stairs) <= row:
#         stairs += '#'
#     else:
#         stairs += ' '

#     if len(stairs) == n:
#         print(stairs)
#         row += 1
#         return steps(n, row=row)
    
#     # recursive case    
#     return steps(n, row=row, stairs=stairs)


# try recursion without resetting stairs

# # method 5
def steps(n: int) -> None:
    # while loop solution
    raise NotImplementedError

# steps(10)
