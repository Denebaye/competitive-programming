#definition for class singly-linkedList
from os import link
from typing import *
class Node:
    def __init__(self,val = 0,next = None) -> None:
        self.val = val
        self.next = next

class ListNode:
    def __init__(self,head) -> None:
        self.head = head

    def nextLargerNodes(self) -> List[int]:
        pos = -1
        stack = []
        ans = []
        node = self.head
        while node:
            pos += 1
            ans.append(0)
            while stack and stack[-1][1] < node.val:
                idx,val = stack.pop()
                ans[idx] = node.val

            stack.append((pos,node.val))
            node = node.next
        return ans

arr = [6,1,1,3,5]
head = Node(arr[0])
linked_list = ListNode(head)
node = linked_list.head

for i in range(1, len(arr)):
    node.next = Node(arr[i])
    node = node.next

print(linked_list.nextLargerNodes())
