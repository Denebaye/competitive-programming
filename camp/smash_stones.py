class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        length = len(stones)
        
        for i in range(length):
            heapq.heappush(max_heap,-stones[i])
        
        while len(max_heap) > 1:
            dif = (-1*heapq.heappop(max_heap) + heapq.heappop(max_heap))
            
            if dif:
                heapq.heappush(max_heap,-dif)
        
        if len(max_heap):
            return -1*max_heap[0]
        else:
            return 0
            
                