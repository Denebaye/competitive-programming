class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        heap = []
        for val in freq.values():
            heappush(heap,-val)        

            
        tot = 0
        N = len(arr)
        outPut = 0 
        
        while heap:
            tot +=(-heappop(heap))
            outPut +=1
            if tot >= N//2:
                return outPut 

# time and space complexity
# time = O(nlog(n))
# space = O(n)