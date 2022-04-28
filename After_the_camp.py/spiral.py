class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        st_row = 0
        st_col = 0
        end_row = len(matrix)
        end_col = len(matrix[0])
        
        ans = []
        while st_row < end_row or st_col < end_col:
#            right
            if st_row < end_row:
                ans.extend([matrix[st_row][j] for j in range(st_col,end_col)])
                st_row += 1
#            down
            if st_col < end_col:
                ans.extend([matrix[i][end_col - 1] for i in range(st_row,end_row)])
                end_col -= 1
#           left 
            if st_row < end_row:
                ans.extend([matrix[end_row - 1][j] for j in range(end_col - 1,st_col - 1,-1)])
                end_row -= 1
#           up 
            if st_col < end_col:
                ans.extend([matrix[i][st_col] for i in range(end_row - 1,st_row - 1,-1)])
                st_col += 1
        
        return ans
# time and space complexity
# time = O(n * m)
# space = O(1)

    

            