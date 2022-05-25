class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [1 for i in range(len(isConnected))]
        def find(parent , x):
            if parent[x] == x:
                return x
            parent[x] = find(parent,parent[x])
            return parent[x]
        
        def union(parent,rank,x,y):
            px,py = find(parent,x),find(parent,y)
            if px!= py:
                if rank[y] < rank[x]:
                    py,px = px,py

                parent[px] = py
                rank[px] += rank[py]
        
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    union(parent,rank,i,j)
        
        # print(rank)
        
        return len(set([find(parent,i) for i in range(len(isConnected)) ]))
