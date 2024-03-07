'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

from collections import defaultdict
from time import time


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = defaultdict(int)
        max_c_len = 0
        res = 0

        l = 0
        for r in range(len(s)):
            count_map[s[r]] += 1
            # Next character could be the longest
            max_c_len = max(max_c_len, count_map[s[r]])

            if k < (r - l + 1) - max_c_len:
                # Shrink window if replacements exceeds limit
                count_map[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res

    def reference(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.characterReplacement(*case))
                else:
                    self.characterReplacement(*case)
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
        ('ABAB', 2),
        ('AABABBA', 1),
        # Additional
        ('AAABAAABAAAB', 1),
        ('BBAABBAABBAA', 2),
        ('AAAABAAAABAA', 3),
        ('XXYYZZXXYYZZ', 4),
        ('AAABBCAAABBC', 5),
    ]
    test.quantify(test_cases)
