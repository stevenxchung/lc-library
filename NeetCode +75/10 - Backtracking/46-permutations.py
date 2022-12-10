'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
from time import time
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path: List[int], nums_list: List[int]):
            if not nums_list:
                res.append(path)
                return
            for i in range(len(nums_list)):
                dfs(path + [nums_list[i]], nums_list[:i] + nums_list[i + 1 :])

        dfs([], nums)
        return res

    def reference(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.reference(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.permute(case))
                else:
                    self.permute(case)
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
    test_cases = [[1, 2, 3], [0, 1], [1]]
    test.quantify(test_cases)
