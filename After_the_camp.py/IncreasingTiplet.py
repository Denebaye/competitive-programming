class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:return False
        num1 = nums[0]
        num2 = nums[1]
        j = len(nums)
        
        for i in range(1,len(nums)):
            if nums[i] > num1:
                j = i + 1
                break
            if i + 1 < len(nums):
                num1 = nums[i]
                num2 = nums[i + 1]
        
        while j < len(nums):
            if nums[j] > num2:
                return True
            elif nums[j] <= num1:
                num1 = nums[j]
            else:
                num2 = nums[j]
            j += 1
        
        return False