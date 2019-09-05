'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''


class Solution:
    def numSquares(self, n):
        if n <= 0:
            return 0

        perfSquares = [0]

        while len(perfSquares) <= n:
            size = len(perfSquares)
            squares = 2147483647

            i = 1
            while i * i <= size:
                squares = min(squares, perfSquares[size - i * i] + 1)
                i += 1

            perfSquares.append(squares)

        return perfSquares[n]


input = 12
# input = 13
sol = Solution()
print(sol.numSquares(input))
