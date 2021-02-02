'''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
'''
def move_zero(arr):
    print(__doc__)
    print("The Given array is:",arr)
    swap =0
    for elem in range(len(arr)):

        if arr[elem] != 0:
            arr[swap],arr[elem] = arr[elem],arr[swap]
            swap=swap+1

    return arr




array_input = [0,1,0,3,12]
print("The output is:",move_zero(array_input))