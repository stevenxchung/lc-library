/* 

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

*/

// let grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]];
let grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
let sum = 0;

let maxGrid = grid => {
  // Skyline viewed from top and bottom
  let TB = new Array(grid.length).fill(0);
  // Skyline viewed from left and right
  let LR = new Array(grid.length).fill(0);

  // Traverse through grid to determine skyline values
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      // Check if current value is greater and if not push value to array
      findSkyline(grid, TB, LR, i, j);
    }
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      maxOutGrid(grid, TB, LR, i, j);
    }
  }

  return { TB, LR, grid, sum };
};

let findSkyline = (grid, TB, LR, i, j) => {
  // Top and bottom skyline
  if (j === 0 && grid[i][0] > TB[0]) {
    TB[0] = grid[i][0];
  } else if (j === 1 && grid[i][1] > TB[1]) {
    TB[1] = grid[i][1];
  } else if (j === 2 && grid[i][2] > TB[2]) {
    TB[2] = grid[i][2];
  } else if (j === 3 && grid[i][3] > TB[3]) {
    TB[3] = grid[i][3];
  }

  // Left and right skyline
  if (i === 0 && grid[0][j] > LR[0]) {
    LR[0] = grid[0][j];
  } else if (i === 1 && grid[1][j] > LR[1]) {
    LR[1] = grid[1][j];
  } else if (i === 2 && grid[2][j] > LR[2]) {
    LR[2] = grid[2][j];
  } else if (i === 3 && grid[3][j] > LR[3]) {
    LR[3] = grid[3][j];
  }
};

// Modifies each element which is not the max
let maxOutGrid = (grid, TB, LR, i, j) => {
  let difference = 0;
  // Handle corner cases
  if (grid[i][j] < TB[j] && grid[i][j] < LR[i]) {
    // Take the smaller of the two
    difference = Math.min(TB[j], LR[i]) - grid[i][j];
    grid[i][j] += difference;
    sum += difference;
  }
};

console.log(maxGrid(grid));

// Data structure for top and bottom skyline
/*
TB = [grid[i][0], grid[i][1], grid[i][2], grid[i][3]]
*/

// Data structure for left and right skyline
/*
LR = [grid[0][j], grid[1][j], grid[2][j], grid[3][j]]
*/

// Java Solution
/*
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int N = grid.length;
        int[] rowMaxes = new int[N];
        int[] colMaxes = new int[N];

        for (int r = 0; r < N; ++r)
            for (int c = 0; c < N; ++c) {
                rowMaxes[r] = Math.max(rowMaxes[r], grid[r][c]);
                colMaxes[c] = Math.max(colMaxes[c], grid[r][c]);
        }

        int ans = 0;
        for (int r = 0; r < N; ++r)
            for (int c = 0; c < N; ++c)
                ans += Math.min(rowMaxes[r], colMaxes[c]) - grid[r][c];

        return ans;
    }
}
*/