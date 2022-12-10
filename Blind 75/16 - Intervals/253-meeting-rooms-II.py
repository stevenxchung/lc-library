'''
*LeetCode premium problem
'''
from time import time
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # We always need at least one room
        rooms = 1
        intervals.sort()
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                # Need new meeting room if overlapping
                rooms += 1

        return rooms

    def reference(self, intervals: List[List[int]]) -> int:
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
        # [(0, 30), (5, 10), (15, 20)],
        # Additional
        [(5, 10), (15, 20), (0, 30)]
    ]
    test.quantify(test_cases)
