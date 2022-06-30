class Solution:
    def solve(self,cost,i,dp):
        if i >= len(cost):
            return 0
        
        if i in dp:
            return dp[i]
        
        else:
            dp[i] = cost[i] + min(self.solve(cost,i+1,dp),self.solve(cost,i+2,dp))
            return dp[i]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        temp = min(self.solve(cost,0,memo),self.solve(cost,1,memo))
        return temp