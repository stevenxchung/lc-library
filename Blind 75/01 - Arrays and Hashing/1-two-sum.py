'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
from time import time
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, e in enumerate(nums):
            diff = target - e
            if diff in complements:
                return [complements[diff], i]
            complements[e] = i

    def reference(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]

    sol_start = time()
    for case in test_cases:
        print(test.twoSum(case[0], case[1]))
    print(f'Runtime for our solution: {time() - sol_start}')

    ref_start = time()
    for case in test_cases:
        print(test.reference(case[0], case[1]))
    print(f'Runtime for reference: {time() - ref_start}')
