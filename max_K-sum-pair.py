
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        domain = set()
        ans = 0
        for x in c:
            if x not in domain and (k - x) in c:
                if x == (k - x):
                    ans += c[x]//2
                else:
                    ans += min(c[x],c[k - x])
                domain.add(x)
                domain.add(k - x)
         
        return ans