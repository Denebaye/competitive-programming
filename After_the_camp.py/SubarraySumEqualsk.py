class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tracker = defaultdict(int)
        tracker[0] +=1
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            if prefix - k in tracker:
                count +=tracker[prefix - k]
            tracker[prefix] +=1
                
        return count
            
    