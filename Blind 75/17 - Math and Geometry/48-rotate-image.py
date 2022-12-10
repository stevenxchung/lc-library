'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''
from time import time
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]):
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # Save top left
                top_left = matrix[top][l + i]
                # Move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # Move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # Move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # Move top left to top right
                matrix[top + i][r] = top_left
            r -= 1
            l += 1

        return matrix

    def reference(self, matrix: List[List[int]]):
        matrix[:] = zip(*matrix[::-1])
        return matrix

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.rotate(case))
                else:
                    self.rotate(case)
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
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ]
    test.quantify(test_cases)
