'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''

import math
from time import time
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find minimum k bananas to eat given h time to finish
        def t_lte_h(speed):
            return sum(math.ceil(p / speed) for p in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l) // 2
            if t_lte_h(k):
                # Time to finish is <= h, set r to new k
                r = k
            else:
                # Otherwise, move lower bound up
                l = k + 1

        return l

    def reference(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minEatingSpeed(*case))
                else:
                    self.minEatingSpeed(*case)
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
        ([3, 6, 7, 11], 8),
        ([30, 11, 23, 4, 20], 5),
        ([30, 11, 23, 4, 20], 6),
        # Additional
        ([312884470], 312884469),
    ]
    test.quantify(test_cases)
