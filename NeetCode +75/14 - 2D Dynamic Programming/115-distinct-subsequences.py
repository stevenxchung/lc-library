'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., 'ACE' is a subsequence of 'ABCDE' while 'AEC' is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.
'''
from time import time


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Initialize cache
        cache = [1] * (len(s) + 1)
        # Loop through rows and columns based on length of both strings
        for _, t_char in enumerate(t, 1):
            prev, cache[0] = cache[0], 0
            for c, s_char in enumerate(s, 1):
                # Subsequence count is based on previous results
                curr = cache[c]
                cache[c] = cache[c - 1] + (t_char == s_char and prev)
                prev = curr

        return cache[-1]

    def reference(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]

        return cache[(0, 0)]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.numDistinct(*case))
                else:
                    self.numDistinct(*case)
        print(f'Runtime for our solution: {time() - sol_start}')

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
    test_cases = [('rabbbit', 'rabbit'), ('babgbag', 'bag')]
    test.quantify(test_cases)
