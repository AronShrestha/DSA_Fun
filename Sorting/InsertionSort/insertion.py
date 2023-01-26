from  typing import *

a =[1,3,2,5,9,6,7,19,8,20,15,3,15]

def InsertionSort(a:List)->List:
    for i in range(1,len(a)):#taking 1 element in list and when there is only one element it is itself sorted
        key = a[i]
        j = i-1
        
        while j >= 0:
            if a[j] > key:
                a[j+1] =a[j]

            else:
                break
            j-=1
        a[j+1] = key 

    return a

print(InsertionSort(a))

