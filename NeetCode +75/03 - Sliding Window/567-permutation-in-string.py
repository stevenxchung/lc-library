'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''
from collections import defaultdict
from time import time


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1_count, c2_count = defaultdict(int), defaultdict(int)
        for c in s1:
            c1_count[c] += 1

        l = 0
        for r in range(len(s2)):
            c2_count[s2[r]] += 1
            if r - l + 1 > len(s1):
                # Shift left pointer when window length exceeded
                c2_count[s2[l]] -= 1
                if c2_count[s2[l]] == 0:
                    # Remove entry if zero
                    del c2_count[s2[l]]
                # Increment last to avoid missing entries
                l += 1

            if c1_count == c2_count:
                # Check after logic above to ensure consistency
                return True

        return False

    def reference(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.checkInclusion(*case))
                else:
                    self.checkInclusion(*case)
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
        ('ab', 'eidbaooo'),
        ('ab', 'eidboaoo'),
        # Additional
        ('hello', 'ooolleoooleh'),
        ('adc', 'dcda'),
    ]
    test.quantify(test_cases)
