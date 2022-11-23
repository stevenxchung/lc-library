'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from time import time
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = i + 1
        while i < len(prices) and j < len(prices):
            profit = prices[j] - prices[i]
            if profit < 0:
                i = j
                continue
            elif profit > 0 and profit > max_profit:
                max_profit = profit
            j += 1

        return max_profit

    def reference(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])

        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxProfit(case))
                else:
                    self.maxProfit(case)
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
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]
    ]
    test.quantify(test_cases)
