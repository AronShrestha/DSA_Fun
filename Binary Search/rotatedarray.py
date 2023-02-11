class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
        h=len(nums)-1
        return self.rotatedArray(nums,h,l,target)
    
    def rotatedArray(self,a,h,l,T)->int:
    
        if l > h : 
            return -1
        else:
            m = l-int((l-h)/2)
            if a[m] == T:
                return m
            else:  
                if a[l] <= a[m] :#looking for first half start to mid if sorted or not
                    if a[l]<=T and a[m]>=T:# looking if target lies between sorted (start to mid)
                        h = m -1
                    else:
                        l = m + 1  # lies outside case
                elif a[m]<=T and a[h]>=T: # if not sorted and target lies betwwen mid to end
                    l = m +1
                else: # if target don't lie between mid and end i,e lies before mid
                    h = m -1
            return self.rotatedArray(a,h,l,T)

nums  = [5,6,7,8,9,1,2,3]
t = 9
q = Solution()
print(q.search(nums,t))