'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''
from time import time
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        :type nums: List[int]
        :rtype: int
        '''
        res = nums[0]
        current = 1
        # Left to right pass. Captures all potential subarrays containing first odd n negative numbers
        for i in nums:
            current *= i
            res = max(res, current)
            # Zero is a delimiter, restart at 1. This is optimal since zero multiplied on is still zero.
            if current == 0:
                current = 1
        current = 1
        # Right to left pass capturing all potential subarrays containing last odd n negative numbers
        for i in reversed(nums):
            current *= i
            res = max(res, current)
            if current == 0:
                current = 1
        return res

    def reference(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
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
    test_cases = [[2, 3, -2, 4], [-2, 0, -1]]
    test.quantify(test_cases)
