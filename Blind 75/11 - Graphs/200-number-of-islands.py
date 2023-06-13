'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
from time import time
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        coord = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = [(r, c)]
            while q:
                r1, c1 = q.pop(0)
                seen.add((r1, c1))
                for dr, dc in coord:
                    r2, c2 = r1 + dr, c1 + dc
                    if (
                        r2 < 0
                        or c2 < 0
                        or r2 >= ROWS
                        or c2 >= COLS
                        or (r2, c2) in seen
                        or grid[r2][c2] == '0'
                    ):
                        continue
                    q.append((r2, c2))

            return

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == '1':
                    bfs(r, c)
                    res += 1

        return res

    def reference(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == '0'
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        return islands

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.numIslands(case))
                else:
                    self.numIslands(case)
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
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
        ],
        [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'],
        ],
        # Additional
        [['1']],
    ]
    test.quantify(test_cases)
