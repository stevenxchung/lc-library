'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
from time import time


class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in pair:
                stack.append(c)
            elif pair[stack[-1]] == c:
                stack.pop()
            elif pair[stack[-1]] != c:
                return False

        # Check edge case
        if len(stack) > 0:
            return False

        return True

    def reference(self, s: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c not in bracket_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != bracket_map[c]:
                return False
            stack.pop()

        return not stack

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isValid(case))
                else:
                    self.isValid(case)
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
    test_cases = [
        '()',
        '()[]{}',
        '(]',
        # Additional
        '(()',
        '[()',
    ]
    test.quantify(test_cases)
