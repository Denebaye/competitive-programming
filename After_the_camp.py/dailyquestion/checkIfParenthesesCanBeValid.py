class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        total = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                total += 1
            else:
                total -= 1
            if total < 0:
                return False
        total = 0
        for i in range(len(s) - 1,-1,-1):
            if locked[i] == '0' or s[i] == ')':
                total += 1
            else:
                total -= 1
            if total < 0:
                return False
        return total % 2 == 0
# space and time complexity
# time = O(n)
# space = O(1)

        
                