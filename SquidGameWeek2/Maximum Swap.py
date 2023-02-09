class Solution:
    def maximumSwap(self, originalNumber):
        
        digitList = [int(x) for x in str(originalNumber)]
        maxIndex = len(digitList) - 1
        firstIndex = secondIndex = 0
        for i in range(len(digitList) - 1, -1, -1):
            if digitList[i] > digitList[maxIndex]:
                maxIndex = i
            elif digitList[i] < digitList[maxIndex]:
                firstIndex = i
                secondIndex = maxIndex
        digitList[firstIndex], digitList[secondIndex] = digitList[secondIndex], digitList[firstIndex]
        return int(''.join([str(x) for x in digitList]))
