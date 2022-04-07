class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for i in range(len(prerequisites)):
            des,src = prerequisites[i]
            indegree[des] += 1
            graph[src].append(des)
        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        ans = []
        
        while queue:
            freeCourse = queue.popleft()
            ans.append(freeCourse)
            
            for child in gr aph[freeCourse]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        if len(ans) == numCourses:
            return ans
        return []
# time and space complexity
# time O(n + numofedges)
# space = O(n)