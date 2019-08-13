'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''


class Solution:
    def longestPalindrome(self, s):
        longestSeenPalindrome = ''
        for i in range(len(s)):
            longestSeenPalindrome = max(self.helper(s, i, i), self.helper(
                s, i, i + 1), longestSeenPalindrome, key=len)

        return longestSeenPalindrome

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


sol = Solution()
print(sol.longestPalindrome('babad'))
