class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.board = matrix
        m = len(self.board)
        n = len(self.board[0])
        self.board =[[0]*n] + self.board
       
        for i in range(m + 1):
            self.board[i] = [0] + self.board[i]
        m = len(self.board)
        n = len(self.board[0])
        for i in range(1,m):
            for j in range(1,n):
                self.board[i][j] +=self.board[i - 1][j] + self.board[i][j - 1] - self.board[i - 1][j - 1]
     
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.board[row2 + 1][col2 + 1] + self.board[row1][col1] - self.board[row2 + 1][col1] - self.board[row1][col2 + 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)