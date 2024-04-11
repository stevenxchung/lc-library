'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

from collections import deque
from time import time
from typing import List


class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        # Where i = course and reqs[i] = n_courses
        reqs = [0] * numCourses
        for c, pre in prerequisites:
            adj[pre].append(c)
            reqs[c] += 1

        q = deque()
        for i in range(numCourses):
            # Start with first required courses
            if reqs[i] == 0:
                q.append(i)

        taken = []
        while q:
            c = q.popleft()
            taken.append(c)
            for c_next in adj[c]:
                reqs[c_next] -= 1
                if reqs[c_next] == 0:
                    # Only add to queue if all prerequisites taken
                    q.append(c_next)

        # If all courses were taken, length should match up
        return taken if len(taken) == numCourses else []

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
