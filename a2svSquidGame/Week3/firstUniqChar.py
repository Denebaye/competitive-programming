class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = Counter(s)
        for idx,c in enumerate(s):
            if frequency[c] == 1:
                return idx
        
        return -1
