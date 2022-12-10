'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
from time import time
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(n_open, n_closed, s=''):
            if n_closed == 0:
                res.append(s)
                return

            elif n_open == 0:
                # Add a closed parentheses
                dfs(n_open, n_closed - 1, s + ')')

            elif n_open == n_closed:
                # Add an open parentheses
                dfs(n_open - 1, n_closed, s + '(')
            else:
                # Add both parentheses
                dfs(n_open - 1, n_closed, s + '(')
                dfs(n_open, n_closed - 1, s + ')')

        dfs(n, n)
        return res

    def reference(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.generateParenthesis(case))
                else:
                    self.generateParenthesis(case)
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
        3,
        1
    ]
    test.quantify(test_cases)
