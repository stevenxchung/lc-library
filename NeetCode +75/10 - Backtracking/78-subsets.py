'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
from time import time
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i: int, subset: List[int]):
            if i == len(nums):
                res.append(subset[:])
                return

            dfs(i + 1, subset + [nums[i]])
            dfs(i + 1, subset)

            return

        dfs(0, [])
        return res

    def reference(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # Decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.subsets(case))
                else:
                    self.subsets(case)
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
    test_cases = [[1, 2, 3], [0]]
    test.quantify(test_cases)
