class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        count = 0
        
        for i in range(row):
            right = col - 1
            left = 0
            idx = col
            while left <= right:
                mid = (left + right)//2
                if grid[i][mid] < 0:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            count += (col - idx)
        
        return count
# time and space complexity
# time = O(len(grid)*log(grid[0]))
# space = O(1)

                    