'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, 'ace' is a subsequence of 'abcde'.

A common subsequence of two strings is a subsequence that is common to both strings.
'''
from time import time


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0] * len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        cache[i][j] = 1
                    else:
                        cache[i][j] = 1 + cache[i - 1][j - 1]
                else:
                    cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

        return cache[-1][-1]

    def reference(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.longestCommonSubsequence(*case))
                else:
                    self.longestCommonSubsequence(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [('abcde', 'ace'), ('abc', 'abc'), ('abc', 'def')]
    test.quantify(test_cases)
