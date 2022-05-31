# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if root == None:return 0
        lv,rv = self.dfs(root.left),self.dfs(root.right)
        leaf_sum = root.val +  lv + rv 
        self.tilt_sum += abs(lv - rv)
        
        return leaf_sum
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt_sum = 0
        self.dfs(root)
        return self.tilt_sum