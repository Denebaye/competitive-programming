# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,currSum,target):
        if not root:return False
        
        currSum += root.val
        
        if root.left == root.right:return currSum == target
        
        return self.solve(root.left,currSum,target) or self.solve(root.right,currSum,target)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.solve(root,0,targetSum)