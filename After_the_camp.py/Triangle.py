class Solution:
    def calculate(self,tri,row,idx,dp):
        if row == len(tri) - 1:
            return tri[row][idx]
        
        if (row,idx) in dp:
            return dp[(row,idx)]
        
        dp[(row,idx)] = tri[row][idx] + min(self.calculate(tri,row + 1,idx,dp),self.calculate(tri,row + 1,idx + 1,dp))
        return dp[(row,idx)]
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.calculate(triangle,0,0,{})
        
