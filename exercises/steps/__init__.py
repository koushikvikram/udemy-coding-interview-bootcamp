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

#     # recursive case (if)
#     if len(stairs) == n:
#         print(stairs)
#         return steps(n, row+1)
#     # recursive case (else)
#     return steps(n, row, stairs)


# # method 5
def steps(n: int) -> None:
    # while loop solution
    row = 1
    # row starts from 1
    while row <= n:
        stairs = ''
        # len(stairs) starts from 0
        while len(stairs) < n:
            if len(stairs) < row:
                stairs += '#'
            else:
                stairs += ' '
        print(stairs)
        row += 1


steps(10)
