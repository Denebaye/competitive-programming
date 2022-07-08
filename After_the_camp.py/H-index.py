class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        temp = [0 for _ in range(N + 1)]
        for index,value in enumerate(citations):
            if value > N:
                temp[N] +=1
            else:
                temp[value] +=1
        
        total = 0
        for index in range(N,-1,-1):
            total +=temp[index]
            if total >=index:
                return index