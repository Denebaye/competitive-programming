from logging.config import valid_ident


class Node:
    def __init__(self, val , next = None) -> None:
        self.value = val
        self.next = next

head = Node(5)
cur = head
ptr = head
stack = []
for i in range(10):
    cur.next = Node(i)
    cur = cur.next
while ptr != None:
    stack.append(ptr)
    print(stack[-1].value)
    ptr = ptr.next
    



