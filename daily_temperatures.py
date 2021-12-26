class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        Dict = {}
        ans = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                tp = stack.pop()
                Dict[tp] = i - tp
                
            stack.append(i)
            
        for  j in range(len(temperatures)):
            if j in Dict:
                ans.append(Dict[j])
            else:
                ans.append(0)
                
        return ans                