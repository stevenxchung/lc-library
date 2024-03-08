'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

from math import inf
from time import time
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                # Min is on the left side or in the middle
                r = mid
            else:
                # Min is on the right side
                l = mid + 1

        # Since sorted, min is always on left index
        return nums[l]

    def reference(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = inf

        while start < end:
            mid = (start + end) // 2
            curr_min = min(curr_min, nums[mid])

            # Right has the min
            if nums[mid] > nums[end]:
                start = mid + 1

            # Left has the  min
            else:
                end = mid - 1

        return min(curr_min, nums[start])

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findMin(case))
                else:
                    self.findMin(case)
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
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        # Additional
        [4, 5, 1, 2, 3],
    ]
    test.quantify(test_cases)
