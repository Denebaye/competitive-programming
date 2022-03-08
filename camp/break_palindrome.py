class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        if N == 1:
            return ""
        
        idx = N
        ptr = (N - 1)//2
        while ptr >= 0: 
            if palindrome[ptr] != "a":
                idx = ptr
            ptr -= 1
        
        
        if idx != N and N % 2 == 0:
            return palindrome[:idx] + "a" + palindrome[idx + 1:]
        elif idx != N and idx != (N - 1)//2:
            return palindrome[:idx] + "a" + palindrome[idx + 1:]
        else:
            return palindrome[:N - 1] + "b"
        #time and space complexity
        # time = O(n)
        # space = O(1)        
                
                
        
        