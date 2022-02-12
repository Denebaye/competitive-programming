graph = {
  '7' : ['3','5'],
  '2' : ['4', '3'],
  '5' : ['8'],
  '4' : [],
  '3' : ['8'],
  '8' : []
}

seen= set() 

def dfs(seen, graph, node):  
    if node not in seen:
        print (node)
        seen.add(node)
        for relative in graph[node]:
            dfs(seen, graph, relative)


print("Following is the Depth-First Search")
dfs(seen, graph, '7')


#----------------------------------------------------------------

graph = {
  'c' : ['b','a'], 
  'b' : ['e', 'd'],
  'a' : ['f'], 
  'e' : [],
  'd' : ['f'],
  'f' : []
}
seen = [] # list to keep track of seen nodes.
queue = []     

# Breadth first search 
def bfs(seen, graph, node):
  seen.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for relative in graph[s]:
      if relative not in seen:
        seen.append(relative)
        queue.append(relative)
print("The following is the Breadth-First search")
bfs(seen, graph, 'c')