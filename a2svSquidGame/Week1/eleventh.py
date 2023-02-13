class Solution:
    def __init__(self, weight_list: List[int]):
        """
        :type weight_list: List[int]
        """
        self.prefix_sums = []
        current_sum = 0
        for weight in weight_list:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
