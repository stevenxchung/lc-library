'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
from time import time
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        minimum = nums[0]
        while i <= j:
            m = (i + j) // 2
            if nums[i] < nums[j]:
                if nums[i] < minimum:
                    minimum = nums[i]
                    break

            if nums[m] >= nums[i]:
                # Search right
                i = m + 1
            else:
                # Otherwise search left
                j = m - 1

        return minimum

    def reference(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findMin(case))
                else:
                    self.findMin(case)
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
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17]
    ]
    test.quantify(test_cases)
