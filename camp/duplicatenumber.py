                    
class Solution:  
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums)
        while l < r:
            mid = (l + r)//2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l
            