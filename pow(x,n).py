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
            
            return ans*(x if n % 2 else 1)
        
        return evPow(x,abs(n)) ** (-1 if n < 0 else 1)