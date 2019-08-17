'''
Given a string, find the length of the longest substring without repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        longest = start = 0
        observed = {}
        while i < len(s):
            if s[i] in observed and start <= observed[s[i]]:
                start = observed[s[i]] + 1
            else:
                longest = max(longest, i - start + 1)
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
