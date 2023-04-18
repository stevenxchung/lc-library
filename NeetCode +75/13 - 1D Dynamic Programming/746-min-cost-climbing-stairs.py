'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
from copy import deepcopy
from time import time
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = cost[:]
        for i in range(len(arr) - 3, -1, -1):
            # Cost at index only depends on previous two cumulative costs
            arr[i] += min(arr[i + 1], arr[i + 2])

        return min(arr[0], arr[1])

    def reference(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minCostClimbingStairs(case))
                else:
                    self.minCostClimbingStairs(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                copy = deepcopy(case)
                if i == 0:
                    print(self.reference(copy))
                else:
                    self.reference(copy)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]
    test.quantify(test_cases)
