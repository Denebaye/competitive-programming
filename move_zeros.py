class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = 0
        while r < len(nums):
            if nums[r]:
                nums[r],nums[w] = nums[w],nums[r]
                w += 1
            r += 1
            
        