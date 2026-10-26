
# class Solution(object):
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    #     return [-1, -1]

    
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i

        return [-1, -1]

           