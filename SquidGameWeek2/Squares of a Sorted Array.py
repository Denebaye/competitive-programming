class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []
        pivot = 0
        for i in range(len(nums)):
            temp.append(int(math.pow(nums[i],2)))
            if i and temp[i - 1] > temp[i]:
                pivot = i
                
        p1 = pivot - 1
        p2 = pivot + 1
        ans = []
        ans.append(temp[pivot])
        
        while p1 >= 0 and p2 < len(temp):
            if temp[p1] < temp[p2]:
                ans.append(temp[p1])
                p1 -=1
            else:
                ans.append(temp[p2])
                p2 +=1
            
        while p1 >=0:
            ans.append(temp[p1])
            p1 -=1
        while p2 < len(temp):
            ans.append(temp[p2])
            p2 +=1
        return ans
            
