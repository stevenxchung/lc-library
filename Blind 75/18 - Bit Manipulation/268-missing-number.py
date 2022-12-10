'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
from time import time
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

    def reference(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.missingNumber(case))
                else:
                    self.missingNumber(case)
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
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1]
    ]
    test.quantify(test_cases)
