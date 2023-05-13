'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
from time import time
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, seen = [], set()

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for n in nums:
                if n in seen:
                    continue
                seen.add(n)
                dfs(subset + [n])
                seen.remove(n)

        dfs([])
        return res

    def reference(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(temp, subset):
            if not temp:
                # Ran out of numbers to select
                res.append(subset[:])
                return

            for i in range(len(temp)):
                # Select from reduced copy of integers
                dfs(temp[:i] + temp[i + 1 :], subset + [temp[i]])

            return

        dfs(nums, [])
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.permute(case))
                else:
                    self.permute(case)
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
    test_cases = [[1, 2, 3], [0, 1], [1]]
    test.quantify(test_cases)
