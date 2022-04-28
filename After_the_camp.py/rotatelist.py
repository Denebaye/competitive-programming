class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        N = len(nums)
        k %= N
        if k > 0:
            reverse(0,N - 1)
            reverse(0,k - 1)
            reverse(k,N - 1)
