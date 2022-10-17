'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
import collections
from time import time
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:
            # Initialize map
            a2z_hash_key = [0] * 26
            for l in word:
                a2z_hash_key[ord(l) - ord('a')] += 1

            a2z_hash_key = str(a2z_hash_key)
            if a2z_hash_key not in buckets:
                buckets[a2z_hash_key] = [word]
            else:
                buckets[a2z_hash_key].append(word)

        return [group for group in buckets.values()]

    def reference(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.groupAnagrams(case))
                else:
                    self.groupAnagrams(case)
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
        ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
        [''],
        ['a'],
    ]
    test.quantify(test_cases)
