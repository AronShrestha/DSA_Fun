arr = [5,9,3,0,2,1,1,111,222,33,112,5554,456]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(1,len(arr)-i):
            if(arr[j-1]>arr[j]):
                temp = arr[j-1]
                arr[j-1] =arr[j]
                arr[j] =temp
    print(arr)
            


bubbleSort(arr)