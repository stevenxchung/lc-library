'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> '1'
'B' -> '2'
...
'Z' -> '26'

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, '11106' can be mapped into:

- 'AAJF' with the grouping (1 1 10 6)
- 'KJF' with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because '06' cannot be mapped into 'F' since '6' is different from '06'.

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
'''
from time import time


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        # The number of ways to decode at index 0 is 1
        prev, curr = 1, 1
        for i in range(1, len(s)):
            temp = curr
            if s[i] == '0':
                # Skip by setting to 0 since there's only 1 way to decode
                curr = 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                # Adds n previous ways to decode if in a-z range
                curr += prev
            prev = temp

        return curr

    def reference(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.numDecodings(case))
                else:
                    self.numDecodings(case)
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
        '12',
        '226',
        '06',
        # Additional
        '101',
        '888',
        '2263',
        '22226',
    ]
    test.quantify(test_cases)
