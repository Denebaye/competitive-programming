class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_indices = {}
        for i in range(len(nums)):
            my_indices[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in my_indices and i != my_indices[target - nums[i]]:
                return [i,my_indices[target - nums[i]]]