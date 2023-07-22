def find_duplicates(arr):

    temp={}
    duplicate=[]
    for i in range(len(arr)):
        if arr[i] not in temp:
            temp[arr[i]] =1
        else:
            duplicate.append(arr[i])
    return duplicate






print(find_duplicates([1,1,1,1,2,2,2,23,3,4,56,7,8,77,8,8,9,1]))