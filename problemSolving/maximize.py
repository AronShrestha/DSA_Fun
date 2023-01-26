from  typing import *

b = 20 
n = 3
a = [[3,1,2,3],[3,4,2,3],[3,1,10,2]]

def possible(arr:List[List[int]],mid,b:int,n:int):
    sumA = [0,0,0]
    for i in range(n):
        for val in a[i]:
            if sumA[i]+val < mid :
                sumA[i]+=val
            else:
                continue
        if sum(sumA) > b:
            return False
    return True
        

        
def sol(arr:List[List[int]],b:int,n:int):
    # print(arr,b,n)
    low = 0
    high = b
    ans = 0
    while low <= high :
        mid = low - int((low-high)/2)
        if  possible(arr,mid,b,n):
            low = mid +1
            ans = mid
           
        else:
            high = mid - 1
    
    return ans





print(sol(a,b,n))