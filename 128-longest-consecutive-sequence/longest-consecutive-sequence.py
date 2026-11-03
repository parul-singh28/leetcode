
class Solution:
    def longestConsecutive(self, nums):
        
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)

        current = 1
        longest = 1

        for i in range(1, len(sorted_nums)):

            if sorted_nums[i] == sorted_nums[i - 1]:
                continue

            elif sorted_nums[i] == sorted_nums[i - 1] + 1:
                current += 1

            else:
                current = 1

            longest = max(longest, current)

        return longest

   