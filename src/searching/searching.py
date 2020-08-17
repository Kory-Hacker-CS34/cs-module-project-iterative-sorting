def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            high = mid - 1
        if target > arr[mid]:
            low = mid + 1

    return -1  # not found
# def binary_search(arr, target):

#     # Your code here
#     middle = int(len(arr) / 2)
#     high = []
#     low = []
#     #if we find the target
#     if target == arr[middle]:
#         return arr[middle]
#     #if there is only one value, we likely haven't found the target
#     if len(arr) == 1:
#         return -1
#     else:
#         #if the target is higher than the middle
#         if target > arr[middle]:
#             high = arr[middle:]
#             binary_search(high, target)
#         #if the target is lower than the middle
#         elif target < arr[middle]:
#             low = arr[:middle]
#             binary_search(low, target)
