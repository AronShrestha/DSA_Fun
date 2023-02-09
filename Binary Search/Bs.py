import typing


li =[1,2,3,4,5,6,7]
e= len(li)-1
l=0
m=int((l+e)/2)
t=3

# def BST(li,t,l,m,e)->list:
#     if e>=l:
#         if li[m]==t:
#             return m
#         elif li[m]>t:
#             e= m-1
#             m=l-int((l-e)/2)
#             return BST(li,t,l,m,e)
#         else:
#             l= m+1
#             m=l-int((l-e)/2)
#             return BST(li,t,l,m,e)
#     return -1
        
# print(BST(li,t,l,m,e))


def binarySearch(arry,low,high,ans)->int:
    if low > high : 
        return -1
    m = low -int((low-high)/2)
    if arry[m] == ans :
        return m
    else:
        if arry[m]> ans:
            return binarySearch(arry,low ,m-1,ans)
        else:
            return binarySearch(arry,m+1,high,ans)
        
 


arry =[1,2,3,4,5,6,7]
print(binarySearch(arry,0,6,1))