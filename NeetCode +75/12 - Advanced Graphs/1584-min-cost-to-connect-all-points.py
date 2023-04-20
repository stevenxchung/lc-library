'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [x_i, y_i].

The cost of connecting two points [x_i, y_i] and [x_j, y_j] is the manhattan distance between them: |x_i - x_j| + |y_i - y_j|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''
from collections import defaultdict
import heapq
from time import time
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Build adjacency list of (cost, index)
        N = len(points)
        cost_map = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                cost_map[i].append((cost, j))
                cost_map[j].append((cost, i))

        total_cost = 0
        seen = set()
        heap = [(0, 0)]  # (cost, index)
        while len(seen) < N:
            cost, idx = heapq.heappop(heap)
            if idx in seen:
                continue
            total_cost += cost
            seen.add(idx)
            for nei_cost, nei in cost_map[idx]:
                if nei not in seen:
                    heapq.heappush(heap, (nei_cost, nei))

        return total_cost

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
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
        # Additional
        [[0, 0], [1, 1], [1, 0], [-1, 1]],
    ]
    test.quantify(test_cases)
