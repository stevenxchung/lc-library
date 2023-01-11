'''
Given an array of points where points[i] = [x_i, y_i] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x_1 - x_2)^2 + (y_1 - y_2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
import heapq
import math
from time import time
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [
            (math.sqrt(pair[0] ** 2 + pair[1] ** 2), pair) for pair in points
        ]
        heapq.heapify(min_heap)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(min_heap)[1])

        return res

    def reference(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.kClosest(*case))
                else:
                    self.kClosest(*case)
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
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
        # Additional
        ([[1, 3], [-2, 2], [2, -2]], 2),
    ]
    test.quantify(test_cases)
