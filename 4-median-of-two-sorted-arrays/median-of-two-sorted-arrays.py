class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sortedarr = nums1 + nums2
        sortedarr.sort()

        n = len(sortedarr)

        if n % 2 == 0:
            median = (sortedarr[n // 2 - 1] + sortedarr[n // 2]) / 2.0
        else:
            median = sortedarr[n // 2]

        return median

        