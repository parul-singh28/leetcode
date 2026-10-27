class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = sorted(freq, key=freq.get, reverse=True)

        return result[:k]
                 