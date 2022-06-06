class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left = right = 0
        length = 0

        while right < len(s):
            while s[right] in mySet:
                mySet.remove(s[left])
                left +=1
            mySet.add(s[right])
            right +=1
            length = max(length,right - left)
          
        
        return length
            
        
# time and space complexity
# time = O(n) time complexity
# space = O(n)
