class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heappush(heap,nums[i])
        
        for i in range(k,len(nums)):
            heappushpop(heap,nums[i])
        
        return heappop(heap)
