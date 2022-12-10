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
        prereq_map = {k: [] for k in range(numCourses)}
        for a, b in prerequisites:
            prereq_map[a].append(b)

        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if prereq_map[course] == []:
                return True

            cycle.add(course)
            for c in prereq_map[course]:
                if not dfs(c):
                    return False
            cycle.remove(course)
            prereq_map[course] = []

            return True

        for k in prereq_map.keys():
            if not dfs(k):
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
                    print(self.canFinish(case[0], case[1]))
                else:
                    self.canFinish(case[0], case[1])
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
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        # Additional
        (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]),
        (3, [[0, 1], [1, 2], [2, 0]]),
    ]
    test.quantify(test_cases)
