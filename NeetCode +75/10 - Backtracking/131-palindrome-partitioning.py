'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
'''
from time import time
from typing import List


class Solution:
    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def dfs(i: int):
            if i >= len(s):
                res.append(temp[:])
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    temp.append(s[i:j + 1])
                    dfs(j + 1)
                    temp.pop()

        dfs(0)
        return res

    def reference(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.partition(case))
                else:
                    self.partition(case)
        print(f'Runtime for our solution: {time() - sol_start}')

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
    test_cases = [
        'aab',
        'a'
    ]
    test.quantify(test_cases)
