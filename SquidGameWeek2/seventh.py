class Solution:
    def minOperations(self, directoryLogs: List[str]) -> int:
        numSteps = 0
        for entry in directoryLogs: 
            if entry == "./": continue
            elif entry == "../": numSteps = max(0, numSteps-1) # parent directory
            else: numSteps += 1 # child directory 
        return numSteps 
