# from collection import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        
        for i in range(len(prerequisites)):
            des,src = prerequisites[i]
            indegree[des] += 1
            graph[src].append(des)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            
            for child in graph[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return count == numCourses
        
                
            