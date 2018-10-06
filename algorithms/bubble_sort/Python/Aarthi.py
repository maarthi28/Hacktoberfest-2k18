def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(arr[j]) > int(arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = []
arr=input('ENTER THE ELEMENTS TO BE SORTED:\n').split(' ')
bubbleSort(arr)
print ("SORTED ARRAY IS:")
for i in range(len(arr)):
    print (arr[i],end=' ')
