class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = [0]*len(graph)
        parents = defaultdict(list)
        
        for parent in range(len(graph)):
            for child in graph[parent]:
                parents[child].append(parent)   
            outdegree[parent] += len(graph[parent])        
        
        queue = deque()
        
        for node in range(len(outdegree)):
            if outdegree[node] == 0:
                queue.append(node)
                
        safes = []
    
        while queue:
            free = queue.popleft()
            safes.append(free)
            
            for parent in parents[free]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    queue.append(parent)
        
        return sorted(safes)
# time and space complexity
# time = O(nodes + edges)
# space = O(nodes)