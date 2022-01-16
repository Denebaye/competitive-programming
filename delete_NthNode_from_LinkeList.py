# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 1
        fpt = head
        if head.next == None: return None
        while fpt != None and fpt.next != None:
            N += 1
            fpt = fpt.next.next
            
            
        if fpt == None:
            N = (N-1)*2
        else:
            N = (N*2) - 1
        target = N - n
        if target == 0:
            head = head.next
            return head
        N = 2
        n = 1
        
        fEvenptr = head.next
        head.next = fEvenptr
        bOddptr = head
        head1 = bOddptr

        if target % 2 != 0:
            for i in range(target):
                if target == n:
                    bOddptr.next = bOddptr.next.next
                    break
                n += 2
                bOddptr = bOddptr.next.next
                
            return head1
        
        else:
            for i in range(target):
                if target == N:
                    fEvenptr.next = fEvenptr.next.next
                    break
                N += 2
                fEvenptr = fEvenptr.next.next
                
            return head    
        