# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastptr = slowptr = head
        while fastptr != None and fastptr.next != None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            
        return slowptr     