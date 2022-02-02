class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def bubble(a,b):
            if int(a + b) > int(b + a):
                return 0
            else:
                return 1
        
        n = len(nums)
        for i in range(n):
            for j in range(n - 1 - i):
                if bubble(str(nums[j]),str(nums[j + 1])):
                    nums[j],nums[j + 1] = nums[j + 1],nums[j]
        
        return str(int("".join(map(str,nums))))
                    
                    
                    
                
        
        
        
        
        
        
        
       
      