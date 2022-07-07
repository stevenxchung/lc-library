'''
Given a string s, find the length of the longest substring without repeating characters.
'''
from time import time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = i + 1
        longest = 0
        tracking = set()
        while i < len(s) and j < len(s):
            sub_s = s[i:j]
            if len(sub_s) > longest and s[j] not in tracking:
                longest = len(sub_s)
            if s[j] in tracking:
                # Increment indexes and clear set
                i = j
                j = i + 1
                tracking = set()

            # Since j = i + 1 can be > len(s)
            if j < len(s):
                tracking.add(s[j])
            j += 1

        return longest

    def reference(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.lengthOfLongestSubstring(case))
                else:
                    self.lengthOfLongestSubstring(case)
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
        'abcabcbb',
        'bbbbb',
        'pwwkew'
    ]
    test.quantify(test_cases)
