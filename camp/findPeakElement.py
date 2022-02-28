class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if mid == 0:
                if nums[left] < nums[right]:
                    return right
                
                return left
            
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            
            if nums[mid + 1] >= nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
                
        
        return left
                
            