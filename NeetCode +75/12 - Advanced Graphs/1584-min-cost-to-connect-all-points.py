'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [x_i, y_i].

The cost of connecting two points [x_i, y_i] and [x_j, y_j] is the manhattan distance between them: |x_i - x_j| + |y_i - y_j|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''
import heapq
import math
from time import time
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_total_cost = 0
        for p1 in points:
            costs = []
            for p2 in points:
                if p1 == p2:
                    continue
                dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                costs.append(dist)
            min_total_cost += min(costs)

        return math.ceil(min_total_cost)

    def reference(self, points: List[List[int]]) -> int:
        # Create adjacency list for all points with (cost, points[i])
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algorithm, use min heap to prioritize min cost
        res, seen, min_heap = 0, set(), [(0, 0)]
        while len(seen) < N:
            cost, point = heapq.heappop(min_heap)
            if point in seen:
                continue
            res += cost
            seen.add(point)
            # Explore neighbors from adjacency list
            for nei_cost, nei in adj[point]:
                if nei not in seen:
                    heapq.heappush(min_heap, (nei_cost, nei))

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minCostConnectPoints(case))
                else:
                    self.minCostConnectPoints(case)
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
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        [[3, 12], [-2, 5], [-4, 1]],
    ]
    test.quantify(test_cases)
