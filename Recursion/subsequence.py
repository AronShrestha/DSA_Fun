# def substring(unprocessed, processed):
#     if len(processed) == 0 :
#         print(unprocessed)
#         return 
#     else:
#         emited = processed[0]
#         substring(emited+unprocessed,processed[1:])
#         substring(unprocessed,processed[1:])


# substring("","abc")


def substring(unprocessed, processed,ans:list):
    """
    passing ans[list] ref
    """
    
    if len(processed) == 0 :
        ans.append(unprocessed)
        
        return ans
    else:
        emited = processed[0]
        substring(emited+unprocessed,processed[1:],ans)
        substring(unprocessed,processed[1:],ans)
        return ans
        


print(substring("","abc",[]))



# def substring(unprocessed, processed):
#     ans = []
    
#     if len(processed) == 0 :
#         ans.append(unprocessed)
        
#         return ans
#     else:
#         emited = processed[0]
        
#         ans += substring(unprocessed,processed[1:])
#         return  substring(emited+unprocessed,processed[1:]) +ans
def substring(unprocessed, processed):
    ans = []
    
    if len(processed) == 0 :
        ans.append(unprocessed)
        
        return ans
    else:
        emited = processed[0]
        right = substring(emited+unprocessed,processed[1:])
        ascii =  substring(str(ord(emited))+unprocessed,processed[1:])
        left = substring(unprocessed,processed[1:])
        ans+=right
        ans += ascii
        ans+=left
        
        return ans
        
        
        
        


print(substring("","abc"))