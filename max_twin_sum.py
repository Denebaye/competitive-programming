# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        counter = 0
        while fast:
            fast = fast.next.next
            slow = slow.next
            counter += 1
        while counter:
            ptr = head.next
            head.next = slow
            slow = head
            head = ptr 
            counter -= 1
        #print(counter)    
        res = 0
        while ptr:
            if slow.val + ptr.val > res:
                res = slow.val + ptr.val
            ptr = ptr.next 
            slow = slow.next
         
        return res