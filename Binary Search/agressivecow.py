

stall = [1,2,8,4,9]

def possible(stall,mid,limit):
    cowAtIndex = 0
    numberOfCow = 1
    for i in range(1,len(stall)):
       
        if abs(stall[i]-stall[cowAtIndex])>=mid:
            numberOfCow+=1
            cowAtIndex = i
            if numberOfCow >= limit:
                return True
    return False



def binarySearch(stall,numberOfCow):
    stall = sorted(stall)
    low = stall[0]
    high = stall[len(stall)-1]-low
    ans =0
  
    while low <= high:
        mid = low -int((low-high)/2)
        if possible(stall,mid,numberOfCow):
            low = mid +1
            ans = mid
        else:
            high = mid -1
        
        
    return ans
print(binarySearch(stall,3))