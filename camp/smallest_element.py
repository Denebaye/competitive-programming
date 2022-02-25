class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def Count(mid):
            c = 0
            for row in range(1,m + 1):
                c += min(mid//row , n)
            
            return c
        
        l = 1
        r = n*m
        while l < r:
            mid = (r + l)//2
            if Count(mid) >= k:
                r = mid
            else:
                l = mid + 1
        
        return l
                