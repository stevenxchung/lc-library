'''
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''

from time import time
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = 0
        valid_intervals = 1

        for i in range(1, len(intervals)):
            # Check how many intervals are valid
            if intervals[prev][1] <= intervals[i][0]:
                prev = i
                valid_intervals += 1

        # Invalid intervals is the difference
        return len(intervals) - valid_intervals

    def reference(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.eraseOverlapIntervals(case))
                else:
                    self.eraseOverlapIntervals(case)
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
        [[1, 2], [2, 3], [3, 4], [1, 3]],
        [[1, 2], [1, 2], [1, 2]],
        [[1, 2], [2, 3]],
        # Additional
        [
            [-52, 31],
            [-73, -26],
            [82, 97],
            [-65, -11],
            [-62, -49],
            [95, 99],
            [58, 95],
            [-31, 49],
            [66, 98],
            [-63, 2],
            [30, 47],
            [-40, -26],
        ],
        [
            [-52, 31],
            [-73, -26],
            [82, 97],
            [-65, -11],
            [-62, -49],
            [95, 99],
            [58, 95],
            [-31, 49],
            [66, 98],
            [-63, 2],
            [30, 47],
            [-40, -26],
        ],
    ]
    test.quantify(test_cases)
