'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''


class Solution:
    def maxProfit(self, prices):
        minPrice = (2**31)-1
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit


# input = [7, 1, 5, 3, 6, 4]
# input = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# input = []
input = [2, 4, 1]
sol = Solution()
print(sol.maxProfit(input))
