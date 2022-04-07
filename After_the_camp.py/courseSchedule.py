# from collection import deque
class Solution:   
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # indegree = [0]*numCourses
        
        
        for des,src in prerequisites:
            # indegree[des] += 1
            graph[src].append(des)
            
        def cycle(node,tracker,visited):
            tracker[node] = True
            visited[node] = True
            for n in graph[node]:
                if n not in visited and cycle(n,tracker,visited):
                    return True
                if n in tracker:
                    return True
            tracker.pop(node)
            return False
        visited = {}
        for course in range(numCourses):
            tracker = {}
            if course not in visited and cycle(course,tracker,visited):
                return False
        
        return True
        
#         queue = deque()
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)
#         count = 0
#         while queue:
#             curr = queue.popleft()
#             count += 1
            
#             for child in graph[curr]:
#                 indegree[child] -= 1
#                 if indegree[child] == 0:
#                     queue.append(child)
        
#         return count == numCourses
        
                
            