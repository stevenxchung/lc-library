'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
from time import time
from typing import List


class Solution:
    def rob_helper(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for n in nums:
            prev, curr = curr, max(prev + n, curr)
        return curr

    def rob(self, nums: List[int]) -> int:
        return max(
            nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1])
        )

    def reference_helper(self, nums: List[int]) -> int:
        plan_a, plan_b = 0, 0

        for n in nums:
            temp = max(n + plan_a, plan_b)
            plan_a = plan_b
            plan_b = temp

        return plan_b

    def reference(self, nums: List[int]) -> int:
        return max(
            nums[0],
            self.reference_helper(nums[1:]),
            self.reference_helper(nums[:-1]),
        )

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
    test_cases = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [1, 2, 3],
        # Additional
        [1],
    ]
    test.quantify(test_cases)
