
def helper(n:int,steps:int)->int:
    if  n == 0:
        return steps
    else:
        if n%2==0:
            n = n/2
        else:
            n-=1
        return helper(n,steps+1)


def mainfun(n:int)->int:
    return helper(n,0)


print(mainfun(8))
