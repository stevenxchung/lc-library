'''
Given a string s, find the length of the longest substring without repeating characters.
'''
from time import time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest, curr = 0, 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                curr -= 1
            seen.add(s[r])
            curr += 1
            longest = max(longest, curr)

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

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.lengthOfLongestSubstring(case))
                else:
                    self.lengthOfLongestSubstring(case)
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
    test_cases = ['abcabcbb', 'bbbbb', 'pwwkew']
    test.quantify(test_cases)
