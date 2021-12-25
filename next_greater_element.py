class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        Dict = {}
        stack = []
        for val in nums2:
            while stack and stack[-1] < val:
                Dict[stack.pop()] = val
            
            stack.append(val)
            
        for val in nums1:
            if val in Dict:
                ans.append(Dict[val])
            else:
                ans.append(-1)
                
        return ans         
                