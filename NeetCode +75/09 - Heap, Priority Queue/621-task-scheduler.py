'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
'''
from collections import Counter, deque
import heapq
from time import time
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Cooling period is zero
        if n == 0:
            return len(tasks)

        task_dict = Counter(tasks)

        max_occ = max(task_dict.values())

        total_max_occ = 0
        for occ in task_dict.values():
            if occ == max_occ:
                total_max_occ += 1

        interval = (max_occ - 1) * (n + 1) + total_max_occ

        return max(interval, len(tasks))

    def reference(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.leastInterval(case[0], case[1]))
                else:
                    self.leastInterval(case[0], case[1])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1]))
                else:
                    self.reference(case[0], case[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (['A', 'A', 'A', 'B', 'B', 'B'], 2),
        (['A', 'A', 'A', 'B', 'B', 'B'], 0),
        (['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2)
    ]
    test.quantify(test_cases)
