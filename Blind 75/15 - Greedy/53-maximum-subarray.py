'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''
from time import time
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = 0
        current_sum = 0
        for n in nums:
            current_sum = max(0, current_sum + n)
            best_sum = max(best_sum, current_sum)
        return best_sum

    def reference(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxSubArray(case))
                else:
                    self.maxSubArray(case)
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
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8]
    ]
    test.quantify(test_cases)
