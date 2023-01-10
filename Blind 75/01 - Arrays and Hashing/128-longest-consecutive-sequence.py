'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''
from time import time
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp_set = set(nums)
        count = 1
        longest = 1
        for e in nums:
            # Only check for start of sequence
            if e - 1 not in temp_set:
                next_n = e + 1
                while next_n in temp_set:
                    count += 1
                    next_n += 1
                if count > longest:
                    longest = count
            count = 1

        return longest

    def reference(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.longestConsecutive(case))
                else:
                    self.longestConsecutive(case)
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
    test_cases = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]]
    test.quantify(test_cases)
