'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
from math import inf
from time import time
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [0] * amount

        def dfs(coins, amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if cache[amount - 1] > 0:
                return cache[amount - 1]

            minimum = inf
            for c in coins:
                cost = dfs(coins, amount - c)
                if not (0 <= cost < minimum):
                    continue
                minimum = cost + 1
            cache[amount - 1] = minimum if minimum != inf else -1

            return cache[amount - 1]

        return dfs(coins, amount)

    def reference(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.coinChange(*case))
                else:
                    self.coinChange(*case)
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
    test_cases = [([1, 2, 5], 11), ([2], 3), ([1], 0)]
    test.quantify(test_cases)
