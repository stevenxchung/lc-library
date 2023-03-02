'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

- For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression '+2-1'.

Return the number of different expressions that you can build, which evaluates to target.
'''
from collections import defaultdict
from time import time
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums or sum(nums) < target:
            return 0

        cache = {0: 1}  # {total : count}
        for n in nums:
            # Build new cache based on possible decisions (+ or -)
            temp = defaultdict(int)
            for k in cache:
                temp[k + n] += cache[k]
                temp[k - n] += cache[k]
            cache = temp

        return cache[target]

    def reference(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findTargetSumWays(*case))
                else:
                    self.findTargetSumWays(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [([1, 1, 1, 1, 1], 3), ([1], 1)]
    test.quantify(test_cases)
