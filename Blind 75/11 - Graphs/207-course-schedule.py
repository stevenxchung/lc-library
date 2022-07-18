'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
from time import time
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {k: [] for k in range(numCourses)}
        for a, b in prerequisites:
            prereq_map[a].append(b)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereq_map[course] == []:
                return True

            visited.add(course)
            for c in prereq_map[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            prereq_map[course] = []
            return True

        for k in prereq_map.keys():
            if not dfs(k):
                return False

        return True

    def reference(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

    def quantify(self, test_cases, runs=100000):
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
        # (2,
        #  [[1, 0]]),
        # (2,
        #  [
        #      [1, 0],
        #      [0, 1]
        #  ])
        # Additional
        (5,
         [
             [0, 1],
             [0, 2],
             [1, 3],
             [1, 4],
             [3, 4]
         ]),
        (3,
         [
             [0, 1],
             [1, 2],
             [2, 0]
         ])
    ]
    test.quantify(test_cases)
