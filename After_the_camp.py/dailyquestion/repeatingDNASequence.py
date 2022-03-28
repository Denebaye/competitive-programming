class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        my_Dict = {}
        
        for i in range(len(s)):
            j = i
            temp = s[i]
            if len(s) - i < 10:
                break
            while j + 1< i + 10:
                temp += s[j + 1]
                j += 1
            
            if temp not in my_Dict:
                my_Dict[temp] = 0
            my_Dict[temp] += 1
        
        ans = []
        for string in my_Dict.keys():
            if my_Dict[string] > 1:
                ans.append(string)
        
        return ans
# time and space complexity
# time = O(n)
# space = O(n)