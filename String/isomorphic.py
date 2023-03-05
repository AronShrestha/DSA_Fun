
# def isomorphic(s, t):
#     hashmapST = {}
#     hashmapTS = {}
#     if len(s)!= len(t):
#         return False
#     else:
#         for i in range(len(s)):
#             Sterm, Tterm = s[i], t[i]
            
#             if (Sterm in hashmapST) and (hashmapST[Sterm] != Tterm) or (Tterm in hashmapTS) and (hashmapTS[Tterm] != Sterm):
#                 return False
            
#             else:
#                 hashmapST[Sterm] = Tterm
#                 hashmapTS[Tterm] = Sterm
    
#     return True

def isomorphic(s,t):
    m1 = [0]
    m2 =[0]


print(isomorphic("badc", "baba"))