
class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)

        ans = [1] * n

        # Step 1: Calculate prefix products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Step 2: Calculate suffix products
        suffix = 1

        for i in range(n - 2, -1, -1):
            suffix = suffix * nums[i + 1]
            ans[i] = ans[i] * suffix

        return ans        