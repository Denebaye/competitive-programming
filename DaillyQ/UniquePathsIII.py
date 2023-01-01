class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.tot_count = 0
        self.output = 0
        visited = set()

        def helper(i,j,count):
            if i >= row or i < 0 or j >= col or j < 0:
                return
            
            if grid[i][j] == -1 or grid[i][j] == 1 or (i,j) in visited:
                return 

            if grid[i][j] == 2:
                if count == self.tot_count:
                    self.output +=1
                return

            visited.add((i,j))

            direction = [(-1,0),(1,0),(0,-1),(0,1)]
            for x,y in direction:
                helper(i + x,j + y,count + 1)
            
            visited.remove((i,j))
            return 

        # count total number of empty squares we can walk over 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    self.tot_count +=1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    helper(i - 1,j,0)
                    helper(i + 1,j,0)
                    helper(i,j - 1,0)
                    helper(i,j + 1,0)
                    break
        
        return self.output