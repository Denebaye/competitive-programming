class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(0,len(nums)- 1):
            for j in range(1,len(nums) - i):
                if nums[i] == nums[j + i]:
                    counter = counter + 1
        return counter                    