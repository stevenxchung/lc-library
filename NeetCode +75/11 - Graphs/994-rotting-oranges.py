'''
You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
from collections import deque
from copy import deepcopy
from time import time
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        # Gather rotting oranges
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((0, r, c))
                    seen.add((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            t, r1, c1 = q.popleft()
            if fresh == 0:
                return t

            for dr, dc in directions:
                r2, c2 = r1 + dr, c1 + dc
                if (
                    r2 < 0
                    or c2 < 0
                    or r2 >= ROWS
                    or c2 >= COLS
                    or (r2, c2) in seen
                    or grid[r2][c2] != 1
                ):
                    continue
                q.append((t + 1, r2, c2))
                seen.add((r2, c2))
                fresh -= 1

        # Handle edge case when there are no fresh oranges to start
        return -1 if fresh > 0 else t

    def reference(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # If in bounds and not rotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and (row, col) not in seen
                        and grid[row][col] == 1
                    ):
                        seen.add((row, col))
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.orangesRotting(case))
                else:
                    self.orangesRotting(case)
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
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 2]],
    ]
    test.quantify(test_cases)
