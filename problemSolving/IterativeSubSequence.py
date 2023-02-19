

def seq(arr):
    ans = [[]]
    n = len(arr)
    for num1 in range(n):

        for num2 in range(num1,n):
            a=[]
            for i in range(num1,num2+1):
                a.append(arr[i])
            ans.append(a)


    return ans

print(seq([1,2,3]))


def subsequence(arr:list)->list[list]:
    outerlist:list[list] = [[]]
    for number in arr:
        length = len(outerlist)
        for i in range(length):
            innerlist:list = outerlist[i].copy() #here we are using shallow copy cz assignment would jst pass reference 
        
            innerlist.append(number)
            outerlist.append(innerlist)
    return outerlist

# print(subsequence([1,2,3]))