class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[len(nums) - 1]:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return - 1
        
        left = 0
        right = len(nums) - 1
        pivot = 0
        
        
        
        
        
        
        
        
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == nums[left] and nums[mid] < nums[0]:
                pivot = mid
                break
                
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:       
                pivot = mid
                right = mid - 1      
            
            
        # print(pivot)
        if target >= nums[0]:
            left = 0
            right = pivot
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return - 1
        
        
        
        else:
            left = pivot 
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return - 1

            
            
            
            
            
            