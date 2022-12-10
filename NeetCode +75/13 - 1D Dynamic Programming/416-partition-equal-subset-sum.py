'''
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''
from time import time
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        cache = set()
        cache.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            temp_cache = set()
            for t in cache:
                if (t + nums[i]) == target:
                    return True
                temp_cache.add(t + nums[i])
                temp_cache.add(t)
            cache = temp_cache

        return True if target in cache else False

    def reference(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.canPartition(case))
                else:
                    self.canPartition(case)
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
        [1, 5, 11, 5],
        [1, 2, 3, 5]
    ]
    test.quantify(test_cases)
