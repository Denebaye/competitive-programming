class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """l = 0
        r = len(nums) - 1
        
        while r >= l:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
        """
        def BS(arr,l,r,T):
            
            if l > r:
                return -1
            
            mid = (l + r)//2
            
            if arr[mid] == T:
                return mid
            
            if arr[mid] < T:
                l = mid + 1
            else:
                r = mid - 1
                
            return BS(arr,l,r,T)
            
            
        return BS(nums,0,len(nums) - 1,target)
    
        
    