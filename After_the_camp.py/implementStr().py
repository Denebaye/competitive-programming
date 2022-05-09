class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        window_size = len(needle)
        if window_size==0:
            return 0
        while left+window_size <= len(haystack):
            if haystack[left:left+window_size] == needle:
                return left
            else:
                left+=1
        return -1