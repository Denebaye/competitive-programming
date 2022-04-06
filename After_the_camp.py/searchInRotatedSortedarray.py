class Solution:
    def findPivot(self,arr): 
        
        right = len(arr) - 1
        left = 0
        
        while left < right:
            mid = left + (right - left)//2
            if arr[mid] < arr[right]:
                right = mid
            else:
                left = mid + 1
        return left
    def binarySearch(self,l,r,arr,target):
        
        while l <= r:
            mid = l + (r - l)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
                
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:return 0
        x = self.binarySearch(0,self.findPivot(nums) - 1,nums,target)
        
        y = self.binarySearch(self.findPivot(nums),len(nums) -1,nums,target)
        
        if x >= 0:
            return x
        if y >=0:
            return y
        return -1
        
        
        
        