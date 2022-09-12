'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [a_i, b_i] indicates that there is an edge between nodes a_i and b_i in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
'''
import collections
from time import time
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {v: -1 for v in range(1, len(edges) + 1)}

        def find(u):
            if parent[u] != -1:
                # Find root with path compression
                parent[u] = find(parent[u])
                return parent[u]
            else:
                return u

        def union(u, v):
            parent_of_u = find(u)
            parent_of_v = find(v)

            if parent_of_u != parent_of_v:
                # After adding edge, graph is still a tree without cycle
                parent[parent_of_u] = parent_of_v
                return True
            else:
                # U and V has same parent node
                return False

        for u, v in edges:
            if not union(u, v):
                return [u, v]

    def reference(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findRedundantConnection(case))
                else:
                    self.findRedundantConnection(case)
        print(f'Runtime for our solution: {time() - sol_start}')

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
        [[1, 2], [1, 3], [2, 3]],
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
        # Additional
        [[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]  # [1, 3]
    ]
    test.quantify(test_cases)
