'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
'''
from time import time
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0
                or r >= ROWS or c >= COLS
                    or board[r][c] not in node.children or board[r][c] == '#'):
                return

            # Add letter to word and increment node
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.is_end:
                res.add(word)

            # Store current letter for backtracking
            temp = board[r][c]
            board[r][c] = '#'

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            # Reset to original letter
            board[r][c] = temp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, '')

        return list(res)

    def reference(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs_reference(r, c, node, word):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                    or (r, c) in visit
                    or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_end:
                res.add(word)

            dfs_reference(r - 1, c, node, word)
            dfs_reference(r + 1, c, node, word)
            dfs_reference(r, c - 1, node, word)
            dfs_reference(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs_reference(r, c, trie.root, '')

        return list(res)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findWords(case[0], case[1]))
                else:
                    self.findWords(case[0], case[1])
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
            [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']],
            ['oath', 'pea', 'eat', 'rain'],
        ),
        (
            [['a', 'b'], ['c', 'd']],
            ['abcb']
        )
    ]
    test.quantify(test_cases)
