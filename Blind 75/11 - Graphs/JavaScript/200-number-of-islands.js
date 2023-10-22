const { performance } = require("perf_hooks");

class Solution {
  method(grid) {
    const [ROWS, COLS] = [grid.length, grid[0].length];

    const dfs = (r, c) => {
      if (r < 0 || c < 0 || r >= ROWS || c >= COLS || grid[r][c] === "0")
        return;

      grid[r][c] = "0";
      dfs(r + 1, c);
      dfs(r - 1, c);
      dfs(r, c + 1);
      dfs(r, c - 1);
    };

    let count = 0;
    for (let i = 0; i < ROWS; i++) {
      for (let j = 0; j < COLS; j++) {
        if (grid[i][j] === "1") {
          dfs(i, j);
          count += 1;
        }
      }
    }

    return count;
  }

  reference(grid, connectedComponents = 0) {
    const [rows, cols] = [grid.length, grid[0].length];

    for (let row = 0; row < rows; row++) {
      /* Time O(ROWS) */
      for (let col = 0; col < cols; col++) {
        /* Time O(COLS) */
        const isIsland = grid[row][col] === "1";
        if (isIsland) connectedComponents++;

        this.dfs(grid, row, rows, col, cols); /* Space O(ROWS * COLS) */
      }
    }

    return connectedComponents;
  }

  dfs = (grid, row, rows, col, cols) => {
    const isBaseCase = grid[row][col] === "0";
    if (isBaseCase) return;

    grid[row][col] = "0";

    for (const [_row, _col] of this.getNeighbors(row, rows, col, cols)) {
      this.dfs(grid, _row, rows, _col, cols); /* Space O(ROWS * COLS) */
    }
  };

  getNeighbors = (row, rows, col, cols) =>
    [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]
      .map(([_row, _col]) => [row + _row, col + _col])
      .filter(
        ([_row, _col]) => 0 <= _row && _row < rows && 0 <= _col && _col < cols
      );

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.method(copy));
        else this.method(copy);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((_, i) => {
      testCases.map((input) => {
        // Create deep copy
        const copy = JSON.parse(JSON.stringify(input));
        if (i === 0) console.log(this.reference(copy));
        else this.reference(copy);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = [
  [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
  ],
  [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
  ],
  // Additional
  [["1"]],
];
test.quantify(testCases);
