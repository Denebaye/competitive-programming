class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        counter = 0
        i = 0
        if target in nums:
            x = nums.index(target)
            while i < len(nums):
                if nums[i] == target :
                    counter += 1
                i += 1
            
            ans = []
            for j in range(counter):
                ans.append(x)
                x += 1
            
        
            return ans
        
        
        