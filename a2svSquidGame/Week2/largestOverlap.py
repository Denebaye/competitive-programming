class Solution:
    def largestOverlap(self, image1, image2):
        rows = len(image1)
        non_zero_indices_a = []
        non_zero_indices_b = []

        for i in range(rows * rows):
            row = i // rows
            col = i % rows

            if image1[row][col]:
                non_zero_indices_a.append(row * 100 + col)

            if image2[row][col]:
                non_zero_indices_b.append(row * 100 + col)

        difference_counter = collections.Counter(
            i - j for i in non_zero_indices_a for j in non_zero_indices_b)
        return max(difference_counter.values() or [0])
