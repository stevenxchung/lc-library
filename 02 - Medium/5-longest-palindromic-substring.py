'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''


class Solution:
    def longestPalindrome(self, s):
        longestSeenPalindrome = ''
        for i in range(len(s)):
            # Where self.palindrome(s, i, i) is for odd number of characters
            # and self.palindrome(s, i, i + 1) is for even number of characters
            longestSeenPalindrome = max(self.palindrome(s, i, i), self.palindrome(
                s, i, i + 1), longestSeenPalindrome, key=len)

        return longestSeenPalindrome

    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            # print(s[left + 1: right])
        return s[left + 1:right]


sol = Solution()
print(sol.longestPalindrome('alibaba'))
