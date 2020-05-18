# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # n -1 because after the sort, the one remaining is the largest
    for i in range(0, len(arr) - 1):
        print(arr)
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # use first number in list and 
        #loop over right side starting with the next index 
             
        for next_smallest in range(cur_index, len(arr)):
            
        # is next smallest less than right side of arr--smallest index
            
            if arr[next_smallest] < arr[smallest_index]:
                
        # make new index equal to smallest index
        
                smallest_index =  next_smallest
                           
        # TO-DO: swap a,b = b,a 
        
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr #make sure you are returning in the proper place


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #need to know if swaps occurred
    swaps = True
    #for pair in range(len(arr))
    #should be using a while loop
    while swaps:
    #loop through elements 
        swaps = False
        for i in range(len(arr) - 1):
            pair = i

    #compare elements if arr[i] is greater move right
    
            if arr[pair] > arr[pair + 1]:
                
            #swap them a,b = b,a

                arr[pair], arr[pair + 1] = arr[pair + 1], arr[pair]
                swaps = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
