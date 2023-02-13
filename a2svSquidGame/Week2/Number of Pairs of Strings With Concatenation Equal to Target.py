class Solution:
    def numOfPairs(self, arr: List[str], t: str) -> int:
        f = Counter(arr)
        res = 0
        for k, v in f.items():
            if t.startswith(k):
                suf = t[len(k):]
                res += v * f[suf]
                if k == suf: res -= f[suf]
        return res
