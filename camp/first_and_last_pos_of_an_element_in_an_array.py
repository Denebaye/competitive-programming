class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        f1 = -1
        f2 = -1
        #while r >= l and len(arr) and (r + l)//2 < len(arr):
            mid = (r + l)//2
            if arr[mid] < target:
                l = mid + 1
                
            elif arr[mid] == target:
                f1 = mid
                r = mid - 1
                
            else:
                r = mid - 1
            
        l = 0
        r = len(arr) - 1
        
        #while r >= l and (r + l)//2 < len(arr) and len(arr):
            mid = (r + l)//2
            if arr[mid] > target:
                r = mid - 1    
                
            elif arr[mid] == target:
                f2 = mid
                l = mid + 1
            else:
                l = mid + 1
            
        return [f1,f2]
                