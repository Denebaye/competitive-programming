class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left = 0
        right = len(mat) - 1

        while left < right:
            mid = left + (right - left)//2
            i = mat[mid].index(max(mat[mid]))
            
            if mid == 0:
                if mat[0][i] > mat[1][i]:
                    return [0,i]
                return [1,i]
            
            top = mat[mid - 1][i]
            bottom = mat[mid + 1][i]
            x = mat[mid][i]
            if x > top and x > bottom:
                return [mid,i]
            if top > bottom:
                right = mid - 1
            else:
                left = mid + 1
        
        return [left,mat[left].index(max(mat[left]))]
        
        
        
        