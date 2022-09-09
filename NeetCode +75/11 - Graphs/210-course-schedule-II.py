'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''
from time import time
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

    def reference(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.findOrder(case[0], case[1]))
                else:
                    self.findOrder(case[0], case[1])
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
        (2,
         [[1, 0]]),
        (4,
         [
             [1, 0],
             [2, 0],
             [3, 1],
             [3, 2]
         ])
    ]
    test.quantify(test_cases)
