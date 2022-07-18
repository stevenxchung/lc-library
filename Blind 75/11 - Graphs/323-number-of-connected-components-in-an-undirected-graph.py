'''
*LeetCode premium problem
'''
from time import time
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_map = {i: [] for i in range(n)}
        for a, b in edges:
            node_map[a].append(b)

        visited = set()
        res = 0

        def dfs(curr, prev):
            if curr in visited:
                return

            visited.add(curr)
            for v in node_map[curr]:
                if v == prev:
                    continue
                dfs(v, curr)

        for k in node_map.keys():
            if k not in visited:
                # New component or group found, set to -1 initially
                dfs(k, -1)
                res += 1

        return res

    def reference(self, n: int, edges: List[List[int]]) -> int:
        parent_arr = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != parent_arr[res]:
                parent_arr[res] = parent_arr[parent_arr[res]]
                res = parent_arr[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parent_arr[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent_arr[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.countComponents(case[0], case[1]))
                else:
                    self.countComponents(case[0], case[1])
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
        (5,
         [
             [0, 1],
             [1, 2],
             [3, 4]
         ])
    ]
    test.quantify(test_cases)
