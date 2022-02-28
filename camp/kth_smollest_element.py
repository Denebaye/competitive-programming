class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """|6(0,0)  7(0,1)  13(0,2)|       
           |11(1,0) 12(1,1) 14(1,2)|
           |12(2,0) 15(2,1) 20(2,2)|
           so  
           |(6 + 20)//2 = 13 and the tot count of nums which are less than or equal to 13 is 6 and my is 8 so I move my left value to 13 + 1 cause nums less than or equal to 13 ar e useless for us (14 + 20)//2 = 17; Count(17) = 8 but there may be a number which can have the same count so right value becomes = 17 and mid = (17 + 14)//2 = 15 count(15) = 8 and we assign right = 15 and mid = (15 + 14)//2 = 14, count(14) = 7,now left becomes = 15 then we will halt our calculation as soon as right value = left value
         1) count
         2) right
         3) left
         
        """
        def count(mid):
            c = 0
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] <= mid:
                        c += 1
            return c
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right)//2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left
            
            
        
        
        
        
        
     