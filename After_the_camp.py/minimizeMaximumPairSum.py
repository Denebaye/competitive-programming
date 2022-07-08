class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        mxPair = 0
        while left < right:
            mxPair = max(mxPair,nums[right] + nums[left])
            right -=1
            left +=1
        
        return mxPair