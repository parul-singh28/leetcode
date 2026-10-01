class Solution(object):

    def intersection(self, nums1, nums2):
        ansarr = []

        for i in nums1:
            for j in nums2:
                if i == j:
                    if i not in ansarr:
                        ansarr.append(i)

        return ansarr
        