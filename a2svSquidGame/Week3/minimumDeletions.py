class Solution:
    def minimumDeletions(self,string: str) -> int:
        count_b = 0
        min_deletions = [0]
        for char in string:
            if char == 'b':
                count_b += 1
                min_deletions.append(min_deletions[-1])
            else:
                min_deletions.append(min(count_b, min_deletions[-1] + 1))
        return min_deletions[-1]
