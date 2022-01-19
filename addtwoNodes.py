# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1,l2,carry):
            if l1 == None and l2 == None:
                if carry ==0:
                    return None
                else:
                    NewNode = ListNode(carry)
                    #NewNode.val = carry
                    return NewNode
                
            nxt1 = None
            nxt2 = None
            val = carry
            if l1 != None:
                nxt1 = l1.next
                val += l1.val
            if l2 != None:
                nxt2 = l2.next
                val += l2.val
           
            NewNode = ListNode(val % 10)
            #NewNode.val = val % 10
            NewNode.next = add(nxt1,nxt2,val//10)
            return NewNode
        return add(l1,l2,0)
            
            
                    