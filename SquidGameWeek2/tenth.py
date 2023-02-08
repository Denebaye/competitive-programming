class Solution:
    def restoreArray(self, adjacentPairList: List[List[int]]) -> List[int]:
  
        nodeAdjacencyMap, restoredArray, nodeCount = defaultdict(list), [], len(adjacentPairList) + 1
        for firstNode, secondNode in adjacentPairList:
            nodeAdjacencyMap[firstNode] += [secondNode]
            nodeAdjacencyMap[secondNode] += [firstNode]
        previousNode = -math.inf
        for node, neighbors in nodeAdjacencyMap.items():
            if len(neighbors) == 1:
                restoredArray += [node]
                break
        while len(restoredArray) < nodeCount:
            for nextNode in nodeAdjacencyMap.pop(restoredArray[-1]):
                if nextNode != previousNode:
                    previousNode = restoredArray[-1]
                    restoredArray += [nextNode]
                    break
        return restoredArray
