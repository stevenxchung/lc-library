'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first if you want to take course a_i.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
'''
from time import time
from typing import List


class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        def bfs(start):
            q = [({start}, start)]  # (set(), course)
            while q:
                path, c = q.pop(0)
                for pre in adj[c]:
                    if pre in path:
                        # Cycle detected
                        return False
                    if pre == []:
                        continue
                    # Copy to track separate paths when branching
                    clone = path.copy()
                    clone.add(pre)
                    q.append((clone, pre))

            return True

        # To capture multiple sets of unrelated courses
        for k in adj.keys():
            if not bfs(k):
                return False

        return True

    def reference(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        # DFS
        preMap = {i: [] for i in range(numCourses)}

        # Map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.canFinish(*case))
                else:
                    self.canFinish(*case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(*case))
                else:
                    self.reference(*case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        # Additional
        (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]),
        (3, [[0, 1], [1, 2], [2, 0]]),
    ]
    test.quantify(test_cases)
