# def checkAnagram(s, t):
#     if len(s) != len(t):
#         return False
    
#     else:
#         t1 = "".join(sorted(s))
#         t2 = "".join(sorted(t))
#         if t1 == t2:
#             return True
#         return False
    

# print(checkAnagram("aron","nora"))

 
def an(s,t):
    if len(s)!=len(t):
        return False
    hashS ={}
    hashT ={}
    for i in range(len(s)):
        S ,T = s[i] ,t[i]
        if S not in hashS:
            hashS[S] = 1
        else:
            hashS[S]+=1
        if T not in hashT:
            hashT[T] = 1
        else:
            
            hashT[T]+=1

    for c in hashS:
        if c not in hashT:
            return False
        else:
            hashS[c] == hashT[c]
            return False
    return True


print(an("rat","car"))