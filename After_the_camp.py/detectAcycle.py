def has_cycle(head):
    nodes = set()
    while head: 
        if head in nodes: 
            return 1 
        nodes.add(head) 
        head = head.next
        
    return 0