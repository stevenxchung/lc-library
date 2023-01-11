'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
'''
from time import time
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        cache = [[0] * N for i in range(M)]

        def dfs(i, j):
            # Only run on unvisited
            if cache[i][j] == 0:
                val = matrix[i][j]

                # Map out directions
                top = (
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0
                )
                bottom = dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0
                left = dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0
                right = (
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0
                )
                # Update cache by selecting max path
                cache[i][j] = 1 + max(top, bottom, left, right)

            return cache[i][j]

        # Get max of all paths
        return max(dfs(x, y) for x in range(M) for y in range(N))

    def reference(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or matrix[r][c] <= prevVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.longestIncreasingPath(case))
                else:
                    self.longestIncreasingPath(case)
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
        [[9, 9, 4], [6, 6, 8], [2, 1, 1]],
        [[3, 4, 5], [3, 2, 6], [2, 2, 1]],
    ]
    test.quantify(test_cases)
