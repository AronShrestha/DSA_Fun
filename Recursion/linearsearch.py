def Lsearch(arr:list,n:int,l:int,target:int)->int:
    if n > l:
        return -1
    else:
        if arr[n] == target:
            return n
        return Lsearch(arr,n+1,l,target)


arr =[ 11,22,3,4,5,6,88,9,123]
l = len(arr)-1
print(Lsearch(arr,0,l,33))

