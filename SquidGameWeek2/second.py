class Solution:
    def solve(self,word,dp,tracker):
        if word not in tracker: return 0
        if word in dp:return dp[word]
        
        count = 0
        for i in range(len(word)):
            count = max(count,self.solve(word[:i] + word[i + 1:],dp,tracker))
                
        dp[word] = count + 1
        return dp[word]

    def longestStrChain(self, words: List[str]) -> int:
        tracker = set(words)
        dp = {}
        count = 0
        for word in words:
            count = max(count,self.solve(word,dp,tracker))
        
        return count
        
        
        
        
        
        
         