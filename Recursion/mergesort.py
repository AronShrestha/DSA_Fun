# def merge(l,r)->list:
#     i = 0
#     j = 0
#     a =[]
#     while i<len(l) and j<len(r):
#         if l[i] >= r[j]:
#             a.append(r[j])
#             j+=1
#         else:
#             a.append(l[i])
#             i+=1
#     if i <len(l):
#         while i < len(l):
#             a.append(l[i])
#             i+=1
#     else:
#         while j<len(r):
#             a.append(r[j])
#             j+=1
#     return a
        
        


# def mergesort(a):
#     if len(a) == 1:
#         return a
#     else:
#         m = int(len(a)/2)
#         left = mergesort(a[0:m],)
#         right = mergesort(a[m:len(a)])
#         return merge(left,right)



def merge2ndway(a,s,m,e)->None:
    i = s
    j = m
    sorted_array = []
    index_of_sorted_array = 0
    while i < m and j < e:
        if a[i]< a[j]:
            sorted_array.append(a[i])
            i+=1
        else:
            sorted_array.append(a[j])
            j+=1
        index_of_sorted_array+=1
    if i<m:
        while i < m:
            sorted_array.append(a[i])
            i+=1
    else:
        while j < e:
            sorted_array.append(a[j])
            j+=1
    
    for i in range(len(sorted_array)):
        a[s+i] = sorted_array[i]


def mergesort2nway(a,l,h)->None:
    if h-l ==1 :
        return 
    m = l -int((l-h)/2)
    mergesort2nway(a,l,m)
    mergesort2nway(a,m,h)
    merge2ndway(a,l,m,h)
a=[1,99,19,2,100,3,66,29,30]
mergesort2nway(a,0,len(a))
print(a)