'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
'''
from time import time
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        cache = [[0] * n for _ in range(n)]

        def calculate(i, j):
            # In memory or gap < 2
            if cache[i][j] or j == i + 1:
                return cache[i][j]

            coins = 0
            # Find the last ballon at j = n - 1
            for k in range(i + 1, j):
                coins = max(coins, nums[i] * nums[k] *
                            nums[j] + calculate(i, k) + calculate(k, j))
            cache[i][j] = coins

            return coins

        # Start from i = 0 and j = n - 1
        return calculate(0, n-1)

    def reference(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + \
                        cache.get((pivot, right), 0)
                    cache[(left, right)] = max(
                        coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxCoins(case))
                else:
                    self.maxCoins(case)
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
        [3, 1, 5, 8],
        [1, 5]
    ]
    test.quantify(test_cases)
