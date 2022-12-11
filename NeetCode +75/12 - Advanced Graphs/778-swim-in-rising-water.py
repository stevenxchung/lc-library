'''
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
'''
from copy import deepcopy
import heapq
from time import time
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Djikstra's/A* (note that there is always a solution, so 'while True' is acceptable)
        n = len(grid) - 1
        # (time, distance from finish, row, col)
        queue = [(grid[n][n], 2 * n, 0, 0)]
        while True:
            # Get the next item from queue
            t, d, i, j = heapq.heappop(queue)

            # Return time if goal reached
            if d == 0:
                return t

            # Only process unvisited squares
            if grid[i][j] > -1:
                # Update time and mark as visited
                t = max(t, grid[i][j])
                grid[i][j] = -1

                # Traverse unvisited neighbors
                if i > 0 and grid[i - 1][j] > -1:
                    # Move Up
                    heapq.heappush(queue, (t, d + 1, i - 1, j))
                if j > 0 and grid[i][j - 1] > -1:
                    # Move Left
                    heapq.heappush(queue, (t, d + 1, i, j - 1))
                if i < n and grid[i + 1][j] > -1:
                    # Move Down
                    heapq.heappush(queue, (t, d - 1, i + 1, j))
                if j < n and grid[i][j + 1] > -1:
                    # Move Right
                    heapq.heappush(queue, (t, d - 1, i, j + 1))

    def reference(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR == N
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.swimInWater(copy))
                else:
                    self.swimInWater(copy)
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
        [[0, 2], [1, 3]],
        [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ],
    ]
    test.quantify(test_cases)
