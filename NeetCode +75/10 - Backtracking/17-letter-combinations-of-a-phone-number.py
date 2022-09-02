'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
from time import time
from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        res = []
        if len(digits) == 0:
            return res

        def dfs(i: int, curr: List[str]):
            if len(digits) == len(curr):
                res.append(''.join(curr))
                return
            for c in phone_map[digits[i]]:
                curr.append(c)
                dfs(i + 1, curr)
                curr.pop()

        dfs(0, [])
        return res

    def reference(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.letterCombinations(case))
                else:
                    self.letterCombinations(case)
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
        '23',
        '',
        '2'
    ]
    test.quantify(test_cases)
