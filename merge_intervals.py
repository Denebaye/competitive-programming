class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        i = 0
        
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            while i + 1 < len(intervals) and intervals[i][1] >= intervals[i + 1][0]:
                if intervals[i][1] >= intervals[i + 1][1]:
                    intervals[i + 1][1] = intervals[i][1]
                    end = intervals[i][1]
                else: 
                    end = max(intervals[i][1],intervals[i + 1][1])
                i += 1
            
            ans.append([start,end])
            i += 1
        return ans    