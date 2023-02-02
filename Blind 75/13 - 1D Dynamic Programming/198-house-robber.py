'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
from time import time
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # There are two choices:
        # 1) Rob nums[i] + nums[i - 2] (current and before previous)
        # 2) Rob nums[i - 1] (previous)
        # The max of these two choices is the max profit
        prev, curr = 0, 0
        for n in nums:
            # After optimizing for O(1) space
            prev, curr = curr, max(curr, prev + n)

        return curr

    def reference(self, nums: List[int]) -> int:
        plan_a, plan_b = 0, 0

        for n in nums:
            temp = max(n + plan_a, plan_b)
            plan_a = plan_b
            plan_b = temp

        return plan_b

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.rob(case))
                else:
                    self.rob(case)
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
    test_cases = [[1, 2, 3, 1], [2, 7, 9, 3, 1]]
    test.quantify(test_cases)
