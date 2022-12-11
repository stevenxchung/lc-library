const { performance } = require('perf_hooks');

class Solution {
  method(m, n) {
    let cache2D = Array.from({ length: m }, () =>
      Array.from({ length: n }, () => 0)
    );

    cache2D[m - 1][n - 1] = 1;

    for (let i = m - 1; i >= 0; i--) {
      for (let j = n - 1; j >= 0; j--) {
        if (i + 1 < m && j + 1 < n) {
          cache2D[i][j] += cache2D[i + 1][j];
          cache2D[i][j] += cache2D[i][j + 1];
        } else if (i === m - 1 || j === n - 1) cache2D[i][j] = 1;
      }
    }

    return cache2D[0][0];
  }

  reference(row, col, memo = this.getMemo(row, col)) {
    const isBaseCase = row === 1 || col === 1;
    if (isBaseCase) return 1;

    const hasSeen = memo[row][col] !== 0;
    if (hasSeen) return memo[row][col];

    return this.dfs(
      row,
      col,
      memo
    ); /* Time O(ROWS * COLS) | Space O((ROWS * COLS) + HEIGHT) */
  }

  getMemo = (row, col) =>
    new Array(row + 1)
      .fill() /* Time O(ROWS)| Space O(ROWS) */
      .map(() => new Array(col + 1).fill(0)); /* Time O(COLS)| Space O(COLS) */

  dfs = (row, col, memo) => {
    const left = this.reference(
      row - 1,
      col,
      memo
    ); /* Time O(ROWS * COLS) | Space O(HEIGHT) */
    const right = this.reference(
      row,
      col - 1,
      memo
    ); /* Time O(ROWS * COLS) | Space O(HEIGHT) */

    memo[row][col] = left + right; /* | Space O(ROWS * COLS) */
    return memo[row][col];
  };

  quantify(testCases, runs = 1e6) {
    const runsArr = Array.from({ length: runs });
    const solStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(...input));
        else this.method(...input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(...input));
        else this.reference(...input);
      });
    });
    console.log(
      `Runtime for reference: ${(performance.now() - refStart) / 1000}`
    );
  }
}

const test = new Solution();
const testCases = [
  [3, 7],
  [3, 2],
];
test.quantify(testCases);
