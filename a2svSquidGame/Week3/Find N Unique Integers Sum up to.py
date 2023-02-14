class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        num = 1
        while len(output) < n - 1:
            output.append(num)
            num +=1
        
        output.append(-sum(output))
        return output
