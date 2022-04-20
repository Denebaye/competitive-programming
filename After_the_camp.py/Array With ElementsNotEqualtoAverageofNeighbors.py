class Solution(object):
    def rearrangeArray(self, nums):
        
        nums = sorted(nums)

        i = 1
        while i < len(nums) - 1:
            nums[i],nums[i + 1] = nums[i + 1],nums[i]
            i += 2
 
        return nums
# space and time complexity
# time = O(nlogn)
# space = O(1)