'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
'''
from time import time
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t_row, b_row = 0, len(matrix) - 1
        l_col, r_col = 0, len(matrix[0]) - 1
        while t_row <= b_row:
            m_row = (t_row + b_row) // 2
            if target < matrix[m_row][l_col]:
                # Target could be in row above
                b_row = m_row - 1
            elif target > matrix[m_row][r_col]:
                # Target could be in row below
                t_row = m_row + 1
            else:
                break

        if t_row > b_row:
            return False

        while l_col <= r_col:
            m_col = (l_col + r_col) // 2
            if target < matrix[m_row][m_col]:
                r_col = m_col - 1
            elif target > matrix[m_row][m_col]:
                l_col = m_col + 1
            else:
                # Target found
                return True

        return False

    def reference(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.searchMatrix(*case))
                else:
                    self.searchMatrix(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
        # Additional
        ([[1], [3]], 1),
        ([[1], [3], [5]], 3),
        ([[1], [3]], 3),
    ]
    test.quantify(test_cases)
