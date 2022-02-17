#prim's algorithm 
INF = 9999999
N = 5
# adjacency matrix
Graph = [[0, 20, 15, 0, 0],
        [20, 0, 15, 19, 20],
        [15, 15, 0, 10, 16],
        [0, 19, 10, 0, 10],
        [0, 20, 16, 10, 0]]

marked = [0, 0, 0, 0, 0]

no_edge = 0

marked[0] = True

print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minm = INF
    a = 0
    b = 0
    for m in range(N):
        if marked[m]:
            for n in range(N):
                if ((not marked[n]) and Graph[m][n]):  
                    if minm > Graph[m][n]:
                        minm = Graph[m][n]
                        a = m
                        b = n
    print(" " + str(a) + "-" + str(b) + " :  " + str(Graph[a][b]))
    marked[b] = True
    no_edge += 1