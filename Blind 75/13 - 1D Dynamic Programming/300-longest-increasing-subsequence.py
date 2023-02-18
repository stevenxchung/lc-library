'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''
from time import time
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for n in nums:
            # Binary search + DP
            if len(sub) == 0 or n > sub[-1]:
                sub.append(n)
            else:
                # Find the index of the smallest number >= n
                idx = 0
                for i in range(len(sub)):
                    if sub[i] >= n:
                        idx = i
                        break
                # Replace that number with n
                sub[idx] = n
        return len(sub)

    def reference(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.lengthOfLIS(case))
                else:
                    self.lengthOfLIS(case)
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
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
        # Additional
        [4, 10, 4, 3, 8, 9],
    ]
    test.quantify(test_cases)
