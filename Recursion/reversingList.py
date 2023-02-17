def revList(a):
    ans = []
    if len(a)==0:
        return []
    else:
        temp = a[0]
        ans.append(temp)
        return  revList(a[1:]) + ans


print(revList([1,2,3,4]))