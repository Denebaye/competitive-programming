# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        outPut = []
        queue = [root]
        level = []
        
        while queue != [] and root != None:
            for node in queue:
                if node.left != None:
                    level.append(node.left)
                if node.right != None:
                    level.append(node.right)
            
            outPut.append(node.val)
            queue = level
            level = []
            
        return outPut