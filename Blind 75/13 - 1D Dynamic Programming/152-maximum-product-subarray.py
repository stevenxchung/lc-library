'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''
from time import time
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 1
        # Left to right pass. Captures all potential subarrays containing first odd n negative numbers
        for n in nums:
            curr *= n
            res = max(res, curr)
            # 0 is a delimiter, restart at 1. This is optimal since 0 * n is still 0.
            if curr == 0:
                curr = 1
        curr = 1
        # Right to left pass capturing all potential subarrays containing last odd n negative numbers
        for n in reversed(nums):
            curr *= n
            res = max(res, curr)
            if curr == 0:
                curr = 1
        return res

    def reference(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            curMax, curMin = max(n * curMax, n * curMin, n), min(
                n * curMax, n * curMin, n
            )
            res = max(res, curMax)

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxProduct(case))
                else:
                    self.maxProduct(case)
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
    test_cases = [[2, 3, -2, 4], [-2, 0, -1]]
    test.quantify(test_cases)
