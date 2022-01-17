# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if list1 == None and list2 == None:return None
        templist = []
        while list1:
            templist.append(list1)
            list1 = list1.next
        
        while list2:
            templist.append(list2)
            list2 = list2.next 
        
        templist.sort(key = lambda x:x.val)
        if len(templist) == 0:return None
        head = templist[0]
        templist[-1].next = None
        for i in range(len(templist) - 1):
            templist[i].next = templist[i + 1]
            
            
        return head     