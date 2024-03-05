'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

from time import time
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res

        # Sorting input takes O(n*log(n)), algorithm below takes O(n^2)
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicates
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                a, b, c = nums[i], nums[l], nums[r]
                total = a + b + c
                if total == 0:
                    res.append([a, b, c])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        # Skip duplicates
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res

    def reference(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.threeSum(case))
                else:
                    self.threeSum(case)
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
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        # Additional
        [],
        [0],
        [0, 0, 0, 0],
        [-2, 0, 1, 1, 2],
    ]
    test.quantify(test_cases)
