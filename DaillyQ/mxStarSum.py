class Solution:
    def solve(self,graph,vals,node,k):
        mx_heap = []
        
        for child in graph[node]:
            heappush(mx_heap,-vals[child])
        
        total = vals[node]
        while k and mx_heap:
            val = -heappop(mx_heap)
            if val < 0:
                break
            total += val
            k -=1
        
        return total
    
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        mx_star_sum = -inf
        
        for node in range(len(vals)):
            mx_star_sum = max(self.solve(graph,vals,node,k),mx_star_sum)
        
        return mx_star_sum