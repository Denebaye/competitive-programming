class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed = sorted(changed)
        freq = Counter(changed)
        res = []
        # print(changed)
        # print(freq)
        for original in changed:
            if freq[original] > 0:
                if original == 0:
                    if freq[0] % 2 != 0:
                        return []
                    else:
                        freq[0] -= 2
                        res.append(0)
                elif 2*original in freq and freq[2*original] > 0:
                    freq[original] -= 1
                    freq[2*original] -= 1
                    res.append(original)
                else:
                    return []
        
        return res
# space and time complexity
# time = O(n)
# space = O(n)