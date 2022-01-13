class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        
        nums.sort(reverse = True)
        print(nums)
        if k <= len(nums):
            return str(nums[k - 1])
        