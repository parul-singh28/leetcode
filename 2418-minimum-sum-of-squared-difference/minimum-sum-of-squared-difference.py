
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2

            needed = sum(max(0, x - mid) for x in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left

        used = sum(max(0, x - level) for x in diff)
        remaining = k - used

        ans = sum(min(x, level) ** 2 for x in diff)

        ans -= remaining * (2 * level - 1)

        return ans


