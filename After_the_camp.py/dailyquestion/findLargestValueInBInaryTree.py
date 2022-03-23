from collections import deque
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        ans = []
        queue = deque([(0,root)])
        
        while queue:
            level,node = queue.popleft()
            if stack and stack[-1][0] != level:
                maxval = stack[-1][1]
                while stack:
                    maxval = max(maxval,stack[-1][1])
                    stack.pop()
                    
                ans.append(maxval)
            if node:   
                stack.append((level,node.val))
            
                if node.left:
                    queue.append((level + 1,node.left))
                if node.right:
                    queue.append((level + 1,node.right))
            
            if len(queue) == 0 and stack:
                maxval = stack[-1][1]
                while stack:
                    maxval = max(maxval,stack[-1][1])
                    stack.pop()
                ans.append(maxval)
        
        return ans
            
            
        