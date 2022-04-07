"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def solve(self,root):
        if not root:return 0
        
        max_depth = 0
        
        for child in root.children:
            max_depth = max(self.solve(child),max_depth)
        
        return max_depth + 1
    
    def maxDepth(self, root: 'Node') -> int:
        return self.solve(root)
        