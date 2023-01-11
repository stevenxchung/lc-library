'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
'''
from time import time


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize cache
        h, w = len(word1) + 1, len(word2) + 1
        cache = [i for i in range(w)]
        for i in range(1, h):
            cur = [i for _ in range(w)]
            for j in range(1, w):
                # Sub-operation is based on min of previous operations
                cur[j] = min(
                    cache[j - 1] + (word1[i - 1] != word2[j - 1]),
                    cache[j] + 1,
                    cur[j - 1] + 1,
                )
            # Update cache after each loop
            cache = cur

        return cache[-1]

    def reference(self, word1: str, word2: str) -> int:
        dp = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]
                    )
        return dp[0][0]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minDistance(*case))
                else:
                    self.minDistance(*case)
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
    test_cases = [('horse', 'ros'), ('intention', 'execution')]
    test.quantify(test_cases)
