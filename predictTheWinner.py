class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def pre(s,e):
            if s == e:
                return nums[s]
            else:
                return max(nums[s] - pre(s + 1,e),nums[e] - pre(s,e - 1))
        
        return pre(0,len(nums) - 1) >= 0