class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        freq = []
        for key in c.keys():
            freq.append([key,c[key]])
        freq.sort(key = lambda x : x[1])
        freq.reverse()
        x = len(nums)
        t = x/3
        y = len(freq)
        ans = []
        
        for i in range(y):
            if freq[i][1] > t:
                ans.append(freq[i][0])
            else:
                break
           
        
        return ans
                
        