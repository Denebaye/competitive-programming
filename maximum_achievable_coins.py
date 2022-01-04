class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        N = len(piles)
        for i in range(N//3,N,2):
            ans += piles[i]
            
                
        #print(piles)
        return ans