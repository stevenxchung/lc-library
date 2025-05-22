'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

from time import time
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax, rightMax = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            # Water level is limited by shorter wall
            if height[l] < height[r]:
                if height[l] > leftMax:
                    leftMax = height[l]
                else:
                    res += leftMax - height[l]
                l += 1
            else:
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    res += rightMax - height[r]
                r -= 1

        return res

    def reference(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.trap(case))
                else:
                    self.trap(case)
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
    test_cases = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 0, 3, 2, 5]]
    test.quantify(test_cases)
