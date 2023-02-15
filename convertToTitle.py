class Solution:
    def convertToTitle(self, num):
        capitals = []
        for x in range(ord('A'), ord('Z')+1):
            capitals.append(chr(x))
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
