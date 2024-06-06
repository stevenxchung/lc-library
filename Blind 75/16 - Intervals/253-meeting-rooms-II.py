'''
*LeetCode premium problem
'''

from time import time
from typing import List, Tuple


class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int, int]]) -> int:
        start_times = sorted([start for start, _ in intervals])
        end_times = sorted([end for _, end in intervals])
        res, count = 0, 0

        # Accumulate results with two pointers
        i, j = 0, 0
        while i < len(intervals):
            if start_times[i] < end_times[j]:
                # Number of meetings has increased
                i += 1
                count += 1
            else:
                # Number of meetings has decreased
                j += 1
                count -= 1
            res = max(res, count)

        return res

    def reference(self, intervals: List[Tuple[int, int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minMeetingRooms(case))
                else:
                    self.minMeetingRooms(case)
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
        [(0, 30), (5, 10), (15, 20)],
        # Additional
        [(5, 10), (15, 20), (0, 30)],
        [(0, 1)],
        [],
    ]
    test.quantify(test_cases)
