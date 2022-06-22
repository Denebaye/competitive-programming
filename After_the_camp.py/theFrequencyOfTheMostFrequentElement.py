class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        outPut = 1
        l = 0
        r = 0
        tot = nums[l]
        while r < len(nums):
            
            while r < len(nums) and (r - l + 1)*nums[r] <= tot + k:
                outPut = max(outPut,r - l + 1)
                r +=1
                if r < len(nums):
                    tot +=nums[r]
            
            tot -=nums[l]
            l +=1
        
        return outPut