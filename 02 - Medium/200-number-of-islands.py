'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''


class Solution:
    def numIslands(self, grid):
        # Check edge cases
        if grid == None or len(grid) == 0:
            return 0
        # Initialize island count
        islands = 0
        # Trigger DFS when a '1' is hit
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1':
                    islands += self.dfsHelper(grid, i, j)

        return islands

    def dfsHelper(self, grid, i, j):
        # Don't care if we are on a '0'
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return 0
        # Otherwise, traverse grid, set grid[i][j] to '0' to avoid traversing again
        grid[i][j] = '0'
        self.dfsHelper(grid, i + 1, j)
        self.dfsHelper(grid, i - 1, j)
        self.dfsHelper(grid, i, j + 1)
        self.dfsHelper(grid, i, j - 1)

        return 1


input = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
sol = Solution()
print(sol.numIslands(input))
