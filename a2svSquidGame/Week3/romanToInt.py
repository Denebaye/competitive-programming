class Solution:
    def romanToInt(self, s: str) -> int:
        whare = {"I" : 1,
                 "V" : 5,
                 "X" : 10 ,
                 "L" : 50 ,
                 "C" : 100 ,
                 "D" : 500,
                 "M" : 1000 }
        outPut = 0
        idx = 0
        while idx < len(s):
            c = s[idx]
            if idx + 1 < len(s) and whare[s[idx + 1]] > whare[c]:
                outPut +=(whare[s[idx + 1]] - whare[c])
                idx +=2
            else:
                outPut +=whare[c]
                idx +=1
        
        return outPut
                
