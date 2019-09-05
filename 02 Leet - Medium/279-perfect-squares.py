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
    # Dynamic programming
    def numSquares(self, n):
        if n <= 0:
            return 0

        # Array of least number of perfect squares which sum to i for perfSquares[i]. If len(perfSquares) > 12 then we have already calculated the result
        perfSquares = [0]

        # While len(perfSquares) <= n we can calculate next result until we get result for n
        while len(perfSquares) <= n:
            size = len(perfSquares)
            squares = 2147483647

            i = 1
            while i * i <= size:
                squares = min(squares, perfSquares[size - i * i] + 1)
                i += 1

            perfSquares.append(squares)

        return perfSquares[n]

    def numSquaresBFS(self, n):
        dist = 1
        q1 = [(0, 1)]
        q2 = []
        label = [10] * (n + 1)

        # BFS using shortest path, length of all edges are 1 and graph has vertices which are numbers from 0 to n
        while True:
            for node, length in q1:
                for edge in range(length, n + 1):
                    nextNode = node + edge * edge
                    if nextNode == n:
                        return dist
                    elif nextNode > n:
                        break
                    elif label[nextNode] > dist:
                        label[nextNode] = dist
                        q2.append((nextNode, edge))
            q1, q2 = q2, []
            dist += 1


input = 12
# input = 13
sol = Solution()
print(sol.numSquares(input))
print(sol.numSquaresBFS(input))
