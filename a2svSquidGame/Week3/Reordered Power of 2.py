class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        temp = 1
        domain = []
        while temp < 10**9:
            domain.append(sorted(str(temp)))
            temp *=2
        
        return sorted(str(n)) in domain
        
        
