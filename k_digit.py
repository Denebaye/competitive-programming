class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k != 0:
                stack.pop()
                k -= 1
            
            stack.append(num[i])
            
        for j in range(k):
            stack.pop()
            
        answer = "".join(stack)
        answer = answer.lstrip('0')
        if len(answer) == 0:
            return "0"
        return answer    