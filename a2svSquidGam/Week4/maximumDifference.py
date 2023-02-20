class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mx = nums[-1]
        outPut = -1
        
        for i in range(len(nums) - 2,-1,-1):
            mx = max(mx,nums[i])
            if mx != nums[i]:
                outPut = max(outPut,mx - nums[i])
            
        
        return outPut
