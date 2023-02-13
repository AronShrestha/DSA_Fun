def merge(l,r):
    i = 0
    j = 0
    a =[]
    while i<len(l) and j<len(r):
        if l[i] >= r[j]:
            a.append(r[j])
            j+=1
        else:
            a.append(l[i])
            i+=1
    if i <len(l):
        while i < len(l):
            a.append(l[i])
            i+=1
    else:
        while j<len(r):
            a.append(r[j])
            j+=1
    return a
        
        


def mergesort(a):
    if len(a) == 1:
        return a
    else:
        m = int(len(a)/2)
        left = mergesort(a[0:m],)
        right = mergesort(a[m:len(a)])
        return merge(left,right)


a=[1,99,19,2,100,3,66,29,30]
print(mergesort(a))