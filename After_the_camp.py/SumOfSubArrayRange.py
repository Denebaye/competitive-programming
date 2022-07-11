class Solution:
    def helper(self,nums,i,j):
        mn = min(nums[i],nums[j])
        mx = max(nums[i],nums[j])
        curr = mx - mn
        j += 1
        while j < len(nums):
            mn = min(mn,nums[j])
            mx = max(mx,nums[j])
            
            curr +=(mx - mn)
            j +=1
        
        return curr
        
    def subArrayRanges(self, nums: List[int]) -> int:
        outPut = 0
        for i in range(len(nums) - 1):
            outPut += self.helper(nums,i,i + 1)
        
        return outPut
        