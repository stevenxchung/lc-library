'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''
from time import time


class Solution:
    def checkValidString(self, s: str) -> bool:
        while s != s.replace('()', ''):
            s = s.replace('()', '')

        # Check if ')' before '('
        q = []
        for i in range(len(s)):
            if s[i] in ['(', '*']:
                q.append(1)
            else:
                if q:
                    q.pop()
                else:
                    return False

        # Check if '(' after ')'
        q = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] in [')', '*']:
                q.append(1)
            else:
                if q:
                    q.pop()
                else:
                    return False

        return True

    def reference(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:  # required because -> s = ( * ) (
                leftMin = 0
        return leftMin == 0

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.checkValidString(case))
                else:
                    self.checkValidString(case)
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
        '()',
        '(*)',
        '(*))',
        # Additional
        '(()))(',
        '))((',
    ]
    test.quantify(test_cases)
