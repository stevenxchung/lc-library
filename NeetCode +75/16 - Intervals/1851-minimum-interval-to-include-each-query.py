'''
You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] describes the ith interval starting at left_i and ending at right_i (inclusive). The size of an interval is defined as the number of integers it contains, or more formally right_i - left_i + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
'''
import bisect
import heapq
from time import time
from typing import List


class Solution:
    def minInterval(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        res = [-1] * len(queries)
        # Sort intervals by size
        intervals.sort(key=lambda i: i[1] - i[0])
        # Sort queries by increasing order
        queries = sorted([q, i] for i, q in enumerate(queries))

        # Binary search for queries contained in interval
        for left, right in intervals:
            i = bisect.bisect(queries, [left])
            while i < len(queries) and queries[i][0] <= right:
                # Insert minimum interval size at proper index
                res[queries.pop(i)[1]] = right - left + 1

        return res

    def reference(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minInterval(*case))
                else:
                    self.minInterval(*case)
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
        ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]),
        ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]),
    ]
    test.quantify(test_cases)
