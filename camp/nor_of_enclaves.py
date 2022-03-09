class Solution:
    def dfs(self,grid,r,c):
        if r <0 or c <0 or r >len(grid) - 1 or c >len(grid[0]) - 1 or grid[r][c]==0:
            return
        
        if grid[r][c]==1:
            grid[r][c] = 0
            self.dfs(grid,r - 1,c)
            self.dfs(grid,r + 1,c)
            self.dfs(grid,r,c - 1)
            self.dfs(grid,r,c + 1)
            
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for r in range(n):
            for c in range(m):
                if ( r==0 or c==0 or r==n-1 or c==m-1 )and grid[r][c]==1:                    
                    self.dfs(grid,r,c)
                
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    count += 1
            
        return count
#     time and space complexity
# time = o(n^2)
# space = O(1)
        
                
                    