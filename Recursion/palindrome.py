def plandrome(n:str)->bool:
    l = len(n)
    e = l-1
    s = 0
    while s <= e:
        if n[s] == n[e]:
            s+=1
            e-=1
        else:
            return False
    
    return True
print(plandrome('1211'))


def pland(n:str,s:str,e:str)->bool:
    """With recursion"""
    if s == e:
        if n[s] == n[e]:
            return True
        else:
            return False
    else:
        if n[s]!=n[e]:
            return False
        return (n,s+1,e+1)

print(plandrome('111'))



    