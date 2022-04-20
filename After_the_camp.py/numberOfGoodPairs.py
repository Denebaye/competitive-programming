class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0      
        freq = Counter(nums)
        
        for val,frq in freq.items(): 
            counter += frq*(frq - 1)//2
        
        return counter
# space and time complexity
# space = O(n)
# time = O(n)