class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #freq = defaultdict(int)
        #for num in nums:
            #freq[num] += 1
        freq = Counter(nums)
        arr = []
        for key in freq.keys():
            arr.append([key,freq[key]])
        
        arr.sort(key = lambda x : x[1])
        arr.reverse()
        ans = []
        for i in range(k):
            ans.append(arr[i][0])
         
        return ans 
            
            
       
        