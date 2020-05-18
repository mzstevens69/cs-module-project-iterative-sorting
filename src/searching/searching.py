def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty

    low = 0   #left
    high = len(arr)-1 #right

    while low <= high:
        mid = (low + high) //2
    
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
        #toss out the left side of arr
        #update our left index
            low = mid + 1      
        
        #otherwise, arr[mid] > target  
        else:
            high = mid - 1

    return -1 # not found
#Recursive Binary search  
# def binary_search_recursive(arr, target, low, high):
  
#     middle = (low+high)//2

    # if len(arr) == 0:
    #     return -1 # array empty
    
    #     if arr[middle] == target:
    #         return middle
        
    #     elif arr[middle] > target:
    #         return binary_search_recursive(arr, target, low, high - 1)
    #     else:
    #         return binary_search_recursive(arr, target, low + 1, high)
    
    # else:
    #     return - 1
