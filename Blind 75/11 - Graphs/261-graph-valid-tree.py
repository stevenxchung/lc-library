'''
*LeetCode premium problem
'''
from time import time
from typing import List


class Solution:
    def isValidTree(self, n: int, edges: List[List[int]]) -> bool:
        # Empty graph counts as a tree
        if len(edges) == 0:
            return True

        node_map = {i: [] for i in range(n)}
        for a, b in edges:
            node_map[a].append(b)

        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)
            for v in node_map[curr]:
                if v == prev:
                    # Skip if next node is prev
                    continue
                if not dfs(v, curr):
                    # Cycle detected
                    return False
            return True

        # If there are more components or groups of nodes, len(visited) != n
        return dfs(0, -1) and len(visited) == n

    def reference(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.isValidTree(case[0], case[1]))
                else:
                    self.isValidTree(case[0], case[1])
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
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
        # Additional
        (7, [[0, 1], [0, 2], [3, 5], [5, 6], [1, 4]]),
    ]
    test.quantify(test_cases)
