# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative solution 
        prev = None
        curr = head
        while curr:
            ptr = curr.next
            curr.next = prev
            prev = curr
            curr = ptr
        return prev   
        #recursive solution
        def rev(head):
            if head == None:
                return 
            if head.next == None:
                return head
            else:
                nodeptr = head
                head.next = None
                res = rev(nodeptr)
                res.next = nodeptr
                return res
            return res
        return rev(head)       
                