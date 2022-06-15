class Solution:
    def capture(self,b,i,j):
        
        b[i][j] = "X"
        directions = [(i - 1,j),(i + 1,j),(i,j - 1),(i,j + 1)]
        
        for di in directions:
            if di[0] < len(b)and di[0] >= 0 and di[1] < len(b[0]) and di[1] >=0 and b[di[0]][di[1]]=="O":
                self.capture(b,di[0],di[1])
    
    def noCapture(self,b,i,j):
        b[i][j] = "S"
        directions = [(i - 1,j),(i + 1,j),(i,j - 1),(i,j + 1)]
        
        for di in directions:
            if di[0] < len(b)and di[0] >=0 and di[1] < len(b[0]) and di[1] >=0 and b[di[0]][di[1]] =="O":
                self.noCapture(b,di[0],di[1])
        
    def checkDfs(self,b,i,j,visited):
        if i >= len(b) or i < 0 or j >= len(b[0]) or j < 0 :
            return False
        
        if b[i][j] == "X":
            return True
        
        directions = [(i - 1,j),(i + 1,j),(i,j - 1),(i,j + 1)]
        visited.add((i,j))
        # print((i,j))
        isCaptured = True
        flag = True
        for di in directions:
            if di not in visited:
                flag = False
                isCaptured &=self.checkDfs(b,di[0],di[1],visited)
                if not isCaptured:
                    return False
        return isCaptured
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        set1 = set()
        m = len(board)
        n = len(board[0])
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    captured = self.checkDfs(board,row,col,set1)
                    if captured == True:
                        self.capture(board,row,col)
                    else:
                        self.noCapture(board,row,col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "S":
                    board[row][col] = "O"
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        