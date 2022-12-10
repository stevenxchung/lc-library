'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
from time import time
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Needs to be in order to eliminate duplicates
        nums.sort()
        res = []

        def dfs(i1: int, subset: List[int]):
            res.append(subset[:])
            for i2 in range(i1, len(nums)):
                if i2 != i1 and nums[i2] == nums[i2 - 1]:
                    # Skip if duplicate
                    continue
                dfs(i2 + 1, subset + [nums[i2]])

        dfs(0, [])
        return res

    def reference(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.subsetsWithDup(case))
                else:
                    self.subsetsWithDup(case)
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
    test_cases = [[1, 2, 2], [0]]
    test.quantify(test_cases)
