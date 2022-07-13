class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        destinations = set()
        
        for source,destination in edges:
            destinations.add(destination)
        
        outPut = []
        for i in range(n):
            if i not in destinations:
                outPut.append(i)
            
        return outPut