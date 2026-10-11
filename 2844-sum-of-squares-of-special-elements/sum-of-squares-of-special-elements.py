
class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        sumofsquare = 0

        for i in range(n):
            if n % (i + 1) == 0:
                square = nums[i] * nums[i]
                sumofsquare += square

        return sumofsquare

        