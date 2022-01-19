class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def p3ree(n):
            if n < 1:
                return False
            if n == 1:
                return True
            ans = p3ree(n/3)
            return ans
        return p3ree(n)