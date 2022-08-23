li=[1,2,3,4,5,6,7,7,8,8,8,8]

# def index(li,t):
#     ans=[]
#     low= 0
#     high = len(li)-1
#     mid = low-int((low-high)/2)
#     print(f"high {high}")
#     while low <= high:
#         if li[mid] == t:
            
#             ans.append(mid)
#             while mid <= high and li[mid]==t:
                
                
#                 mid+=1
#             ans.append(mid-1)
#             print(ans)
#             return ans[0],ans[-1]

             
                    
        
#         elif li[mid]>t:
           
#             high = mid -1
#             mid = low-int((low-high)/2)
#         else:
            
#             low = mid +1
#             mid = low-int((low-high)/2)
#     return ans
# print(index(li,8))


# better implementation

def get_first(li,t):
    low= 0
    high = len(li)-1
    mid = low-int((low-high)/2)
    ans =-1
    while low <= high:
        if li[mid] == t:
            ans=mid 
            high =mid -1
            

                     
        
        elif li[mid]>t:
           
            high = mid -1
           
        else:
            
            low = mid +1
        mid = low-int((low-high)/2)
    return ans

def get_last(li,t):
    low= 0
    high = len(li)-1
    mid = low-int((low-high)/2)
    ans =-1
    while low <= high:
        if li[mid] == t:
            ans=mid 
            low=mid +1
            

                     
        
        elif li[mid]>t:
           
            high = mid -1
           
        else:
            
            low = mid +1
        mid = low-int((low-high)/2)
    return ans
    

if __name__=='__main__':
    target = 8
    ans=[]
    ans.append(get_first(li,8))
    ans.append(get_last(li,8))
    print(ans[0],ans[1])
  
