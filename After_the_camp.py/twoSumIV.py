# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node,target,visited):
        if not node:return False
        if target - node.val in visited:
            return True
        visited.add(node.val)
        return self.solve(node.right,target,visited) or self.solve(node.left,target,visited)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.solve(root,k,set())
# time and space complexity
# time = O(n)
# space = O(n)
