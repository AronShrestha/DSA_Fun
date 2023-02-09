

def helper(n:list,index:int,l)->bool:
    if index >= l:
        return True
    else:
        if n[index-1] <= n[index]:
            return helper(n,index+1,l)
        else:
            return False



def checkSorted(n):
    lengthOfn = len(n)
    return helper(n,1,lengthOfn)

print(checkSorted([1,2,3,4,0,12,3]))