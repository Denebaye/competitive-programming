class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        #O(nlog(n)) time complexity and O(n) space complexity using heap
        """"heap = []
        for key,val in frequency.items():
            heapq.heappush(heap,(-val,key))
        ans = []
        for i in range(k):
            x = heapq.heappop(heap)
            ans.append(x[1])
        
        return ans"""
        # using list
        lst = []
        for key,val in frequency.items():
            lst.append((-val,key))
        
        lst.sort()
        ans = []
        
        for i in range(k):
            ans.append(lst[i][1])
            
        return ans 
        
        