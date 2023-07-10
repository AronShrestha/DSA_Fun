

def sum(arr : list, target : int)-> list[int]:
    '3 ponter way acc to e'
    print("Inside func")
    for i in range(2,len(arr)):
        if ((arr[i-1] + arr[i-2] +arr[i]) == target):
            return [i-2,i-1,i]
    return [-1]

print(sum([2,3,1,5,9,3,5],17))