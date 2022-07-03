'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
from time import time


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashed = set(e for e in s)
        for e in t:
            if e not in s_hashed:
                return False
        return True

    def reference(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ('anagram', 'nagaram'),
        ('rat', 'car')
    ]

    sol_start = time()
    for case in test_cases:
        print(test.isAnagram(case[0], case[1]))
    print(f'Runtime for our solution: {time() - sol_start}')

    ref_start = time()
    for case in test_cases:
        print(test.reference(case[0], case[1]))
    print(f'Runtime for reference: {time() - ref_start}')
