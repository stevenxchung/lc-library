'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
from copy import deepcopy
from time import time
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return

            board[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return

        # Find 'O' first and flip them to '#'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (
                    r in {0, ROWS - 1} or c in {0, COLS - 1}
                ):
                    dfs(r, c)

        # Flip all 'O' to 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # Reverse '#' back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '#':
                    board[r][c] = 'O'

        return board

    def reference(self, board: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (
                    r in [0, ROWS - 1] or c in [0, COLS - 1]
                ):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        return board

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                # Create deep copy
                copy = deepcopy(case)
                if i == 0:
                    print(self.solve(copy))
                else:
                    self.solve(copy)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
        [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
        ],
        [['X']],
        [
            ['O', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'X'],
            ['O', 'O', 'X', 'O'],
            ['O', 'O', 'O', 'O'],
        ],
    ]
    test.quantify(test_cases)
