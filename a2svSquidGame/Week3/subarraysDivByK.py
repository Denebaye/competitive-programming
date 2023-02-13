class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_frequency = defaultdict(int)
        remainder_frequency[0] = 1
        result = running_sum = 0
        for number in nums:
            running_sum += number
            current_remainder = running_sum % k
            result += remainder_frequency[current_remainder]
            remainder_frequency[current_remainder] += 1
        return result
