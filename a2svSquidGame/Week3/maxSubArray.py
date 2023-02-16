class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        outPut = prefix = nums[0]
        for i in range(1,len(nums)):
            prefix = max(prefix + nums[i],nums[i])
            outPut = max(prefix,outPut)
        
        return outPut
