# class Solution(object):

#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         for i in range(len(s)):
#             if s.count(s[i]) == 1:
#                 return i

#         return -1  
# class Solution(object):

#     def firstUniqChar(self, s):
        
#         visit = set()

#         for i in s:
#             visit.add(i)

#         for i in range(len(s)):
#             if s.count(s[i]) == 1:
#                 return i

#         return -1
        
class Solution(object):

    def firstUniqChar(self, s):
        count = {}

        # Count frequency
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # Find first character with frequency 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1