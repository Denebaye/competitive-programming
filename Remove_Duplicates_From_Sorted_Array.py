class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f = 1
        l = 0
        while f < len(nums):
            if nums[l] < nums[f]:
                l += 1
                nums[l],nums[f] = nums[f],nums[l]
            f += 1
        
        return l + 1
        