class Solution:
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        hash={}
        ans = []
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            
        
            if temp not in hash.keys():
                hash[temp] =[strs[i]]
                
            else:
                hash[temp].append(strs[i])
            
        
        for val in hash.values():
            ans.append(val)
            
            
        
        return ans
c = Solution()
strs=["eat","tea","tan","ate","nat","bat"]
print(c.groupAnagrams(strs))