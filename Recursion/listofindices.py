def indexlist(ans:list,arr:list,index:int,l:int,target:int)->list:
    if index > l:
        return ans
    else:
        if arr[index] == target:
            
            ans.append(index)
            print("processing",ans)

        return indexlist(ans,arr,index+1,l,target)
        


def indexList(arr:list,target:int,index:int)->list:
    "without passing answer list"
    temp =[]
    if index > len(arr)-1:
        return temp
    

   
    if arr[index] == target:
            
            temp.append(index)
           
    ans = indexList(arr,target,index+1)
    if len(temp)!=0:
        ans+=temp
    return ans

def List(arr:list,target):
    "without passing indez and answer list"
    data = []
    if len(arr)<=0 :
        return data
    else:
    
        
        for i in range(len(arr),0,-1):
            temp = arr.pop()
            ans = List(arr,target)
            if  temp== target:
                data.append(i-1)
            if len(data) != 0:
                ans+= data

            
          
            return ans






# arr =[ 11,22,3,4,5,6,5,5,88,9,123,22,5]
# l = len(arr)-1
# # print(indexlist([],arr,0,l,5))
a = [2,3,4,5,2,3,4,3]
# l = len(a)-1
# print(indexList(a,3,0))
print(List(a,3))

