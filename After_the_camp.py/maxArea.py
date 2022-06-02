class Solution:
    def dfs(self,grid,i,j):
        
        directions = [(i - 1,j),(i + 1,j),(i,j + 1),(i,j - 1)]
        curArea = grid[i][j]
        grid[i][j] = "#"
        for d in directions:
            if d[0] >= 0 and d[1] >=0 and d[0] < len(grid) and d[1] < len(grid[0]) and grid[d[0]][d[1]] == 1:
                curArea +=self.dfs(grid,d[0],d[1])
        
        return curArea
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    maxArea = max(maxArea,self.dfs(grid,row,col))
                    
        return maxArea