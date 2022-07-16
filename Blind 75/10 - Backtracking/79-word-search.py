'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
from time import time
from typing import List


class Solution:
    def dfs_helper(self, i: int, j: int, board: List[List[str]], word: str):
        if len(word) == 0:
            # End of word
            return True
        if i < 0 or j < 0 \
                or i >= len(board) or j >= len(board[0]) \
                or board[i][j] != word[0]:
            return

        temp = board[i][j]
        # To prevent visiting self
        board[i][j] = '#'
        res = self.dfs_helper(i - 1, j, board, word[1:]) \
            or self.dfs_helper(i + 1, j, board, word[1:]) \
            or self.dfs_helper(i, j - 1, board, word[1:]) \
            or self.dfs_helper(i, j + 1, board, word[1:])
        # Revert
        board[i][j] = temp

        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        if not board:
            return False
        for i in range(ROWS):
            for j in range(COLS):
                if self.dfs_helper(i, j, board, word):
                    return True

        return False

    def reference(self, board: List[List[str]], word: str) -> bool:
        return

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.exist(case[0], case[1]))
                else:
                    self.exist(case[0], case[1])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1]))
                else:
                    self.reference(case[0], case[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            'ABCCED'
        ),
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            'SEE'
        ),
        (
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            'ABCB'
        )
    ]
    test.quantify(test_cases)
