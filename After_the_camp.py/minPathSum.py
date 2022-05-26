class Solution:
    def dfs(self,grid,i,j,dp):
        if len(grid) == 0:return 0
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j] 
        
        
        if i >=len(grid) or j >=len(grid[0]): 
            return sys.maxsize
        if (i,j) in dp:
            return dp[(i,j)]
       
        dp[(i,j)] = grid[i][j] + min(self.dfs(grid,i + 1,j,dp),self.dfs(grid,i,j + 1,dp))
        return dp[(i,j)]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.dfs(grid,0,0,{})