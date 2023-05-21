'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''
from time import time
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        seen = set()

        def bfs(r, c):
            queue = [(r, c)]
            seen.add((r, c))
            area = 1

            while queue:
                row, col = queue.pop(0)
                for dr, dc in directions:
                    r_new, c_new = (row + dr), (col + dc)
                    if (
                        0 <= r_new < ROWS
                        and 0 <= c_new < COLS
                        and grid[r_new][c_new] == 1
                        and (r_new, c_new) not in seen
                    ):
                        seen.add((r_new, c_new))
                        queue.append((r_new, c_new))
                        area += 1

            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    max_area = max(max_area, bfs(r, c))

        return max_area

    def reference(self, grid: List[List[int]]) -> int:
        max_area = 0
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in seen
                or grid[r][c] == 0
            ):
                return 0

            seen.add((r, c))
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxAreaOfIsland(case))
                else:
                    self.maxAreaOfIsland(case)
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
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        [[0, 0, 0, 0, 0, 0, 0, 0]],
    ]
    test.quantify(test_cases)
