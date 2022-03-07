# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:return answer
        
        curr_queue = deque([(root,0)])
        next_queue = deque([(root)])
        while curr_queue:
            node1,level = curr_queue.popleft()
            node2 = next_queue.popleft()
            
            if len(answer) == level:
                answer.append([])
            if level % 2 == 0:
                answer[level].append(node1.val)
             
            if level % 2:
                answer[level].append(node2.val)
            
            if node1.left:
                curr_queue.append((node1.left,level + 1))
            if node1.right:
                curr_queue.append((node1.right,level + 1))
            if node2.right:
                next_queue.append((node2.right))
            if node2.left:
                next_queue.append((node2.left))
        
        return answer
                
                
                
                
                
                
                
                
                