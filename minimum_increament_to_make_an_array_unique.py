class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        op = 0
        
        for i in range(1, len(nums)):
             if nums[i] <= nums[i-1]:
                op += (nums[i - 1] + 1) - nums[i]
                nums[i] = nums[i-1] + 1
            
        return op
    