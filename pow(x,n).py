class Solution:   
    def myPow(self, x: float, n: int) -> float:
        def evPow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            ans = evPow(x,n//2)
            ans *= ans
            if n % 2 != 0:
                return x*ans
            
            return ans
        ans = evPow(x,abs(n))
        if n > 0:
            return ans
        else:
            return 1/ans
                    