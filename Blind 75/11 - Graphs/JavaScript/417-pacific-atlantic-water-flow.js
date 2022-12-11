const { performance } = require('perf_hooks');

class Solution {
  method(heights) {
    if (!heights) {
      return [];
    }

    const [ROWS, COLS] = [heights.length, heights[0].length];
    let [pacific, atlantic] = [new Set(), new Set()];

    const dfs = (r, c, seen, prevHeight) => {
      if (
        seen.has(`${r}, ${c}`) ||
        r < 0 ||
        c < 0 ||
        r >= ROWS ||
        c >= COLS ||
        heights[r][c] < prevHeight
      )
        return;

      seen.add(`${r}, ${c}`);
      dfs(r + 1, c, seen, heights[r][c]);
      dfs(r - 1, c, seen, heights[r][c]);
      dfs(r, c + 1, seen, heights[r][c]);
      dfs(r, c - 1, seen, heights[r][c]);
    };

    for (let i = 0; i < ROWS; i++) {
      dfs(i, 0, pacific, heights[i][0]);
      dfs(i, COLS - 1, atlantic, heights[i][COLS - 1]);
    }

    for (let j = 0; j < COLS; j++) {
      dfs(0, j, pacific, heights[0][j]);
      dfs(ROWS - 1, j, atlantic, heights[ROWS - 1][j]);
    }

    let res = [];
    for (let i = 0; i < ROWS; i++) {
      for (let j = 0; j < COLS; j++) {
        if (pacific.has(`${i}, ${j}`) && atlantic.has(`${i}, ${j}`))
          res.push([i, j]);
      }
    }

    return res;
  }

  reference(heights) {
    const [pacificReachable, atlanticReachable] =
      this.search(heights); /* Time O(ROWS * COLS) | Space O(ROWS * COLS) */

    return this.searchGrid(
      heights,
      pacificReachable,
      atlanticReachable
    ); /* Time O(ROWS * COLS) | Space O(ROWS * COLS) */
  }

  search = (heights) => {
    const [rows, cols] = [heights.length, heights[0].length];
    const [pacificReachable, atlanticReachable] = [
      this.getMatrix(rows, cols),
      this.getMatrix(rows, cols),
    ]; /* Time O(ROWS * COLS) | Space O(ROWS * COLS) */

    this.searchRows(heights, rows, cols, pacificReachable, atlanticReachable);
    this.searchCols(heights, rows, cols, pacificReachable, atlanticReachable);

    return [pacificReachable, atlanticReachable];
  };

  searchGrid = (
    heights,
    pacificReachable,
    atlanticReachable,
    intersection = []
  ) => {
    const [rows, cols] = [heights.length, heights[0].length];

    for (let row = 0; row < rows; row++) {
      /* Time O(ROWS) */
      for (let col = 0; col < cols; col++) {
        /* Time O(COLS) */
        const isReachable =
          pacificReachable[row][col] && atlanticReachable[row][col];
        if (!isReachable) continue;

        intersection.push([row, col]); /* Space O(ROWS * COLS) */
      }
    }

    return intersection;
  };

  getMatrix = (rows, cols) =>
    new Array(rows)
      .fill() /* Time O(ROWS * COLS) | Space O(ROWS * COLS) */
      .map(() => new Array(cols).fill(false));

  searchRows = (heights, rows, cols, pacificReachable, atlanticReachable) => {
    for (let row = 0; row < rows; row++) {
      /* Time O(ROWS) */
      const [pacificStart, atlanticStart] = [0, cols - 1];

      this.dfs(
        row,
        pacificStart,
        rows,
        cols,
        pacificReachable,
        heights
      ); /* Space O(ROWS * COLS) */
      this.dfs(
        row,
        atlanticStart,
        rows,
        cols,
        atlanticReachable,
        heights
      ); /* Space O(ROWS * COLS) */
    }
  };

  searchCols = (heights, rows, cols, pacificReachable, atlanticReachable) => {
    for (let col = 0; col < cols; col++) {
      /* Time O(COLS) */
      const [pacificStart, atlanticStart] = [0, rows - 1];

      this.dfs(
        pacificStart,
        col,
        rows,
        cols,
        pacificReachable,
        heights
      ); /* Space O(ROWS * COLS) */
      this.dfs(
        atlanticStart,
        col,
        rows,
        cols,
        atlanticReachable,
        heights
      ); /* Space O(ROWS * COLS) */
    }
  };

  dfs = (row, col, rows, cols, isReachable, heights) => {
    isReachable[row][col] = true;

    for (const [_row, _col] of this.getNeighbors(row, rows, col, cols)) {
      if (isReachable[_row][_col]) continue;

      const isLower = heights[_row][_col] < heights[row][col];
      if (isLower) continue;

      this.dfs(
        _row,
        _col,
        rows,
        cols,
        isReachable,
        heights
      ); /* Space O(ROWS * COLS) */
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
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.method(input));
        else this.method(input);
      });
    });
    console.log(
      `Runtime for solution: ${(performance.now() - solStart) / 1000}\n`
    );

    const refStart = performance.now();
    runsArr.map((run, i) => {
      testCases.map((input) => {
        if (i === 0) console.log(this.reference(input));
        else this.reference(input);
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
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
  ],
  [
    [2, 1],
    [1, 2],
  ],
];
test.quantify(testCases);
