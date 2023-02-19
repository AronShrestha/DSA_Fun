# def substring(sink, source):
#     if len(source) == 0 :
#         print(sink)
#         return 
#     else:
#         emited = source[0]
#         substring(emited+sink,source[1:])
#         substring(sink,source[1:])


# substring("","abc")


def substring(sink, source,ans):
    
    if len(source) == 0 :
        ans.append(sink)
        
        return ans
    else:
        emited = source[0]
        substring(emited+sink,source[1:],ans)
        substring(sink,source[1:],ans)
        return ans
        


# print(substring("","abc",[]))



# def substring(sink, source):
#     ans = []
    
#     if len(source) == 0 :
#         ans.append(sink)
        
#         return ans
#     else:
#         emited = source[0]
        
#         ans += substring(sink,source[1:])
#         return  substring(emited+sink,source[1:]) +ans
def substring(sink, source):
    ans = []
    
    if len(source) == 0 :
        ans.append(sink)
        
        return ans
    else:
        emited = source[0]
        right = substring(emited+sink,source[1:])
        ascii =  substring(str(ord(emited))+sink,source[1:])
        left = substring(sink,source[1:])
        ans+=right
        ans += ascii
        ans+=left
        
        return ans
        
        
        
        


print(substring("","abc"))