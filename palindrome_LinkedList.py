# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:return True
        checker = []
        ptr = head 
        while ptr:
            checker.append(ptr.val)
            ptr = ptr.next
            
            
        ptr1 = 0
        ptr2 = len(checker) - 1
        
        while ptr1 <= ptr2:
            if checker[ptr1] != checker[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True     
                
        
            