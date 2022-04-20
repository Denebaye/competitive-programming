class Solution(object):
    def rearrangeArray(self, nums):
        
        nums = sorted(nums)
        for i in range(1, len(nums), 2):
            if i != len(nums)-1:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums
# space and time complexity
# time = O(nlogn)
# space = O(1)