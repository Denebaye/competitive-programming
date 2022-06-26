class Solution:
    def solve(self,seg):
        seg.sort()
        diff = seg[1] - seg[0]
        for i in range(1,len(seg)):
            if seg[i] - seg[i - 1] != diff:
                return False
            
        return True
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans = []
        for idx in range(len(l)):
            ans.append(self.solve(nums[l[idx]:r[idx] + 1]))
        
        return ans
        
        