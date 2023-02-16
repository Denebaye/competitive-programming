class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        half = n//2
        if n % 2:
            return []
        changed.sort()
        tracker = defaultdict(int)
        outPut = []
        for num in changed:
            if num/2 in tracker and tracker[num/2] > 0:
                tracker[num/2] -=1
                outPut.append(int(num/2))
            else:
                tracker[num] +=1
                
        return outPut if len(outPut) == half else []
                
        
