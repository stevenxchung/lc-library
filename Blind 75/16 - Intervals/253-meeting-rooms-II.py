'''
*LeetCode premium problem
'''
from time import time
from typing import List, Tuple


class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int, int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        # If there are meetings we always need at least one room
        res = 1
        for i in range(1, len(intervals)):
            prev, curr = intervals[i - 1], intervals[i]
            if prev[-1] > curr[0]:
                # Need new conference room if overlap found
                res += 1

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
