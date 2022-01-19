class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(stack) != 0 and stack[-1] == "(" and s[i] == ")":
                stack.pop()
                continue
            elif len(stack) != 0 and stack[-1] == "[" and s[i] == "]":
                stack.pop()
                continue
            elif len(stack) != 0 and stack[-1] == "{" and s[i] == "}":
                stack.pop()
                continue
            else:
                stack.append(s[i])
                
      
        return len(stack) == 0            