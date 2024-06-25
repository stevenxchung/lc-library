'''
You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] describes the ith interval starting at left_i and ending at right_i (inclusive). The size of an interval is defined as the number of integers it contains, or more formally right_i - left_i + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
'''

import heapq
from time import time
from typing import List


class Solution:
    def minInterval(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        intervals.sort()
        res = {}  # {query_value: min_size}
        min_heap = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                # Add to heap when query in range
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(min_heap, (size, end))
                i += 1

            while min_heap and min_heap[0][1] < q:
                # Pop if outside of range
                heapq.heappop(min_heap)
            # Top of heap contains minimum interval size if not empty
            res[q] = min_heap[0][0] if min_heap else -1
        # Unpack minimum interval sizes
        return [res[q] for q in queries]

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
