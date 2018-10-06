# Python program for implementation of Bubble Sort 
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if int(arr[j]) > int(arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 

arr = []
arr=input('ENTER THE ELEMENTS TO BE SORTED:\n').split(' ')
 
bubbleSort(arr)
 
print ("SORTED ARRAY IS:")
for i in range(len(arr)):
    print (arr[i],end=' ')
