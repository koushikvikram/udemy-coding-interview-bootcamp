# --- Directions
# Print out the n-th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of the preceeding two.
# For example, the sequence
#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# forms the first ten entries of the fibonacci series.
# Example:
#   fib(4) === 3


# # method 1 - iterative solution
# def fib(n: int) -> int:
#     result = [0, 1]
#     for i in range(2, n+1):
#         result.append(result[i-2]+result[i-1])
#     return result[-1]


# method 2 - recusive solution
# def fib(n: int):
#     if n < 2:
#         return n
#     return fib(n-2) + fib(n-1)


# method 3 - recusion with memoization
fib_cache = {}

def fib_memo(n: int):
    # try to fetch result from cache
    try:
        return fib_cache[n]
    # if result not in cache, compute result and store in cache
    except:
        if n < 2:
            result = n
        else:
            result = fib_memo(n-2) + fib_memo(n-1)
        fib_cache[n] = result
    
    return result
    

# print(fib_memo(100))

# # method 4 - another iterative solution without using extra space
# def fib(n: int) -> int:
#     if n < 2:
#         return n

#     prev, current = 0, 1
#     for _ in range(2, n+1):
#         prev, current = current, prev+current
    
#     return current


# print(fib(4))
    