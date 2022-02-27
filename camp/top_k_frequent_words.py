class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        c = Counter(words)
        # print(c)
        max_heap = []
        for key,val in c.items():
            heapq.heappush(max_heap,[-val,key])
            
        ans = []
        while k:
            x = heapq.heappop(max_heap)
            ans.append(x[1])
            k -= 1
        
        return ans
            
            
            
            