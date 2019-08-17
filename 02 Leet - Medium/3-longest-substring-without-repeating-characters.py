'''
Given a string, find the length of the longest substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        longest = seen = 0
        observed = {}
        while i < len(s):
            if s[i] in observed and seen <= observed[s[i]]:
                seen = observed[s[i]] + 1
            else:
                longest = max(longest, i - seen + 1)
            observed[s[i]] = i
            i += 1

        return longest


# input = 'abcabcbb'
# input = 'bbbbb'
# input = 'pwwkew'
# input = 'aab'
input = 'dvdf'
sol = Solution()
print(sol.lengthOfLongestSubstring(input))
