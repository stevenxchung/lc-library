'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''
from collections import defaultdict, deque
from time import time
from typing import List


class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        # Create a graph for adjacency and traversing
        adj = {i: set() for i in range(numCourses)}
        graph = defaultdict(set)
        for a, b in prerequisites:
            adj[a].add(b)
            graph[b].add(a)

        # Find starting location based on courses with no prereq
        q = []
        for c, pre in adj.items():
            if len(pre) == 0:
                q.append(c)

        res = []
        while q:
            c = q.pop(0)
            res.append(c)
            if len(res) == numCourses:
                return res

            for next_c in graph[c]:
                # Remove prereq from the next course
                adj[next_c].remove(c)
                if len(adj[next_c]) == 0:
                    # Taken all requirements, add next course to queue
                    q.append(next_c)

        return []

    def reference(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        prereq_map = {k: [] for k in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        res = []
        visited, cycle = set(), set()

        def dfs(course: int):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in prereq_map[course]:
                if not dfs(pre):
                    # Cycle detected
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findOrder(*case))
                else:
                    self.findOrder(*case)
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
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        (1, []),
        # Additional
        (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]),
        (3, [[0, 1], [1, 2], [2, 0]]),
        (3, [[0, 1], [0, 2], [1, 2], [2, 1]]),
    ]
    test.quantify(test_cases)
