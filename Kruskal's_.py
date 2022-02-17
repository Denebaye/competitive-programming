class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def new_edge(self, x, y, z):
        self.graph.append([x, y, z])



    def look(self, parent, i):
        if parent[i] == i:
            return i
        return self.look(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.look(parent, x)
        yroot = self.look(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # solving the problem
    def kruskal(self):
        answer = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.look(parent, u)
            y = self.look(parent, v)
            if x != y:
                e = e + 1
                answer.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, cost in answer:
            print("%d - %d: %d" % (u, v, cost))


p = Graph(6)
p.new_edge(0, 1, 4)
p.new_edge(0, 2, 4)
p.new_edge(1, 2, 2)
p.new_edge(1, 0, 4)
p.new_edge(2, 0, 4)
p.new_edge(2, 1, 2)
p.new_edge(2, 3, 3)
p.new_edge(2, 5, 2)
p.new_edge(2, 4, 4)
p.new_edge(3, 2, 3)
p.new_edge(3, 4, 3)
p.new_edge(4, 2, 4)
p.new_edge(4, 3, 3)
p.new_edge(5, 2, 2)
p.new_edge(5, 4, 3)
p.kruskal()