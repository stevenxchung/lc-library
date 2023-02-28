'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''
from math import inf
from time import time
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Cooldown has no stock while holding does
        cooldown, sell, hold = 0, 0, -inf
        for price in prices:
            # Store previous prices for reference
            prev_cooldown, prev_sell, prev_hold = cooldown, sell, hold
            # New prices are based on previous prices and/or current price
            cooldown = max(prev_cooldown, prev_sell)
            sell = prev_hold + price
            hold = max(prev_hold, prev_cooldown - price)
        # Can only sell or cooldown at end state
        return max(sell, cooldown)

    def reference(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.maxProfit(case))
                else:
                    self.maxProfit(case)
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
    test_cases = [[1, 2, 3, 0, 2], [1]]
    test.quantify(test_cases)
