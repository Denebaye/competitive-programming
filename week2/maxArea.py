class Solution:
    def maxArea(self, h: List[int]) -> int:
        left = 0
        right = len(h) - 1
        res = 0
        while left < right :
            temp = (right - left) * min(h[left],h[right])
            if h[left] <= h[right]:
                left += 1
            else:
                right -= 1
            if temp > res:
                res = temp
                
         
        return res
        
