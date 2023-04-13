'''
*LeetCode premium problem
'''
from math import inf
from time import time
from typing import List, Tuple


class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int, int]]) -> bool:
        prev_end = -inf
        intervals.sort()
        for _, end in intervals:
            if prev_end > end:
                return False
            else:
                prev_end = end

        return True

    def reference(self, intervals: List[Tuple[int, int]]) -> bool:
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.canAttendMeetings(case))
                else:
                    self.canAttendMeetings(case)
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
    ]
    test.quantify(test_cases)
