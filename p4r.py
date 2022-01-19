class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def p4r(n):
            if n < 1:
                return False
            if n == 1:
                return True
            ans = p4r(n/4)
          
            return ans
        return p4r(n) 