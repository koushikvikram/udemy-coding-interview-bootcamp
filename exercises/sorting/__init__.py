# References
# Bubble sort explanation: https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
# Selection sort explanation: https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm
# Merge sort explanation: https://www.geeksforgeeks.org/merge-sort/


# def bubbleSort(arr):
#     swapped = False
#     i = 0
#     while True:
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             swapped = True
#         i += 1
#         if i == len(arr) - 1 and not swapped:
#             return arr
#         if i == len(arr) - 1:
#             i = 0
#             swapped = False


# def bubbleSort(arr):
#     n = len(arr)
    
#     for i in range(n):
#         # last 'i' elements are already in place
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    
#     return arr


def bubbleSort(arr):
    '''optimizing by breaking if not swapped in current iteration'''
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def selectionSort(arr):
    # aka "prove me wrong" sort
    n = len(arr)

    for i in range(n-1):
        index_min = i
        for j in range(i+1, n):
            if arr[j] < arr[index_min]:
                index_min = j
        if i != index_min:
            arr[i], arr[index_min] = arr[index_min], arr[i]

    return arr


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    center = len(arr)//2
    left = arr[:center]
    right = arr[center:]

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    '''left and right are both sorted arrays'''
    results = []

    while left and right:
        if left[0] < right[0]:
            results.append(left[0])
            left = left[1:]
        else:
            results.append(right[0])
            right = right[1:]

    results += left
    results += right

    return results



nums = [5, 2, 3, 4, 1]
sorted_nums = [1, 2, 3, 4, 5]
fn = mergeSort
print(fn(nums))  # [1, 2, 3, 4, 5]
print(fn(sorted_nums))  # [1, 2, 3, 4, 5]


# list_1 = [-30, 22]
# list_2 = [0, 97]
# print(merge(list_1, list_2)) # [-30, 0, 22, 97]