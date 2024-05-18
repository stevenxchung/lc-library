'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string '.

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''

from collections import Counter
from time import time


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize overall count map with t
        count_map = Counter(t)
        required = sum(count_map.values())
        start, end = 0, 0
        l = 0
        for r, c in enumerate(s, 1):
            if count_map[c] > 0:
                required -= 1

            # Can be negative (character is not required)
            count_map[c] -= 1

            # Window contains all characters, reduce window to minimum
            if required == 0:
                # Shrink until we reach required character
                while l < r and count_map[s[l]] < 0:
                    count_map[s[l]] += 1
                    l += 1

                # Update window size if smaller than existing
                if end == 0 or r - l < end - start:
                    start, end = l, r

                # Moving right one more loses a required character
                count_map[s[l]] += 1
                required += 1
                l += 1

        return s[start:end]

    def reference(self, s: str, t: str) -> str:
        if t == '':
            return ''

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # Update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # Pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float('infinity') else ''

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minWindow(*case))
                else:
                    self.minWindow(*case)
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
    test_cases = [('ADOBECODEBANC', 'ABC'), ('a', 'a'), ('a', 'aa')]
    test.quantify(test_cases)
