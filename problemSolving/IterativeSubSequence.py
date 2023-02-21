




def subsequence(arr:list)->list[list]:
    outerlist:list[list] = [[]]
    for number in arr:
        length = len(outerlist)
        for i in range(length):
            innerlist:list = outerlist[i].copy() #here we are using shallow copy cz assignment would jst pass reference 
        
            innerlist.append(number)
            outerlist.append(innerlist)
    return outerlist

print(subsequence([1,2,3]))