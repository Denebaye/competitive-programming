class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack = []
        ans = []
        curridx = 0
        flag = False
        
        for i in range(len(s)):
            idx = i + 1
            for j in range(idx,len(s)):
                if s[i] == s[j]:
                    idx = j + 1
                    flag = True
            if not flag and len(stack) == 0:
                ans.append(idx - curridx)
                curridx = idx
            if not flag and stack and stack[-1] == idx:
                ans.append(stack.pop() - curridx)
                curridx = idx
            if flag and stack and stack[-1] < idx:
                stack.pop()
                stack.append(idx)
            if flag and len(stack) == 0:
                stack.append(idx)
            flag = False
        
        return ans
# space and time complexity
# space = O(1)
# time = O(n^2)
                