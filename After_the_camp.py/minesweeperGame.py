class Solution:
    def number(self,board,i,j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 0
        if board[i][j] == "M":
            return 1
        return 0
    
    def helper(self,board,i,j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "E":
            return 
        
        tot_num = 0
        for d in self.directions:
            tot_num +=self.number(board,d[0] + i,d[1] + j)
        
        if tot_num == 0:
            board[i][j] = "B"
            for d in self.directions:
                self.helper(board,d[0] + i,d[1] + j)
        else:
            board[i][j] = str(tot_num)
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        x = click[0]
        y = click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        self.directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
        self.helper(board,x,y)
        return board
    
        
    
