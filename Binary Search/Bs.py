from curses.ascii import BS


li =[1,2,3,4,5,6,7]
e= len(li)-1
l=0
m=int((l+e)/2)
t=3

def BST(li,t,l,m,e):
    if e>=l:
        if li[m]==t:
            return m
        elif li[m]>t:
            e= m-1
            m=l-int((l-e)/2)
            return BST(li,t,l,m,e)
        else:
            l= m+1
            m=l-int((l-e)/2)
            return BST(li,t,l,m,e)
    return -1
        
print(BST(li,t,l,m,e))