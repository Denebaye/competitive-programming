class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 1:
            return self.get_kth_smallest(nums1, nums2, total_length // 2)
        else:
            return (self.get_kth_smallest(nums1, nums2, total_length // 2 - 1) + self.get_kth_smallest(nums1, nums2, total_length // 2)) / 2.0

    def get_kth_smallest(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if not nums1:
            return nums2[k]

        if k == len(nums1) + len(nums2) - 1:
            return max(nums1[-1], nums2[-1])

        mid_index1 = len(nums1) // 2
        mid_index2 = k - mid_index1

        if nums1[mid_index1] > nums2[mid_index2]:
            return self.get_kth_smallest(nums1[:mid_index1], nums2[mid_index2:], mid_index1)
        else:
            return self.get_kth_smallest(nums1[mid_index1:], nums2[:mid_index2], mid_index2)
