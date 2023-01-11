'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''
from time import time
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = [s]
        found = set()
        while queue:
            s = queue.pop(0)
            for w in wordDict:
                if s.startswith(w):
                    s_new = s[len(w) :]
                    if s_new == '':
                        return True
                    if s_new not in found:
                        queue.append(s_new)
                        found.add(s_new)

        return False

    def reference(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.wordBreak(*case))
                else:
                    self.wordBreak(*case)
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
    test_cases = [
        ('leetcode', ['leet', 'code']),
        ('applepenapple', ['apple', 'pen']),
        ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']),
        # Additional
        ('bb', ['a', 'b', 'bbb', 'bbbb']),
        ('aaaaaaa', ['aaaa', 'aaa']),
        ('aaaaaa', ['aa', 'a']),
    ]
    test.quantify(test_cases)
