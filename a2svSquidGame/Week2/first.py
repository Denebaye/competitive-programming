class Solution:
    def helper(self,word,prefix):
        ptr = 0
        if len(word) < len(prefix):
            return False

        while ptr < len(prefix):
            if prefix[ptr] != word[ptr]:
                return False
            ptr +=1
        
        return True

    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if self.helper(word,pref):
                count +=1
        
        return count
        