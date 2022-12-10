'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
from time import time
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        # Monotonically increasing stack
        stack = []

        for i, h in enumerate(heights):
            start = i
            # Remove from the stack when current height is smaller
            while stack and stack[-1][-1] > h:
                i_prev, h_prev = stack.pop()
                max_area = max(max_area, h_prev * (i - i_prev))
                # Reassign start to previous index
                start = i_prev
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

    def reference(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.largestRectangleArea(case))
                else:
                    self.largestRectangleArea(case)
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
        [2, 1, 5, 6, 2, 3],
        [2, 4]
    ]
    test.quantify(test_cases)
