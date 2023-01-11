'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
from time import time
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, max_area = 0, 0
        i, j = 0, len(height) - 1
        while i < j:

            if height[i] < height[j]:
                area = height[i] * (j - i)
            else:
                area = height[j] * (j - i)

            if area > max_area:
                max_area = area

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area

    def reference(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxArea(case))
                else:
                    self.maxArea(case)
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
    test_cases = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1]]
    test.quantify(test_cases)
