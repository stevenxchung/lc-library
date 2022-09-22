'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''
from time import time


class Solution:
    def minWindowOld(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        have, need = 0, 0
        t_hash = {c: 0 for c in t}
        for c in t:
            if c in t_hash:
                need += 1
                t_hash[c] += 1

        window = {c: 0 for c in t}
        # for c in t:
        #     if c in window:
        #         window[c] += 1

        i, j = 0, 0
        min_i, min_j = 0, 0
        min_length = len(s)
        s_length = len(s)
        last_s_added = False
        while i < s_length:
            sub_s = s[i:j + 1]
            # Move left pointer
            if (have == need or j == s_length - 1) and s[i] in window:
                window[s[i]] -= 1
                if window[s[i]] != t_hash[s[i]]:
                    have -= 1
                i += 1
            elif j == s_length - 1:
                if s[i] in window:
                    window[s[i]] += 1
                    if window[s[i]] == t_hash[s[i]]:
                        have += 1
                i += 1

            if j < s_length - 1:
                if s[j] in window:
                    window[s[j]] += 1
                    if window[s[j]] == t_hash[s[j]]:
                        have += 1
                j += 1

            # Edge case
            if not last_s_added and j == s_length - 1 and s[j] in window:
                window[s[j]] += 1
                if window[s[j]] == t_hash[s[j]]:
                    have += 1
                last_s_added = True

            if have == need and len(sub_s) < min_length:
                min_length = len(sub_s)
                min_i, min_j = i, j

        return s[min_i: min_j + 1]

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        have, need = 0, 0
        t_hash = {c: 0 for c in t}
        for c_right in t:
            if c_right in t_hash:
                need += 1
                t_hash[c_right] += 1

        window = {c: 0 for c in t}
        # for c in t:
        #     if c in window:
        #         window[c] += 1

        i = 0
        min_i, min_j = 0, 0
        min_length = len(s)
        for j in range(len(s)):
            c_right = s[j]
            window[c_right] = 1 + window.get(c_right, 0)
            if c_right in t_hash and window[c_right] == t_hash[c_right]:
                have += 1

            while have == need:
                sub_s = s[i:j + 1]
                if len(sub_s) < min_length:
                    min_i, min_j = i, j
                    min_length = len(sub_s)

                # Move left pointer
                c_left = s[i]
                window[c_left] -= 1
                if c_left in t_hash and window[c_left] < t_hash[c_left]:
                    have -= 1
                i += 1

        return s[min_i: min_j + 1]

    def reference(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
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
                    resLen = (r - l + 1)
                # Pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minWindow(case[0], case[1]))
                else:
                    self.minWindow(case[0], case[1])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1]))
                else:
                    self.reference(case[0], case[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ('ADOBECODEBANC', 'ABC'),
        ('a', 'a'),
        ('a', 'aa')
    ]
    test.quantify(test_cases)
