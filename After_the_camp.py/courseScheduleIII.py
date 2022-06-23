class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x : x[1])
        total = 0
        heap = []
        count = 0
        for dur,dl in courses:
            if dur > dl : continue
            
            total +=dur
            
            if total > dl:
                heappush(heap,-dur)
                total +=heappop(heap)
            else:
                count +=1
                heappush(heap,-dur)
        
        return count
