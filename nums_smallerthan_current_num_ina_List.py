class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        another_arr = sorted(nums)
        ans =[]
        for i in range(len(nums)):
            ans.append(another_arr.index(nums[i]))
        return ans