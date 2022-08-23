li=[3,5,3,2,0]

def findingPeakElement(li):
    low = 0
    high = len(li)-1
    mid = low -int((low-high)/2)
    while low<high:
        print(mid)
        if li[mid] >li[mid+1] and li[mid]>li[mid-1]:
            return mid
        elif li[mid] <li[mid+1]:
            low = mid +1
        else:
            high= mid
        mid = low -int((low-high)/2)
    return-1


print(findingPeakElement(li))

