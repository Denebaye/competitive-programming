class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(s,l,r):
            flag = False
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -=1
                r +=1
                flag = True
            if flag:
                return (l +1,r)
            return (l,r)
        
        start,end = 0,1
        mx = 1
        for i in range(len(s)):
            odd_pal = pal(s,i,i)
            even_pal = pal(s,i,i +1)            
            
            if mx < (odd_pal[1] - odd_pal[0]):
                start,end = odd_pal[0],odd_pal[1]
                mx = max(mx,end - start)
                
            if mx < (even_pal[1] - even_pal[0]):
                start,end = even_pal[0],even_pal[1]
                mx = max(mx,end - start)
        
        return s[start:end]
# time and space complexity
# time = O(n^2)
# space = O(1)