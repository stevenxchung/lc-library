'''
*LeetCode premium problem
'''
from time import time
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        alien_dict = {c: set() for w in words for c in w}
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            if w1[0] == w2[0] and len(w1) > len(w2):
                # First word cannot start with same char and be longer
                return ''
            for k in range(len(w1)):
                if w1[k] != w2[k]:
                    alien_dict[w1[k]].add(w2[k])
                    break

        # True == current path, False == visited
        path_map = {}
        res = []

        def dfs(c):
            if c in path_map:
                return path_map[c]

            path_map[c] = True
            for nei in alien_dict[c]:
                if dfs(nei):
                    # Loop exists
                    return True
            path_map[c] = False
            res.append(c)

            return False

        for c in alien_dict:
            if c in path_map:
                continue
            if dfs(c):
                # Loop exists
                return ''

        # Reverse due to post-order DFS
        res.reverse()
        return ''.join(res)

    def reference(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ''

        res.reverse()
        return ''.join(res)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.alienOrder(case))
                else:
                    self.alienOrder(case)
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
    test_cases = [['wrt', 'wrf', 'er', 'ett', 'rftt']]
    test.quantify(test_cases)
