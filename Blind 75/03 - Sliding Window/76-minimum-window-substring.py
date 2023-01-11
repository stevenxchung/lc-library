'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string '.

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''
from math import inf
from time import time


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        window, t_map = {}, {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        # Track characters
        have, need = 0, len(t_map)
        p_window, minLen = [0, 0], inf
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_map and window[c] == t_map[c]:
                have += 1

            while have == need:
                if (r - l + 1) < minLen:
                    p_window = [l, r]
                    minLen = r - l + 1
                # Remove from window and increment left pointer
                window[s[l]] -= 1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1

        l, r = p_window
        return s[l : r + 1] if minLen != inf else ''

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
