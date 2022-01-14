class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(10**9 + 7)
        def evpow( x , y,mod):
            if y == 0: return 1
            elif y == 1:
                return x
            else:
                ans = evpow(x,y//2,mod)
                ans *= ans
                ans %= mod
                if y % 2:
                    ans *= x
                    ans %= mod
            return ans
              
        if n % 2:
            return (evpow(5,1 + n//2,mod) * evpow(4,n//2,mod)) % mod 
        else:
            return (evpow(5,n//2,mod) * evpow(4,n//2,mod)) % mod 