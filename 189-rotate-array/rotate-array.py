class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """

        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]
        