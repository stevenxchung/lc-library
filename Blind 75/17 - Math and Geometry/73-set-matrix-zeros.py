'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''
from copy import deepcopy
from time import time
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Mark existing matrix row or column if zero
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        # If already a zero then whole row is zero
                        row_zero = True

        # Skip first row and column since we check that later
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    # Zero out any marked row or column
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            # Zero out first row
            for r in range(ROWS):
                matrix[r][0] = 0

        if row_zero:
            # Zero out first column
            for c in range(COLS):
                matrix[0][c] = 0

        return matrix

    def reference(self, matrix: List[List[int]]):
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        return matrix

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.setZeroes(copy))
                else:
                    self.setZeroes(copy)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(copy))
                else:
                    self.reference(copy)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    ]
    test.quantify(test_cases)
