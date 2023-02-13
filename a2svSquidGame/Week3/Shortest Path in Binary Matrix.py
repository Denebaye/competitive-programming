class Solution:
    def shortestPathBinaryMatrix(self,matrix):
        row_count = len(matrix)
        if matrix[0][0] or matrix[row_count-1][row_count-1]:
            return -1
            
        queue = [(0, 0, 1)]
        matrix[0][0] = 1
        for i, j, distance in queue:
            if i == row_count-1 and j == row_count-1: return distance
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < row_count and 0 <= y < row_count and not matrix[x][y]:
                    matrix[x][y] = 1
                    queue.append((x, y, distance+1))
        return -1
