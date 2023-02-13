
def findMin(a,l,h):
    low  = l
    min = 9999999999
    ans_index = -1
    while low < h :
        if a[low] < min :

            min = a[low]
            ans_index = l
        low+=1
    a[l],a[ans_index] = a[ans_index],a[l]



def  selectionsort(a,l,h):
    if l == h :
        return 
    else:
        findMin(a,l,h)
        selectionsort(a,l+1,h)

arr =[20,1,2,4,30]
selectionsort(arr,0,len(arr))