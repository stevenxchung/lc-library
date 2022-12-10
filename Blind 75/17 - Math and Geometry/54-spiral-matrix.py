'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''
from time import time
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        t, b = 0, len(matrix)
        l, r = 0, len(matrix[0])
        while l < r and t < b:
            # Left to right
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            # Top to bottom
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and t < b):
                break

            # Right to left
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            # Bottom to top
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res

    def reference(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = [*zip(*matrix)]
            matrix = matrix[::-1]
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.spiralOrder(case))
                else:
                    self.spiralOrder(case)
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
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ]
    test.quantify(test_cases)
