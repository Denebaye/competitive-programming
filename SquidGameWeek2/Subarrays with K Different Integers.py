class Solution:    
    def subarraysWithKDistinct(self, arr, k):
        return self.numSubarraysAtMostK(arr, k) - self.numSubarraysAtMostK(arr, k - 1)

    def numSubarraysAtMostK(self, arr, k):
        count = collections.Counter()
        res = left = 0
        for right in range(len(arr)):
            if count[arr[right]] == 0: k -= 1
            count[arr[right]] += 1
            while k < 0:
                count[arr[left]] -= 1
                if count[arr[left]] == 0: k += 1
                left += 1
            res += right - left + 1
        return res
