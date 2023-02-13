'''
Given a string s, return the longest palindromic substring in s.
'''
from time import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        IN_BOUNDS = range(len(s))
        res = s[0]
        for i in IN_BOUNDS:
            # Odd palindromes
            j = i
            while i in IN_BOUNDS and j in IN_BOUNDS and s[i] == s[j]:
                if len(s[i : j + 1]) > len(res):
                    res = s[i : j + 1]
                i -= 1
                j += 1

            # Even palindromes
            j = i + 1
            while i in IN_BOUNDS and j in IN_BOUNDS and s[i] == s[j]:
                if len(s[i : j + 1]) > len(res):
                    res = s[i : j + 1]
                i -= 1
                j += 1

        return res

    def reference(self, s: str) -> str:
        res = ''
        resLen = 0

        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.longestPalindrome(case))
                else:
                    self.longestPalindrome(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = ['babad', 'cbbd']
    test.quantify(test_cases)
