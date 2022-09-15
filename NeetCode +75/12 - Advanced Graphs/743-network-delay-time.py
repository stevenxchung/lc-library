'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (u_i, v_i, w_i), where u_i is the source node, v_i is the target node, and w_i is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''
import collections
import heapq
from time import time
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        edges = {}
        for u, v, w in times:
            if u not in edges:
                edges[u] = [(v, w)]
            else:
                edges[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        t = 0
        while heap:
            # Prioritize shortest path first
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            # BFS
            if n1 in edges:
                for n2, w2 in edges[n1]:
                    if n2 not in visited:
                        path = w1 + w2
                        heapq.heappush(heap, (path, n2))

        return t if len(visited) == n else -1

    def reference(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.networkDelayTime(case[0], case[1], case[2]))
                else:
                    self.networkDelayTime(case[0], case[1], case[2])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1], case[2]))
                else:
                    self.reference(case[0], case[1], case[2])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (
            [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
            4,
            2
        ),
        (
            [[1, 2, 1]],
            2,
            1
        ),
        (
            [[1, 2, 1]],
            2,
            2
        )
    ]
    test.quantify(test_cases)
