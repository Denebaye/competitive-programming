class Solution: 
    def secondsToRemoveOccurrences(self, s: str) -> int:
        max_len = count = prev_max = 0 
        for i, ch in enumerate(s): 
            if ch == '1': 
                max_len = max(prev_max, i - count)
                count += 1
                if max_len: prev_max = max_len+1
        return max_len 
