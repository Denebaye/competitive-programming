class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        
        prefix_sum = 0
        
        for i in range(len(nums)):
            if total - (prefix_sum + nums[i]) == prefix_sum:
                return i
            prefix_sum += nums[i]
            
        return - 1