# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

from typing import List


# # Method 1
# def chunk(input_list: List[int], chunk_size: int) -> List[List[int]]:
#     assert chunk_size >= 1, "chunk size should be at least 1"
#     output = []

#     for i in range(0, len(input_list), chunk_size):
#         output.append(list(input_list[i: i+chunk_size]))
    
#     return output


# Method 2
def chunk(input_list: List[int], chunk_size: int) -> List[List[int]]:
    # while loop solution
    assert chunk_size >= 1, "chunk size should be at least 1"
    output = []
    i = 0

    while i < len(input_list):
        if i+chunk_size < len(input_list):
            output.append(input_list[i:i+chunk_size])
        else:
            output.append(input_list[i:])
        i += chunk_size

    return output
    